---
title: "python -m SimpleHTTPServer"
date: 2010-10-01
post_lang: en
tags: [linux, minicommands, shell]
original_url: http://www.joanmarcriera.es/2010/10/01/python-m-simplehttpserver/
summary: "Serving the current directory over HTTP with Python's built-in module."
draft: false
---

Serve current directory tree at http://hostname:8000. If more than one is needed it is able to receive another port at the end.

```bash
python -m SimpleHTTPServer 8000
```

## 2026 note

`SimpleHTTPServer` exists only in Python 2; in Python 3 the equivalent is `python3 -m http.server 8000`. It listens on all interfaces by default, so add `--bind 127.0.0.1` when you only want local access, and treat it as a quick testing tool rather than a production web server.
