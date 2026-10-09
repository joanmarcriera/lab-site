---
title: "Finding which package contains a file"
date: 2009-07-21
post_lang: en
tags: [debian, linux, server, shell]
original_url: http://www.joanmarcriera.es/2009/07/21/finding-which-package-contains-a-file/
summary: "A pointer to an article on finding which Debian package owns a file, using dpkg --search and apt-file."
third_party: true
draft: false
---

This post was a copy of someone else's article on how to find which Debian package contains a given file: `dpkg --search <file>` for files already installed, and `apt-file update` followed by `apt-file search <file>` for files in packages that are not installed. The text was not mine and I did not keep the source link; it appears to have come from the Debian Administration site.

## 2026 note

Both commands still work on Debian and Ubuntu (`dpkg -S` is the short form of `dpkg --search`, and `apt-file` is still packaged). The Debian packages website has a "Search the contents of packages" page, which does the same job without installing anything.
