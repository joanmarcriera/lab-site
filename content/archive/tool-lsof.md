---
title: "Tool: lsof"
date: 2010-01-06
post_lang: en
tags: [linux, minicommands, shell]
original_url: http://www.joanmarcriera.es/2010/01/06/tool-lsof/
third_party: true
summary: "Pointer to a third-party tutorial on using lsof to list open files, processes and network sockets."
draft: false
---

This post was a copy of an article about `lsof`, the tool that lists open files, from the "A Unix Utility You Should Know About" series on the catonmat blog by Peteris Krumins. It walked through listing files by user, process, PID, port and network connection. The original link no longer works; the blog now lives at [catonmat.net](https://catonmat.net/).

## 2026 note

`lsof` is still available on Linux and macOS. For sockets, `ss -ltnp` on Linux is the usual modern alternative to `lsof -i`.
