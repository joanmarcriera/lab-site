---
title: "Export X to windows"
date: 2009-03-24
post_lang: en
tags: [linux, windows]
original_url: http://www.joanmarcriera.es/2009/03/24/export-x-to-windows/
summary: "How to run graphical Linux applications on a Windows desktop using Xming and PuTTY X11 forwarding."
draft: false
---

First of all we need two programs :

- [Xming](http://sourceforge.net/projects/xming/)
- [putty](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html)

Procedure:

- Start Xming
- Configure putty on X11 forwarding.

*(screenshot lost)*

- connect to remote machine able to export X11
- lauch application with & at the end.

*(screenshot lost)*

That's all.

## 2026 note

The technique still works: an X server on Windows plus an SSH client with X11 forwarding enabled (`ssh -X`, or the X11 checkbox in PuTTY). Xming itself is old and no longer actively developed; VcXsrv is a commonly used free replacement, and Windows 11 with WSL2 can run Linux GUI applications directly through WSLg. For remote desktops over slow links, tools such as X2Go or a VNC server are often more comfortable than raw X forwarding.
