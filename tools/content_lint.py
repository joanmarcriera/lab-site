#!/usr/bin/env python3
"""Content lint for the lab-site Hugo source (stdlib only).

Usage:
    python3 tools/content_lint.py [--root DIR] [--fix-alt] [--allow-missing-summary]

Checks every Markdown file under <root>/content/:
  1. Front matter: `title`, ISO `date`, boolean `draft` on every page
     (section `_index.md` pages need only `title`); a `summary` on the
     children of lab/, field-notes/, leadership/ and work/; `post_lang`
     (en|es|ca) and `original_url` on archive posts.
  2. Internal links: every `/path/` or relative Markdown link resolves to a
     page, section, alias, tag page or file under static/. Archive posts live
     at /archive/<year>/<file-name>/, the year taken from the front-matter date.
  3. Images: every `![alt](src)` and `<img>` has descriptive alt text, and a
     local src exists under static/.

Exits 1 if any error is found, 0 otherwise.
--fix-alt is a dry run: it prints the alt text it would suggest for images
without one (from the file name, with the preceding paragraph as context)
and changes nothing.
--allow-missing-summary reports a missing `summary` as a warning, not an error.
"""

import argparse
import datetime
import os
import re
import sys

SUMMARY_SECTIONS = {"lab", "field-notes", "leadership", "work"}
LANGS = {"en", "es", "ca"}
GENERIC_ALT = {"image", "img", "picture", "photo", "screenshot", "figure", "alt"}

LINK_RE = re.compile(r'(!?)\[([^\]]*)\]\(\s*<?([^)\s>]+)>?(?:\s+"[^"]*")?\s*\)')
REF_RE = re.compile(r'^\s{0,3}\[[^\]]+\]:\s*<?(\S+?)>?(?:\s+"[^"]*")?\s*$')
IMG_TAG_RE = re.compile(r'<img\b[^>]*>', re.I)
ATTR_RE = re.compile(r'(\w+)\s*=\s*("([^"]*)"|\'([^\']*)\'|(\S+))')
DATE_RE = re.compile(r'^\d{4}-\d{2}-\d{2}([T ]\d{2}:\d{2}(:\d{2})?(Z|[+-]\d{2}:\d{2})?)?$')
EXTERNAL = re.compile(r'^([a-z][a-z0-9+.-]*:|//|#)', re.I)


