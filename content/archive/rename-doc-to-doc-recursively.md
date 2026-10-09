---
title: "Rename  .DOC to .doc recursively"
date: 2010-01-06
post_lang: en
tags: [linux, shell]
original_url: http://www.joanmarcriera.es/2010/01/06/rename-doc-to-doc-recursively/
summary: "Renaming every .DOC file to .doc under a directory tree with find and rename."
draft: false
---

This is the easy way to change all files matching a patten.

```bash
$ find /path/to/images -name '*.DOC' -exec rename "s/.DOC/.doc/g" {} \;
```

## 2026 note

This relies on the Perl-based `rename` (the default on Debian and Ubuntu); on Fedora/RHEL the `rename` from util-linux has a different syntax. A safer pattern today is `find /path -name '*.DOC' -exec rename 's/\.DOC$/.doc/' {} +`, which escapes the dot and only touches the extension at the end of the name.
