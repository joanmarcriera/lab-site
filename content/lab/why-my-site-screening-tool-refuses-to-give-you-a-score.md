---
title: "Why my site-screening tool refuses to give you a score"
date: 2026-09-03
tags: [geospatial, ai-infrastructure, evidence]
draft: false
---

Screening a site for something like an AI data centre means pulling together grid capacity,
water availability, fibre routes, flood risk, and planning status — data that lives in half a
dozen different formats, from half a dozen different authorities, updated on half a dozen
different schedules. The normal way to make that digestible is to roll it into a single score:
green light, amber light, a number out of ten. I built a private, self-hosted service to do this
kind of screening properly, and the decision I keep coming back to is that it deliberately does
not do that.

The reasoning is simple once you say it out loud: a composite score built from uncalibrated
weights isn't a measurement, it's an opinion wearing a measurement's clothes. If I don't yet know
whether grid headroom should count for twice as much as flood risk, forcing them into one number
doesn't resolve that uncertainty — it just hides it behind a decimal point that looks more
confident than anything underneath it deserves. So the first vertical slice returns raw
measurements and an explicit pass/fail/unknown per constraint, and "unknown" is a first-class
answer, never quietly coerced to zero or to a pass. A screening tool's most useful sentence is
often "we don't have good evidence for this yet," and a single score can't say that.

A few other decisions came out of the same instinct:

- **Keep the deterministic core separate from QGIS.** The calculation API is plain Python with
  deterministic tests; QGIS runs as a serial batch worker for validation and export only, never
  embedded per-request. That trade costs some latency but buys a runtime I can actually test and
  fail predictably, instead of inheriting whatever thread-safety and plugin behaviour QGIS brings
  with it.
- **Publish packages transactionally.** Every output format — JSON, GeoPackage, PDF report, QGIS
  project — gets built into a staging directory and only swapped into place once *all* of them
  succeed. A failed PDF export must never leave behind a directory that looks complete but isn't;
  the previous good package stays live until the new one fully lands.
- **Quarantine anything pulled from a public catalogue.** Community GIS resources can save real
  time, but they're neither an authoritative data source nor a trusted software supply chain. So
  external assets go through an explicit allowlist by ID, get audited as static content, and are
  never auto-executed — a small amount of friction in exchange for not silently running someone
  else's script against my data.
- **Defer the database.** GeoParquet, GeoPackage and a file-based columnar engine cover a
  single-user, single-machine workload just fine for now. I'm not standing up PostGIS until a
  real requirement — concurrent editing, or searches slow enough to matter — actually shows up.

**What I'd do differently:** the honest answer is nothing about the no-score decision — it's the
one part of this I'm most confident is right, and I expect it to look more right, not less, as
real candidate sites get run through it. If anything I'd have written the evidence-grading rules
(source, date, method, coverage, freshness) on day one instead of adding them once the shape of
the API was already settled; retrofitting provenance onto data structures that weren't built to
carry it is more awkward than designing it in from the start.

## Sources

- [GeoParquet](https://geoparquet.org/)
- [QGIS](https://qgis.org/)
- [DuckDB spatial extension](https://duckdb.org/docs/extensions/spatial)