def parse_front_matter(text):
    """Return (dict of top-level YAML keys -> raw string, body, body_offset_lines) or (None, text, 0)."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return None, text, 0
    fm = {}
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return fm, "\n".join(lines[i + 1:]), i + 1
        m = re.match(r'^([A-Za-z_][\w-]*):\s*(.*)$', line)
        if m:
            fm[m.group(1)] = unquote(m.group(2).strip())
    return None, text, 0


def unquote(v):
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        return v[1:-1]
    return v


def parse_list(v):
    v = v.strip()
    if v.startswith("[") and v.endswith("]"):
        return [unquote(x.strip()) for x in v[1:-1].split(",") if x.strip()]
    return []


def strip_code(body):
    """Blank out fenced code blocks and inline code, keeping line numbers."""
    out, fence = [], None
    for line in body.split("\n"):
        m = re.match(r'^\s*(```|~~~)', line)
        if fence:
            out.append("")
            if m and m.group(1) == fence:
                fence = None
            continue
        if m:
            fence = m.group(1)
            out.append("")
            continue
        out.append(re.sub(r'`[^`]*`', '', line))
    return out


class Page:
    def __init__(self, root, path):
        self.path = path
        self.rel = os.path.relpath(path, os.path.join(root, "content")).replace(os.sep, "/")
        with open(path, encoding="utf-8") as f:
            self.text = f.read()
        self.fm, self.body, self.offset = parse_front_matter(self.text)
        parts = self.rel.split("/")
        self.section = parts[0] if len(parts) > 1 else ""
        self.base = os.path.splitext(parts[-1])[0]
        self.is_index = self.base == "_index"

    def year(self):
        d = (self.fm or {}).get("date", "")
        return d[:4] if DATE_RE.match(d) else None

    def url(self):
        fm = self.fm or {}
        if fm.get("url"):
            return norm(fm["url"])
        dirpath = os.path.dirname(self.rel)
        if self.is_index:
            return norm("/" + dirpath + "/") if dirpath else "/"
        slug = fm.get("slug") or self.base
        if self.section == "archive":
            return norm("/archive/%s/%s/" % (self.year() or "0000", self.base))
        return norm("/" + (dirpath + "/" if dirpath else "") + slug + "/")


def norm(p):
    p = p.split("#")[0].split("?")[0]
    if not p.startswith("/"):
        p = "/" + p
    p = re.sub(r'/+', '/', p)
    if not os.path.splitext(p)[1] and not p.endswith("/"):
        p += "/"
    return p


def load(root):
    pages = []
    for d, _, files in os.walk(os.path.join(root, "content")):
        for name in sorted(files):
            if name.endswith(".md"):
                pages.append(Page(root, os.path.join(d, name)))
    pages.sort(key=lambda p: p.rel)
    return pages


def known_urls(pages):
    urls = {"/", "/tags/"}
    for p in pages:
        urls.add(p.url())
        fm = p.fm or {}
        for a in parse_list(fm.get("aliases", "")):
            urls.add(norm(a))
        for t in parse_list(fm.get("tags", "")):
            urls.add(norm("/tags/" + re.sub(r'\s+', '-', t.lower()) + "/"))
    return urls


def check_front_matter(p, report, allow_missing_summary):
    if p.fm is None:
        report.error(p, 1, "front-matter", "no YAML front matter")
        return
    fm = p.fm
    if not fm.get("title"):
        report.error(p, 1, "front-matter", "missing title")
    if p.is_index:
        return
    if "date" not in fm:
        report.error(p, 1, "front-matter", "missing date")
    elif not valid_date(fm["date"]):
        report.error(p, 1, "front-matter", "malformed date %r" % fm["date"])
    if "draft" not in fm:
        report.error(p, 1, "front-matter", "missing draft")
    elif fm["draft"] not in ("true", "false"):
        report.error(p, 1, "front-matter", "draft is not a boolean: %r" % fm["draft"])
    if p.section in SUMMARY_SECTIONS and not fm.get("summary"):
        if allow_missing_summary:
            report.warn(p, 1, "front-matter", "missing summary")
        else:
            report.error(p, 1, "front-matter", "missing summary")
    if p.section == "archive":
        if fm.get("post_lang") not in LANGS:
            report.error(p, 1, "front-matter", "post_lang missing or not en|es|ca: %r" % fm.get("post_lang"))
        if not fm.get("original_url"):
            report.error(p, 1, "front-matter", "missing original_url")


def valid_date(d):
    if not DATE_RE.match(d):
        return False
    try:
        datetime.date.fromisoformat(d[:10])
    except ValueError:
        return False
    return True


def resolve(p, target):
    """Turn a link target into a site path, relative links taken from the page URL."""
    if target.startswith("/"):
        return norm(target)
    base = p.url()
    return norm(os.path.normpath(os.path.join(base, target.split("#")[0])).replace(os.sep, "/"))


def exists(root, urls, path):
    if path in urls:
        return True
    return os.path.isfile(os.path.join(root, "static", path.lstrip("/")))


def describe_alt(src, context):
    name = os.path.splitext(os.path.basename(src))[0]
    words = re.sub(r'[-_]+', ' ', name).strip()
    hint = context.strip().split(". ")[0][:120] if context.strip() else ""
    return words[:1].upper() + words[1:], hint


def check_body(root, p, urls, report, fix_alt):
    lines = strip_code(p.body)
    for i, line in enumerate(lines):
        lineno = p.offset + i + 1
        targets = []
        for m in LINK_RE.finditer(line):
            is_img, text, target = m.group(1) == "!", m.group(2), m.group(3)
            targets.append((target, is_img))
            if is_img:
                check_alt(p, lineno, text, target, lines, i, report, fix_alt)
        m = REF_RE.match(line)
        if m:
            targets.append((m.group(1), False))
        for tag in IMG_TAG_RE.findall(line):
            attrs = {a.group(1).lower(): next(g for g in a.groups()[2:] if g is not None)
                     for a in ATTR_RE.finditer(tag)}
            src = attrs.get("src", "")
            check_alt(p, lineno, attrs.get("alt"), src, lines, i, report, fix_alt, tag=True)
            if src:
                targets.append((src, True))
        for target, is_img in targets:
            if EXTERNAL.match(target):
                continue
            path = resolve(p, target)
            if not exists(root, urls, path):
                kind = "image" if is_img else "link"
                report.error(p, lineno, kind, "%s does not resolve (%s)" % (target, path))


def check_alt(p, lineno, alt, src, lines, i, report, fix_alt, tag=False):
    if alt is None:
        problem = "<img> without alt attribute"
    elif not alt.strip():
        problem = "empty alt text"
    elif alt.strip().lower() in GENERIC_ALT or alt.strip() == os.path.basename(src):
        problem = "non-descriptive alt text %r" % alt
    else:
        return
    report.error(p, lineno, "alt", "%s for %s" % (problem, src))
    if fix_alt:
        context = ""
        for j in range(i - 1, -1, -1):
            if lines[j].strip():
                context = lines[j]
                break
        suggestion, hint = describe_alt(src, context)
        print("  would set alt for %s:%d to %r (context: %r)" % (p.rel, lineno, suggestion, hint))


class Report:
    def __init__(self):
        self.errors, self.warnings = [], []

    def error(self, p, line, rule, msg):
        self.errors.append((p.rel, line, rule, msg))

    def warn(self, p, line, rule, msg):
        self.warnings.append((p.rel, line, rule, msg))


def run(root, fix_alt=False, allow_missing_summary=False, out=None):
    out = out or sys.stdout
    pages = load(root)
    urls = known_urls(pages)
    report = Report()
    for p in pages:
        check_front_matter(p, report, allow_missing_summary)
        check_body(root, p, urls, report, fix_alt)
    for level, items in (("ERROR", report.errors), ("WARN", report.warnings)):
        for rel, line, rule, msg in items:
            print("%s content/%s:%d [%s] %s" % (level, rel, line, rule, msg), file=out)
    counts = {}
    for _, _, rule, _ in report.errors:
        counts[rule] = counts.get(rule, 0) + 1
    print("pages checked: %d; errors: %d %s; warnings: %d" % (
        len(pages), len(report.errors), counts or "", len(report.warnings)), file=out)
    return report


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--root", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
    ap.add_argument("--fix-alt", action="store_true", help="dry run: print suggested alt text")
    ap.add_argument("--allow-missing-summary", action="store_true",
                    help="report a missing summary as a warning, not an error")
    args = ap.parse_args(argv)
    report = run(os.path.abspath(args.root), args.fix_alt, args.allow_missing_summary)
    return 1 if report.errors else 0


if __name__ == "__main__":
    sys.exit(main())
