# Lab Notes — blog.riera.co.uk

Hugo source for **[blog.riera.co.uk](https://blog.riera.co.uk)** — technology leadership and
self-hosted AI infrastructure. No hype, just things that work.

## How it works

- Static site built with [Hugo](https://gohugo.io/); config in `hugo.toml`, posts in `content/`.
- Deployed to GitHub Pages by `.github/workflows/hugo.yml` on every push to `main`.

## Quick start

```bash
# Install Hugo (v0.147.2 required)
hugo version

# Local preview
hugo server -D  # includes drafts; http://localhost:1313

# Build for production
hugo --minify  # outputs to ./public
```

## Writing a post

1. Create a draft under `drafts/my-post.md` with `draft: true` front matter
2. Run `hugo server -D` to preview locally
3. When ready, move to `content/field-notes/` or `content/leadership/`, set `draft: false`
4. Commit and push to `main` — GitHub Actions auto-builds and deploys via GitHub Pages

Posts must pass gitleaks scanning (no secrets in the content or git history).
