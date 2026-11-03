#!/usr/bin/env python3
"""Guard the site's redirect aliases (stdlib only).

Usage:
    python3 tools/check_aliases.py [--root DIR] [--manifest FILE]
    python3 tools/check_aliases.py --update      # rewrite the manifest

Reads the front matter (YAML `---` or TOML `+++`) of every .md file under
<root>/content, collects `aliases`, normalises each to `/path/`, and fails
(exit 1, one line per problem: file and alias) when:
  (a) an alias is declared twice (same or different files);
  (b) an alias equals another page's own URL (an alias equal to the
      declaring page's own URL is only noted as redundant);
  (c) an alias listed in the manifest (tests/aliases.expected.txt) is no
      longer produced by any page -- a rename or deletion that would break
      an inbound redirect (see CLAUDE.md).
New aliases not yet in the manifest are reported but do not fail; run
--update to record them.

Page URL derivation (best effort, for check b): an explicit `url` wins;
otherwise /<dir>/<slug or file name>/, with `_index.md` and `index.md`
mapping to their directory, and the `archive` permalink rule from hugo.toml
(/archive/:year/:contentbasename/, year from `date`). Not covered: other
[permalinks] rules, translations, and `slug` on section pages.
"""
import argparse
import re
import sys
from pathlib import Path

ARCHIVE_SECTION = "archive"


def norm(path):
    path = "/" + path.strip().strip("/")
    return path if path == "/" else path + "/"


def front_matter(text):
    """Return (format, body) of the front matter block, or (None, '')."""
    for fence, fmt in (("---", "yaml"), ("+++", "toml")):
        if text.startswith(fence + "\n"):
            end = text.find("\n" + fence, len(fence))
            if end != -1:
                return fmt, text[len(fence) + 1:end]
    return None, ""


def _unquote(value):
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def _inline_list(value):
    inner = value.strip()[1:-1]
    return [_unquote(v) for v in inner.split(",") if v.strip()]


def parse(text):
    """Extract aliases, url, slug and date from YAML or TOML front matter."""
    fmt, body = front_matter(text)
    sep = ":" if fmt == "yaml" else "="
    data = {"aliases": []}
    lines = body.splitlines()
    i = 0
    while i < len(lines):
        m = re.match(r"^(aliases|url|slug|date)\s*" + sep + r"\s*(.*)$", lines[i])
        i += 1
        if not m:
            continue
        key, value = m.group(1), m.group(2).strip()
        if key != "aliases":
            data[key] = _unquote(value)
        elif value.startswith("["):
            while not value.rstrip().endswith("]") and i < len(lines):
                value += lines[i]
                i += 1
            data["aliases"] = _inline_list(value)
        elif value:
            data["aliases"] = [_unquote(value)]
        else:  # YAML block list
            while i < len(lines) and re.match(r"^\s*-\s+", lines[i]):
                data["aliases"].append(_unquote(lines[i].split("-", 1)[1]))
                i += 1
    return data


def page_url(rel, meta):
    """Best-effort URL Hugo gives the page at content-relative path `rel`."""
    if meta.get("url"):
        return norm(meta["url"])
    parts = list(rel.parts)
    name = Path(parts.pop()).stem
    if name in ("_index", "index"):
        return norm("/".join(parts))
    slug = meta.get("slug") or name
    if parts and parts[0] == ARCHIVE_SECTION and meta.get("date", "")[:4].isdigit():
        return norm("%s/%s/%s" % (ARCHIVE_SECTION, meta["date"][:4], name))
    return norm("/".join(parts + [slug]))


def collect(content_dir):
    """Return ({alias: [files]}, {url: file})."""
    aliases, urls = {}, {}
    for path in sorted(content_dir.rglob("*.md")):
        rel = path.relative_to(content_dir)
        meta = parse(path.read_text(encoding="utf-8"))
        urls[page_url(rel, meta)] = str(rel)
        for alias in meta["aliases"]:
            aliases.setdefault(norm(alias), []).append(str(rel))
    return aliases, urls


def check(root, manifest):
    aliases, urls = collect(root / "content")
    errors, notes = [], []
    for alias, files in sorted(aliases.items()):
        if len(files) > 1:
            errors.append("duplicate alias %s in %s" % (alias, ", ".join(files)))
        if alias in urls and urls[alias] in files:
            notes.append("alias %s in %s is the page's own URL (redundant)"
                         % (alias, urls[alias]))
        elif alias in urls:
            errors.append("alias %s in %s collides with the URL of %s"
                          % (alias, files[0], urls[alias]))
    expected = read_manifest(manifest)
    for alias in sorted(expected - set(aliases)):
        errors.append("alias %s from %s is no longer produced by any page "
                      "(renamed/deleted? inbound redirect breaks)" % (alias, manifest.name))
    notes += ["new alias %s not in manifest (run --update)" % a
              for a in sorted(set(aliases) - expected)]
    return errors, notes, aliases


def read_manifest(manifest):
    if not manifest.exists():
        return set()
    return {norm(l) for l in manifest.read_text(encoding="utf-8").splitlines()
            if l.strip() and not l.startswith("#")}


def write_manifest(manifest, aliases):
    manifest.parent.mkdir(parents=True, exist_ok=True)
    body = "# Generated by tools/check_aliases.py --update. One alias per line.\n"
    manifest.write_text(body + "".join(a + "\n" for a in sorted(aliases)), encoding="utf-8")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--root", default=Path(__file__).resolve().parent.parent, type=Path)
    ap.add_argument("--manifest", type=Path, help="default: <root>/tests/aliases.expected.txt")
    ap.add_argument("--update", action="store_true", help="rewrite the manifest from the tree")
    args = ap.parse_args(argv)
    manifest = args.manifest or args.root / "tests" / "aliases.expected.txt"
    if args.update:
        aliases, _ = collect(args.root / "content")
        write_manifest(manifest, aliases)
        print("wrote %d aliases to %s" % (len(aliases), manifest))
        return 0
    errors, notes, aliases = check(args.root, manifest)
    for note in notes:
        print("note: " + note)
    for err in errors:
        print("ERROR: " + err, file=sys.stderr)
    print("%d aliases checked, %d errors" % (len(aliases), len(errors)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
