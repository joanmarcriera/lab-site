# Lab Notes — blog.riera.co.uk

Hugo source for **[blog.riera.co.uk](https://blog.riera.co.uk)** — hands-on infrastructure
engineering: HPC, storage, Linux and self-hosted AI. A work catalogue (`content/work/`), current
build logs (`content/lab/`), the recovered 2009–2014 blog (`content/archive/`), field notes and
leadership.

## How it works

- Static site built with [Hugo](https://gohugo.io/); config in `hugo.toml`, posts in `content/`.
- Deployed to GitHub Pages by `.github/workflows/hugo.yml` on every push to `main`.

## Quick start

```bash
# Hugo v0.147.2 is required (pinned in CI); keep that binary in .bin/hugo — see CLAUDE.md
.bin/hugo version

# Local preview
hugo server -D  # includes drafts; http://localhost:1313

# Build for production
hugo --minify  # outputs to ./public
```

## Writing a post

1. Create a draft under `drafts/my-post.md` with `draft: true` front matter
2. Run `hugo server -D` to preview locally
3. When ready, move to `content/lab/`, `content/field-notes/` or `content/leadership/`, set `draft: false`
4. Commit and push to `main` — GitHub Actions auto-builds and deploys via GitHub Pages

Posts must pass gitleaks scanning (no secrets in the content or git history).

<!-- vikunja-tracking -->
## Tracking

Vikunja project **66 · Lab Notes blog** — https://familia.riera.co.uk/projects/66
