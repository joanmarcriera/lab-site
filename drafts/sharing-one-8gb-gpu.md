---
title: "Nine containers, one 8 GB graphics card, and a model that spilled onto the CPU"
date: 2026-10-16
draft: true
tags: [gpu, homelab, ollama, docker]
summary: "A consumer GPU cannot be partitioned, so sharing it is a matter of manners. What the card looked like while two tenants fought over it, and the settings that keep it usable."
---

## Problem

My storage server has one graphics card, an RTX 4060 with 8 GB of memory. Nine containers have
it mapped: a local LLM server (Ollama), the photo library's server and its machine-learning
service, two speech transcription services, an embedding batch job, an image-generation
pipeline (ComfyUI), and two media servers that use its video encoder.

A data-centre GPU can be cut into hard slices. A consumer one cannot. The driver will
time-slice compute between processes, so *access* is never the problem. **Memory is.** If the
models that are resident add up to more than 8 GB, something either crashes or quietly falls
back to the CPU, and nothing tells you which.

## Approach

Since the memory cannot be fenced, the sharing has to be cooperative:

1. **Release memory when idle.** Every tenant gets a timeout after which its model is unloaded.
2. **Serialise the heavy jobs.** Two things that each want most of the card should queue, not
   race.
3. **Look at placement, not just presence.** "The model is loaded" and "the model is on the GPU"
   are different statements.

## Steps

The settings on the tenants that matter, read from the running containers:

```
whisperx-asr           MODEL_KEEP_ALIVE_SECONDS=600  PRELOAD_MODEL=  DEVICE=cuda  COMPUTE_TYPE=int8_float16
ix-ollama-ollama-1     OLLAMA_KEEP_ALIVE=5m  OLLAMA_MAX_LOADED_MODELS=1  OLLAMA_NUM_PARALLEL=1
                       OLLAMA_FLASH_ATTENTION=1  OLLAMA_KV_CACHE_TYPE=q8_0
legacy-whisperx        GPU_LOCK_FILE=/gpu-lock/gpu.lock
```

- Transcription loads nothing at start-up and unloads its model after ten idle minutes.
- Ollama keeps one model, serves one request at a time, and unloads after five minutes. Parallel
  requests do not help: when I tried three at once they simply took three times as long.
- The two services that run long batch jobs share a lock file on a mounted volume. The lock is
  an ordinary `flock`, taken around the one expensive call:

```python
def acquire_gpu_lock():
    lock_path = Path(os.environ.get("GPU_LOCK_FILE", "/gpu-lock/gpu.lock"))
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    handle = lock_path.open("a+")
    fcntl.flock(handle.fileno(), fcntl.LOCK_EX)   # blocks until the other job lets go
    return handle
```

A second job that wants the card waits on that line instead of loading its model next to the
first one's.

To see who holds the memory:

```bash
nvidia-smi --query-compute-apps=pid,used_memory,process_name --format=csv
```

On a container host the process name is not much use. The control group file tells you which
container a process belongs to:

```bash
cat /proc/<pid>/cgroup     # 0::/docker/<container id>
```

## Verify

This is not a staged test. I ran the commands on a Friday afternoon when I had not planned
anything, and it caught the sharing going wrong.

```
$ nvidia-smi --query-gpu=name,memory.total,memory.used,memory.free,utilization.gpu --format=csv
name, memory.total [MiB], memory.used [MiB], memory.free [MiB], utilization.gpu [%]
NVIDIA GeForce RTX 4060, 8188 MiB, 6602 MiB, 1332 MiB, 100 %

$ nvidia-smi --query-compute-apps=pid,used_memory,process_name --format=csv
pid, used_gpu_memory [MiB], process_name
3765283, 6232 MiB, python3
4079204, 360 MiB, /usr/lib/ollama/llama-server
```

Resolving the two processes through their control groups and command lines: the 6.2 GB holder is
`python3 ./ComfyUI/main.py --listen --port 8188`, inside the image-generation container, which
had been up for 58 minutes. The 360 MiB one is Ollama's runner. Ollama's own view of itself:

```
$ curl -s http://127.0.0.1:30068/api/ps    (name, size_vram, size)
qwen2.5vl:7b   0.19 of 7.03 GB on GPU
```

That is the failure. Ollama thinks it has a vision model loaded, and it has, but only 0.19 GB of
it is on the GPU. The other 6.8 GB is in system memory and every token is computed on the CPU. The
model is "resident", the service is "up", and the answer is several times slower than it should
be. Meanwhile the card reads 100 % utilisation, because the image pipeline is using all of it.

Sampling the card every five seconds shows the other half of it:

```
16:48:38  6602 MiB  100 %
16:48:43  6602 MiB  100 %
16:48:48  6602 MiB  100 %
16:48:53  6602 MiB  100 %
16:48:58  2154 MiB   78 %      <- the image job finished a render and released its memory
16:49:03  6538 MiB  100 %      <- the next render loaded it again
```

ComfyUI gives its memory back between renders and takes it again straight away. My reading, not something I captured: Ollama loaded
its model while the image job held most of the card, so it was placed mostly on the CPU, and it
keeps that placement until its five-minute timer unloads the model.

## Gotchas

- **`size_vram` is the number to watch, not the model list.** `size_vram` of zero, or far below
  `size`, means CPU. Nothing logs it as an error.
- **Placement is decided once, at load time.** Freeing memory afterwards does not move the
  model. It has to unload and load again.
- **Idle timeouts cannot save you from an active tenant.** They help only between jobs. The
  image pipeline is not idle, it is simply bursty, and the gaps are the dangerous part.
- **A lock only works between tenants that use it.** The `flock` covers the two batch services.
  Ollama and the image pipeline do not take it, which is exactly the pair that collided here.
  Giving every tenant the same lock, or having one queue in front of the card, is the next step.
- **Flash attention and a quantised KV cache** (`OLLAMA_FLASH_ATTENTION`, `OLLAMA_KV_CACHE_TYPE=q8_0`)
  shrink the context's memory so a 7B model has a better chance of fitting beside something else.
  They make the fit easier, not guaranteed.
- **The honest fix for many resident models is more memory.** For now the answer here is
  stricter queueing, not hardware.

## Further reading

- [Ollama FAQ](https://github.com/ollama/ollama/blob/main/docs/faq.md), for keep-alive and the
  loaded-model API.
- `man flock`, for the lock semantics.
