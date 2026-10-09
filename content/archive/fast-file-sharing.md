---
title: "Fast file sharing"
date: 2010-01-12
post_lang: en
tags: [linux, minicommands, shell]
original_url: http://www.joanmarcriera.es/2010/01/12/fast-file-sharing/
summary: "Two one-liners to share a file quickly over HTTP, using netcat or Python's built-in web server."
draft: false
---

Option a) (port 80)

```bash
$ nc -w 5 -v -l -p 80 < file.ext
```

Option b) (port 8000)

```bash
$ python -m SimpleHTTPServer
```

Easy.

## 2026 note

Option b) is Python 2 only; on Python 3 the equivalent is `python3 -m http.server 8000`, which serves the whole current directory. Option a) still works with traditional netcat, but the flags differ between netcat versions (OpenBSD netcat, for instance, uses `nc -l 80 < file.ext` without `-p`), and binding port 80 needs root.
