# Lab Notes — blog.riera.co.uk

Hugo source for **[blog.riera.co.uk](https://blog.riera.co.uk)** — technology leadership and
self-hosted AI infrastructure. No hype, just things that work.

## How it works

- Static site built with [Hugo](https://gohugo.io/); config in `hugo.toml`, posts in `content/`.
- Deployed to GitHub Pages by `.github/workflows/hugo.yml` on every push to `main`.

## Writing a post

Add a Markdown file under `content/posts/` with front matter, push to `main`, done.
