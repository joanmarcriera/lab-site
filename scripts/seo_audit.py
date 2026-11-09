#!/usr/bin/env python3
"""SEO audit over a built Hugo site (default: ./public). Report only, stdlib only.

Usage: python3 scripts/seo_audit.py [public_dir] [--base https://blog.riera.co.uk/]
Exit code 0 = no errors (warnings allowed), 1 = errors found.
"""
import json
import os
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict
from html.parser import HTMLParser
from urllib.parse import urlparse

TITLE_MIN, TITLE_MAX = 10, 70
DESC_MIN, DESC_MAX = 50, 160


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.lang = None
        self.titles = []
        self.metas = []  # (key, content)
        self.links = []  # (rel, href, hreflang)
        self.h1 = 0
        self.jsonld = []
        self._in_title = False
        self._in_ld = False
        self._buf = ""

    def handle_starttag(self, tag, attrs):
        a = {k.lower(): (v or "") for k, v in attrs}
        if tag == "html":
            self.lang = a.get("lang")
        elif tag == "title":
            self._in_title, self._buf = True, ""
        elif tag == "meta":
            key = a.get("name") or a.get("property") or a.get("http-equiv")
            if key:
                self.metas.append((key.lower(), a.get("content", "")))
        elif tag == "link":
            self.links.append((a.get("rel", "").lower(), a.get("href", ""), a.get("hreflang")))
        elif tag == "h1":
            self.h1 += 1
        elif tag == "script" and a.get("type") == "application/ld+json":
            self._in_ld, self._buf = True, ""

    def handle_endtag(self, tag):
        if tag == "title" and self._in_title:
            self.titles.append(self._buf.strip())
            self._in_title = False
        elif tag == "script" and self._in_ld:
            self.jsonld.append(self._buf)
            self._in_ld = False

    def handle_data(self, data):
        if self._in_title or self._in_ld:
            self._buf += data

    def meta(self, key):
        return [c for k, c in self.metas if k == key]


