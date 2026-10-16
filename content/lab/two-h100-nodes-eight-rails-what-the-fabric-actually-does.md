---
title: "Two H100 nodes, eight rails: what the fabric actually does"
date: 2026-10-12
draft: false
tags: [infiniband, nccl, h100, hpc, networking]
summary: "A few hours on two rented 8-GPU InfiniBand nodes: 98.8% of line rate on every rail, then the same all_reduce on eight rails, one rail and plain TCP. The job completes correctly every time; over TCP it runs about 200 times slower."
---

*Part 2 of 2. [Part 1](/lab/an-infiniband-fabric-with-no-infiniband-hardware/) covers the
management plane on a simulated fabric. This part is the data plane on real hardware.*

## Problem

In part 1 I could cut a cable and watch a subnet manager reroute, but nothing moved any data.
On 12 October 2026 I rented two GPU VMs on one InfiniBand cluster to find out what a tenant
can see and measure from inside: each node has 8 H100 80GB GPUs and 8 ConnectX adapters at
400 Gb/s (NDR 4X), one "rail" per GPU. I wanted to know three things. Does each rail
deliver its line rate? How much of that survives a multi-node all_reduce? And what does it
look like when a rail, or the whole fabric, is not being used?

## Approach

Spot VMs from Nebius, Ubuntu 24.04, driver 570.211.01, CUDA 12.8, NCCL 2.26.2, HPC-X 2.26,
[nccl-tests](https://github.com/NVIDIA/nccl-tests) pinned to commit `afd59ab`. Three layers,
each checked before trusting the next:

1. `ib_write_bw` on each of the eight adapters, node0 to node1, one at a time.
2. nccl-tests `all_reduce_perf` on one node (8 GPUs) and on two (16 ranks over MPI).
3. The same two-node all_reduce with NCCL deliberately constrained: one adapter only
   (`NCCL_IB_HCA=mlx5_0`), then InfiniBand switched off.

Everything is `busbw` from nccl-tests, out-of-place, quoted with its message size. busbw is
a yardstick that makes different GPU counts comparable. It is not wire speed.

I also ran a ResNet-50 DDP job (synthetic data) on 1, 8 and 16 GPUs, which is the least
interesting result and is in the repo.

![What a tenant can see: each GPU's PCIe-local adapter, one rail each, and a switch layer that stays invisible](/img/lab/rail_topology.png)

## What I measured

Raw files and scripts are in [gpu-fleet-ops](https://github.com/joanmarcriera/gpu-fleet-ops/tree/main/results/2026-10-12-2x8xH100-ib);
every number below names its file in the table there.

**The links are healthy.** `ib_write_bw` (1 MiB, 4 queue pairs) gave 395.0 to 395.1 Gb/s on
all eight rails, 98.8% of 400 Gb/s
([`perftest/`](https://github.com/joanmarcriera/gpu-fleet-ops/tree/main/results/2026-10-12-2x8xH100-ib/perftest)).

![ib_write_bw per rail against the 400 Gb/s line rate](/img/lab/perftest_rails.png)

**At 8 GiB, the second node costs about 3%.** all_reduce busbw is 480.2 to 480.5 GB/s inside
one node (three runs) and 466.8 to 468.0 GB/s across two
([`nccl/41-*`, `42-*`](https://github.com/joanmarcriera/gpu-fleet-ops/tree/main/results/2026-10-12-2x8xH100-ib/nccl)).
At smaller sizes the gap widens: about 5% at 1 GiB and 8% at 256 MiB. And two nodes is the easy
case. 480 is above the roughly 450 GB/s per-direction NVLink 4 bandwidth that caps a ring's busbw
(a forced Ring here gives 368), so something else is helping.
Forcing the algorithm on one node shows what: NVLS (reduction inside the NVSwitch) 481.0,
Ring 368.4, Tree 298.1 GB/s. Across two nodes a forced Ring gave 332.1.

![all_reduce busbw at 8 GiB with NCCL_ALGO forced, against the NVLink 4 ring ceiling](/img/lab/algorithms.png)

**Breaking it.** Same two nodes, same binary, same correctness check (`#wrong` is 0 in every
run):

| Two nodes, all_reduce | Size | busbw | What NCCL reported |
|---|---|---|---|
| eight rails (default) | 1 GiB | 444 to 446 GB/s | `NET/SPCX_v10 ... GDRDMA` |
| one rail (`mlx5_0`) | 1 GiB | 91.5 GB/s | same plugin, one adapter |
| InfiniBand off | 256 MiB | 1.93 GB/s | `NET/Socket` over `eth0` |

![The same three configurations at one message size, 256 MiB: 388, 90 and 1.93 GB/s](/img/lab/degradation_ladder.png)

![all_reduce bus bandwidth against message size: one node, two nodes, one rail, TCP](/img/lab/busbw_vs_size.png)

The TCP row is at a smaller size than I would like, because that run used a shorter sweep (up to 256 MiB, fewer iterations); the healthy two-node figure at the same 256 MiB is 388 GB/s, so the gap is roughly
200 times. One rail leaves about a fifth of the healthy figure. Its algbw is 48.8 GB/s, close to
what a single 395 Gb/s adapter carries (49.4 GB/s). That fits an NVLS or Tree style algorithm,
which moves each byte across the node boundary about once per direction, with the cross-node
traffic of all 16 GPUs squeezed through one adapter. A ring would push nearly twice the data
through that adapter and land nearer 26 GB/s. I did not instrument which algorithm NCCL picked,
so read it as consistent with the explanation, not proof of it. The adapter also sits badly
for most GPUs: `mlx5_0` is on GPU4's PCIe switch and a socket hop (SYS) away from GPUs 0 to 3.

**Other collectives.** all_gather 318 GB/s busbw and all-to-all 72 GB/s on 16 GPUs at 4 GiB.
All-to-all is the weak one: NVLS does not help, and half of each GPU's data has to leave the
node. That is the pattern mixture-of-experts models put on a fabric.

## What broke and what that taught me

**A degraded fabric does not fail. It gets slower.** Every constrained run finished and passed
its correctness check. The TCP run exited 0; the one-rail run printed a correct table, then hit
the same teardown segfault as every default run (more on that below). For a tenant, "one adapter is down" or "someone left `NCCL_IB_DISABLE=1`
in the environment" looks like a training job that is simply slow. This is why a rail-optimised
design matters to the people renting it: each GPU has its own adapter on its own rail, the
loss of one rail is a visible, bounded loss, and the topology tells NCCL which adapter belongs
to which GPU. Here `nvidia-smi topo -m` showed GPU0 sharing a PCIe switch with `mlx5_4`, not
`mlx5_0`, so even the adapter numbering is not what you would assume.

**Read the transport line.** With `NCCL_DEBUG=INFO`, the line `via NET/...` says what
actually carried the traffic. `NET/Socket` means no InfiniBand, whatever the hardware has.
The cheapest check a tenant has is to grep for it before a long run.

**The default transport was not the stock one.** The multi-node default picked up the
NCCL Spectrum-X plugin that ships with HPC-X, through `LD_LIBRARY_PATH`. With
`NCCL_NET_PLUGIN=none` NCCL used its built-in `NET/IB`. Speed was the same within noise
(467.6 vs 468.9 GB/s median of three), but every default multi-node run ended with exit code
139, a segfault at teardown after the table had printed, and all three plugin-none runs
exited 0. I did not investigate the crash. It is the kind of thing that breaks a job
runner that trusts the exit code.

**Node 1 came up wrong twice.** First on a different image (driver 580, CUDA 13), then
not attached to the GPU cluster, then right. By my notes about an hour went on this. The first perftest
pass had run against a node that no longer existed, so I reran it and published only the
rerun. Compare driver, CUDA, NCCL and HPC-X on both nodes before any MPI run.

**The tenant view stops at the endpoint.** `sminfo`, `ibnetdiscover`, `iblinkinfo`,
`ibqueryerrors` and `ibdiagnet` could not open a management port inside the VM, and
`ibdiagnet` reported zero nodes. That is by design: `ibstat` reports CA type MT4126, a ConnectX
virtual function (SR-IOV), and a VF gets no subnet-management access. Everything here is endpoint-side. The error counters in
sysfs read zero since boot on node0, which is the only fabric-health evidence I have.

## What I did not test

- HPL, the OSU micro-benchmarks and nvbandwidth. Not run.
- GPU-memory perftest. The perftest build had no CUDA support, so the GPU-NIC locality
  difference (PIX against SYS) is untested.
- The switch side: topology, routing, adaptive routing, congestion. Blocked, see above.
- Failure injection beyond transport settings. One rail and TCP are NCCL settings, not a
  cable pull or a process kill, and the checkpoint and recovery study I planned for these
  nodes did not run.
- Statistics. At most three runs per configuration, one for forced algorithms, one rail,
  TCP, all_gather and all-to-all. No confidence intervals.
- The first perftest sweep failed with a remote access error just above 1 MiB. The rerun
  completed to 8 MiB. I did not chase the first failure.
- ResNet-50 on random tensors is a gentle load: about 100 MB of gradients per step. Scaling
  efficiency was 95.2% at 8 GPUs and 94.9% at 16, which says little about a large model. That
  job used the NCCL bundled with PyTorch (2.28.9), not the 2.26.2 above.

I ran this with Claude: I chose the setup and operated the VMs and first benchmarks, and
Claude read the nodes over SSH at my request, ran the later NCCL experiments from node0 and
wrote the training script. It once labelled a finished run as hung, which the raw file now
corrects.

## Further reading

- [gpu-fleet-ops](https://github.com/joanmarcriera/gpu-fleet-ops): the scrubbed raw output,
  the scripts, the plotting code and a summary with every caveat.
- [nccl-tests](https://github.com/NVIDIA/nccl-tests) and the NCCL documentation on
  `NCCL_ALGO`, `NCCL_IB_HCA` and `NCCL_NET_PLUGIN`.
- [Part 1](/lab/an-infiniband-fabric-with-no-infiniband-hardware/): the management plane
  on a simulated fabric.
