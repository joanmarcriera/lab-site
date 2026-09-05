# CLAUDE.md — lab-site

**Purpose**: Hugo static blog at blog.riera.co.uk — Marc's personal technology leadership and
self-hosted infrastructure journal. Two published sections (field-notes, leadership) + drafts pipeline.

## Quick start

```bash
# Install Hugo (v0.147.2) — check Homebrew or https://gohugo.io/installation/
hugo version

# Local preview
hugo server -D  # -D includes drafts; navigate to http://localhost:1313

# Build for production
hugo --minify  # outputs to ./public

# Push to publish
git push origin main  # GitHub Actions runs gitleaks → Hugo build → Pages deploy
```

## Layout & conventions

**Content structure** (all Markdown):
- `content/field-notes/` — 2016–2026 infrastructure career stories (framed in `_index.md`
  as former-employer retrospectives; see `content/disclaimer.md` for AI disclosure)
- `content/leadership/` — CTO programme, finance, ITIL knowledge base
- `content/disclaimer.md` — employment/AI transparency statement
- `drafts/` — unpublished posts (Hugo ignores this dir; each file has `draft: true` YAML as backup)

**Front matter** (YAML per post):
```yaml
title: "Post Title"
date: 2026-09-05
draft: false  # true = excluded from build
tags: [tag1, tag2]
```

**Themes & CSS**: One custom stylesheet (`static/css/lab-site.css`) — no external theme.
Dark mode via `@media (prefers-color-scheme: dark)`. OpenGraph cards use `static/img/card.png`.

**Deployment**: `.github/workflows/hugo.yml` runs gitleaks on full history (secret scan),
then Hugo minify, then GitHub Pages. No other environments.

## How to work here

1. **Draft posts**: Add `.md` files to `drafts/` with `draft: true`. Run `hugo server -D`,
   edit Markdown in place (Hugo reloads on save). No commit needed yet.
2. **Review & gate**: Check `content/disclaimer.md` for the employer/secret checklist
   (no formal doc, embedded in disclaimer + prior commits 28b515a / 6f35a4c).
   Grep post for `employer|token|api_key|secret`.
3. **Publish**: Move file to `content/<section>/`, set `draft: false`, push to main.
   GitHub Actions auto-deploys within 2–3 min.
4. **Tags & series**: Taxonomy is `tag`; use `tags: [tag1, tag2]` in front matter.
   No auto-generated series (manual link structure in post body).

## Gotchas & conventions

- **No publish-date display**: Dates are in front matter but not shown on live site
  (removed ~commit fc3faf1 for "Lab Notes" feel). Check front matter to see publication order.
- **Gitleaks gates the build**: CI fails on ANY secret pattern match. Drafts under `drafts/`
  are scanned too, so even unpublished posts must pass gitleaks.
- **Hugo version pinned**: `0.147.2` in `.github/workflows/hugo.yml`; use `hugo version`
  locally to verify match.
- **CNAME for custom domain**: `static/CNAME` points to blog.riera.co.uk; Pages auto-reads it.
- **No draft section**: Unlike WordPress, Hugo drafts are not built at all. Use `drafts/` dir
  + `draft: true` as a two-layer guard.
- **Not in Vikunja**: blog/lab-site work is ad hoc; no standing Vikunja project yet
  (see HANDOFF-2026-09-05.md for context). If posting becomes a cadence, create a small
  `empresa/projecte` child project to track draft → review → publish pipeline.

## Recipes

**Add a new post**:
```bash
# Draft mode
cat > drafts/my-post-title.md << 'EOF'
---
title: "My Post Title"
date: 2026-09-06
draft: true
tags: [tag1]
---

Content in Markdown.
EOF

hugo server -D  # Preview at localhost:1313

# When ready to publish
mv drafts/my-post-title.md content/field-notes/  # or content/leadership/
# Edit front matter: set draft: false
git add content/field-notes/my-post-title.md
git commit -m "content(field-notes): add my post title"
git push origin main
```

**Check for secrets before committing**:
```bash
gitleaks detect --source . --verbose  # Local gitleaks (if installed)
# OR: rely on CI, which will fail the build
```

**Test build locally**:
```bash
hugo --minify
ls -l public/  # Verify output
```
