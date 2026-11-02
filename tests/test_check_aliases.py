"""Tests for tools/check_aliases.py on synthetic content trees."""
import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import check_aliases  # noqa: E402

CLEAN = {
    "about.md": '---\ntitle: "About"\naliases: ["/me/"]\n---\nHi.\n',
    "field-notes/_index.md": '---\ntitle: "Notes"\naliases: ["/war-stories/"]\n---\n',
    "field-notes/a-post.md": ('---\ntitle: "A"\naliases:\n  - /war-stories/a-post\n'
                              '  - "/old/a/"\n---\nBody.\n'),
    "lab/toml.md": '+++\ntitle = "T"\naliases = ["/t-old/"]\nslug = "tee"\n+++\n',
    "archive/old.md": '---\ntitle: "Old"\ndate: 2010-03-01\naliases: ["/2010/03/old/"]\n---\n',
}


class CheckAliasesTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.manifest = self.root / "tests" / "aliases.expected.txt"
        for rel, text in CLEAN.items():
            self.write(rel, text)
        self.run_tool("--update")

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, rel, text):
        path = self.root / "content" / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def run_tool(self, *args):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            rc = check_aliases.main(["--root", str(self.root), *args])
        return rc, out.getvalue() + err.getvalue()

    def test_clean_tree_passes(self):
        rc, out = self.run_tool()
        self.assertEqual(rc, 0, out)
        self.assertIn("6 aliases checked, 0 errors", out)

    def test_parses_yaml_block_toml_and_archive_urls(self):
        aliases, urls = check_aliases.collect(self.root / "content")
        self.assertIn("/war-stories/a-post/", aliases)
        self.assertIn("/t-old/", aliases)
        self.assertIn("/lab/tee/", urls)
        self.assertIn("/archive/2010/old/", urls)
        self.assertIn("/field-notes/", urls)

    def test_duplicate_fails(self):
        self.write("lab/dup.md", '---\ntitle: "D"\naliases: ["/me"]\n---\n')
        rc, out = self.run_tool()
        self.assertEqual(rc, 1)
        self.assertIn("duplicate alias /me/ in about.md, lab/dup.md", out)

    def test_collision_with_page_url_fails(self):
        self.write("lab/x.md", '---\ntitle: "X"\naliases: ["/field-notes/a-post/"]\n---\n')
        rc, out = self.run_tool()
        self.assertEqual(rc, 1)
        self.assertIn("alias /field-notes/a-post/ in lab/x.md collides with the URL of "
                      "field-notes/a-post.md", out)

    def test_self_alias_is_only_a_note(self):
        self.write("disclaimer.md", '---\ntitle: "D"\naliases: ["/disclaimer/"]\n---\n')
        rc, out = self.run_tool()
        self.assertEqual(rc, 0, out)
        self.assertIn("is the page's own URL", out)

    def test_removed_alias_fails(self):
        (self.root / "content" / "field-notes" / "a-post.md").rename(
            self.root / "content" / "field-notes" / "renamed.md")
        self.write("field-notes/renamed.md", '---\ntitle: "A"\n---\nBody.\n')
        rc, out = self.run_tool()
        self.assertEqual(rc, 1)
        self.assertIn("alias /war-stories/a-post/ from aliases.expected.txt is no longer "
                      "produced", out)
        self.assertIn("/old/a/", out)

    def test_update_is_idempotent(self):
        first = self.manifest.read_text()
        self.assertEqual(self.run_tool("--update")[0], 0)
        self.assertEqual(self.manifest.read_text(), first)
        self.assertEqual(len([l for l in first.splitlines() if l.startswith("/")]), 6)


if __name__ == "__main__":
    unittest.main()
