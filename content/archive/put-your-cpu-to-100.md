---
title: "Put your CPU to 100%"
date: 2010-04-16
post_lang: en
tags: [linux, minicommands, server, shell]
original_url: http://www.joanmarcriera.es/2010/04/16/put-your-cpu-to-100/
summary: "A one-line shell command that keeps one CPU core at full load for testing."
draft: false
---

```bash
$ yes > /dev/null
```

With this command one of our cpus will go nuts. Use it for testing purpose only.

## 2026 note

This still works: `yes > /dev/null` pins one core, so start one copy per core (or more) to load the whole machine. For proper load testing, `stress-ng` is the common current tool, as it can stress CPU, memory and I/O with controlled workers and a timeout.
