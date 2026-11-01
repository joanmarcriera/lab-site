"""Tests for tools/content_lint.py. Run: python3 -m unittest discover -s tests"""

import io
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stdout

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
import content_lint  # noqa: E402

GOOD_LAB = '---\ntitle: "A"\ndate: 2026-10-09\ndraft: false\nsummary: "S"\n---\n'
GOOD_ARCHIVE = ('---\ntitle: "B"\ndate: 2014-03-01\ndraft: false\npost_lang: en\n'
                'original_url: http://example.org/b/\n---\n')


class LintTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = self.tmp.name
        self.write("content/lab/_index.md", '---\ntitle: "Lab"\n---\n')
        self.write("content/archive/b.md", GOOD_ARCHIVE + "Body.\n")
        self.write("static/img/lab/x.png", "")

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, rel, text):
        path = os.path.join(self.root, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)

    def main(self):
        with redirect_stdout(io.StringIO()):
            return content_lint.main(["--root", self.root])

    def lint(self, **kw):
        out = io.StringIO()
        with redirect_stdout(out):
            report = content_lint.run(self.root, out=out, **kw)
        self.output = out.getvalue()
        return [m for _, _, _, m in report.errors]

    def test_clean_tree_passes(self):
        self.write("content/lab/a.md", GOOD_LAB + "See [b](/archive/2014/b/) and ![A chart](/img/lab/x.png).\n")
        self.assertEqual(self.lint(), [])
        self.assertEqual(self.main(), 0)

    def test_missing_fields(self):
        self.write("content/lab/a.md", '---\ntitle: "A"\n---\n')
        errors = self.lint()
        for want in ("missing date", "missing draft", "missing summary"):
            self.assertIn(want, errors)
        self.assertEqual(self.main(), 1)

    def test_missing_summary_can_be_a_warning(self):
        self.write("content/lab/a.md", '---\ntitle: "A"\ndate: 2026-01-01\ndraft: false\n---\n')
        self.assertEqual(self.lint(allow_missing_summary=True), [])
        self.assertIn("WARN", self.output)

    def test_section_index_needs_only_title(self):
        self.assertEqual(self.lint(), [])

    def test_malformed_date_and_draft(self):
        self.write("content/lab/a.md", GOOD_LAB.replace("2026-10-09", "2026-13-09")
                   .replace("draft: false", "draft: no"))
        errors = self.lint()
        self.assertTrue(any("malformed date" in e for e in errors))
        self.assertTrue(any("not a boolean" in e for e in errors))

    def test_no_front_matter(self):
        self.write("content/about.md", "Just text.\n")
        self.assertIn("no YAML front matter", self.lint())

    def test_archive_fields(self):
        self.write("content/archive/c.md", '---\ntitle: "C"\ndate: 2010-01-01\ndraft: false\npost_lang: fr\n---\n')
        errors = self.lint()
        self.assertTrue(any("post_lang" in e for e in errors))
        self.assertIn("missing original_url", errors)

    def test_broken_links(self):
        self.write("content/lab/a.md", GOOD_LAB +
                   "[wrong year](/archive/2013/b/) [typo](/lab/aa/) [rel](../nope/)\n"
                   "[ok rel](../) [ext](https://example.org/x) [anchor](#top)\n"
                   "```\n[in code](/not/checked/)\n```\n[ref]: /missing/page/\n")
        errors = self.lint()
        self.assertEqual(len(errors), 4, errors)
        for want in ("/archive/2013/b/", "/lab/aa/", "/lab/nope/", "/missing/page/"):
            self.assertTrue(any(want in e for e in errors), want)

    def test_aliases_and_tags_resolve(self):
        self.write("content/lab/a.md", GOOD_LAB.replace("---\n", "---\ntags: [Big Data]\n"
                                                        "aliases: [\"/old/a/\"]\n", 1)
                   + "[t](/tags/big-data/) [al](/old/a/)\n")
        self.assertEqual(self.lint(), [])

    def test_image_alt_and_src(self):
        self.write("content/lab/a.md", GOOD_LAB +
                   "![](/img/lab/x.png)\n![image](/img/lab/x.png)\n![Missing file](/img/lab/gone.png)\n"
                   '<img src="/img/lab/x.png">\n<img src="/img/lab/x.png" alt="">\n'
                   '<img src="/img/lab/x.png" alt="Rail map">\n')
        errors = self.lint()
        self.assertEqual(len(errors), 5, errors)
        self.assertIn("empty alt text for /img/lab/x.png", errors)
        self.assertTrue(any("non-descriptive" in e for e in errors))
        self.assertTrue(any("gone.png does not resolve" in e for e in errors))
        self.assertTrue(any("without alt attribute" in e for e in errors))

    def test_fix_alt_is_a_dry_run(self):
        text = GOOD_LAB + "Bandwidth per rail.\n\n![](/img/lab/perf_rails.png)\n"
        self.write("content/lab/a.md", text)
        self.write("static/img/lab/perf_rails.png", "")
        self.lint(fix_alt=True)
        self.assertIn("would set alt", self.output)
        self.assertIn("'Perf rails'", self.output)
        with open(os.path.join(self.root, "content/lab/a.md"), encoding="utf-8") as f:
            self.assertEqual(f.read(), text)


if __name__ == "__main__":
    unittest.main()
