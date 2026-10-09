---
title: "Tool: nc / netcat"
date: 2010-01-13
post_lang: en
tags: [linux, minicommands, shell]
original_url: http://www.joanmarcriera.es/2010/01/13/tool-nc-netcat/
third_party: true
summary: "Pointer to a third-party tutorial on netcat: chat, file transfer, port scanning and proxying."
draft: false
---

This post was a copy of the catonmat.net article "A Unix Utility You Should Know About: Netcat" by Peteris Krumins. It showed netcat as a telnet replacement, a chat and file-transfer tool, a simple port scanner and a way to turn any process into a network server. The original is at [catonmat.net](https://catonmat.net/blog/unix-utilities-netcat).

## 2026 note

The `-e` option is missing from most current netcat builds, and BSD/OpenBSD netcat takes `-l PORT` without `-p`. `nmap` is the proper tool for port scanning, and `socat` covers the proxy and server cases.
