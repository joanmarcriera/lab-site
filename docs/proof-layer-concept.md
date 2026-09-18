<!-- Merged 2026-09-18 from the separate local-ai-lab repo, which contained only this
     README plus five empty .gitkeep directories — no artefacts were ever added.
     The public repos (GitHub joanmarcriera/local-ai-lab, Forgejo marc/local-ai-lab)
     still exist and are untouched; refill them if the proof-layer idea is revived. -->

# Local-AI Automation Lab

I lead high-performance technical teams and run the infrastructure to prove it —
self-hosted, AI-assisted, no hype, just things that work.

This is the **proof layer** for my content: every post I publish points at a folder
here with the actual artefacts — n8n workflows, prompts, Dockerfiles, benchmark
notes, and honest failure logs. Built on my own hardware (TrueNAS + RTX 4060,
Mac M5, two OptiPlexes), orchestrated by n8n, drafted by local Ollama models.

## Structure
- `posts/` — one folder per published post: README, workflow JSON, prompts, configs
- `learning-log/` — daily learning notes (leadership + platform engineering)
- `templates/` — reusable n8n workflows and pipeline stages, promoted from posts/
- `docker/` — container definitions for the GPU render pipeline
- `docs/` — architecture, licences, decisions

## The pipeline that publishes this repo
Sources (course notes, saved links) → local LLM drafting → quality gate →
confidentiality scrubber → **human approval** → multi-platform publish + this repo.
Engagement is never automated; every post is approved by me.

*AI-assisted content, my real face and words. Everything here runs locally unless
explicitly noted.*