def main():
    args = sys.argv[1:]
    base = "https://blog.riera.co.uk/"
    if "--base" in args:
        i = args.index("--base")
        base = args[i + 1]
        del args[i:i + 2]
    root = os.path.abspath(args[0] if args else "public")
    host = urlparse(base).netloc
    errors, warnings = [], []

    def err(page, msg):
        errors.append(f"{page}: {msg}")

    def warn(page, msg):
        warnings.append(f"{page}: {msg}")

    def local_file(url):
        """Map an absolute site URL to a file under root, or None if off-site."""
        u = urlparse(url)
        if u.netloc != host:
            return None
        p = u.path.lstrip("/")
        if p == "" or p.endswith("/"):
            p += "index.html"
        return os.path.join(root, p)

    titles, descs = defaultdict(list), defaultdict(list)
    pages = 0
    for dirpath, _, files in os.walk(root):
        for f in files:
            if not f.endswith(".html"):
                continue
            path = os.path.join(dirpath, f)
            rel = os.path.relpath(path, root)
            with open(path, encoding="utf-8") as fh:
                html = fh.read()
            p = PageParser()
            p.feed(html)
            refresh = p.meta("refresh")
            if refresh:  # Hugo alias redirect page
                canon = [h for r, h, _ in p.links if r == "canonical"]
                if not canon:
                    err(rel, "alias page has no canonical")
                elif local_file(canon[0]) is None or not os.path.exists(local_file(canon[0])):
                    err(rel, f"alias target missing or off-host: {canon[0]}")
                if "noindex" not in " ".join(p.meta("robots")):
                    err(rel, "alias page is not noindex")
                continue
            pages += 1
            is404 = rel == "404.html"
            url = base + ("" if rel == "index.html" else rel[: -len("index.html")] if rel.endswith("index.html") else rel)

            if not p.lang:
                err(rel, "missing <html lang>")
            if len(p.titles) != 1:
                err(rel, f"{len(p.titles)} <title> elements")
            elif not TITLE_MIN <= len(p.titles[0]) <= TITLE_MAX:
                warn(rel, f"title length {len(p.titles[0])} (want {TITLE_MIN}-{TITLE_MAX}): {p.titles[0]!r}")
            if p.titles and not is404:
                titles[p.titles[0]].append(rel)
            d = p.meta("description")
            if len(d) != 1:
                err(rel, f"{len(d)} meta descriptions")
            else:
                if not d[0].strip():
                    err(rel, "empty meta description")
                elif not DESC_MIN <= len(d[0]) <= DESC_MAX:
                    warn(rel, f"description length {len(d[0])} (want {DESC_MIN}-{DESC_MAX})")
                if not is404:
                    descs[d[0]].append(rel)
            if p.h1 != 1:
                err(rel, f"{p.h1} <h1> elements")
            robots = " ".join(p.meta("robots")).lower()
            if is404:
                if "noindex" not in robots:
                    err(rel, "404 page should be noindex")
            elif "noindex" in robots:
                err(rel, "indexable page marked noindex")

            canon = [h for r, h, _ in p.links if r == "canonical"]
            if len(canon) != 1:
                err(rel, f"{len(canon)} canonical links")
            elif not is404:
                if urlparse(canon[0]).netloc != host:
                    err(rel, f"canonical on wrong host: {canon[0]}")
                elif canon[0] != url:
                    err(rel, f"canonical {canon[0]} != page URL {url}")
            for key in ("og:title", "og:description", "og:type", "og:url", "og:image",
                        "og:site_name", "twitter:card", "twitter:title",
                        "twitter:description", "twitter:image"):
                v = p.meta(key)
                if len(v) != 1 or not v[0].strip():
                    err(rel, f"{len(v)} non-empty {key} tags (want 1)")
            for key in ("og:image", "twitter:image"):
                for v in p.meta(key):
                    lf = local_file(v)
                    if lf is None:
                        if not v.startswith("https://"):
                            err(rel, f"{key} not absolute https: {v}")
                    elif not os.path.isfile(lf):
                        err(rel, f"{key} file missing: {v}")
            hl = [h for _, _, h in p.links if h]
            if hl:
                err(rel, "hreflang present on a monolingual site")
            for block in p.jsonld:
                try:
                    data = json.loads(block)
                except ValueError as e:
                    err(rel, f"invalid JSON-LD: {e}")
                    continue
                for node in data.get("@graph", [data]):
                    if "@type" not in node:
                        err(rel, "JSON-LD node without @type")
            if not p.jsonld and not is404:
                warn(rel, "no JSON-LD")

    for t, rels in titles.items():
        if len(rels) > 1:
            err(", ".join(sorted(rels)), f"duplicate title {t!r}")
    for d, rels in descs.items():
        if len(rels) > 1:
            warn(", ".join(sorted(rels)[:5]) + (" ..." if len(rels) > 5 else ""),
                 f"description shared by {len(rels)} pages")

    if not os.path.isfile(os.path.join(root, "404.html")):
        err("404.html", "missing")

    rpath = os.path.join(root, "robots.txt")
    if not os.path.isfile(rpath):
        err("robots.txt", "missing")
    else:
        txt = open(rpath, encoding="utf-8").read()
        if f"Sitemap: {base}sitemap.xml" not in txt:
            err("robots.txt", f"no 'Sitemap: {base}sitemap.xml' line")
        lines = [ln.strip().lower() for ln in txt.splitlines()]
        if "disallow: /" in lines:
            err("robots.txt", "disallows the whole site")

    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    try:
        sm = ET.parse(os.path.join(root, "sitemap.xml"))
        locs = [e.text for e in sm.getroot().findall("s:url/s:loc", ns)]
        if not locs:
            err("sitemap.xml", "no URLs")
        for loc in locs:
            lf = local_file(loc)
            if lf is None:
                err("sitemap.xml", f"URL on wrong host: {loc}")
            elif not os.path.isfile(lf):
                err("sitemap.xml", f"URL has no page: {loc}")
            elif not urlparse(loc).path.endswith("/"):
                warn("sitemap.xml", f"URL without trailing slash: {loc}")
    except (OSError, ET.ParseError) as e:
        err("sitemap.xml", f"unreadable: {e}")

    try:
        rss = ET.parse(os.path.join(root, "index.xml")).getroot()
        ch = rss.find("channel")
        if rss.tag != "rss" or ch is None:
            err("index.xml", "not an RSS 2.0 document")
        else:
            for t in ("title", "link", "description"):
                if not (ch.findtext(t) or "").strip():
                    err("index.xml", f"channel missing <{t}>")
            for it in ch.findall("item"):
                link = it.findtext("link") or ""
                if urlparse(link).netloc != host:
                    err("index.xml", f"item link on wrong host: {link}")
                if not (it.findtext("title") or "").strip():
                    err("index.xml", f"item without title: {link}")
    except (OSError, ET.ParseError) as e:
        err("index.xml", f"invalid RSS: {e}")

    for w in warnings:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    print(f"\n{pages} pages audited: {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
