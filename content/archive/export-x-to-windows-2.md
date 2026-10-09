---
title: "Export X to windows"
date: 2009-04-15
post_lang: en
tags: [linux, windows]
original_url: http://www.joanmarcriera.es/2009/04/15/export-x-to-windows-2/
summary: "A second version of the Xming and PuTTY X11 forwarding guide, adding that Xming must be started as administrator."
draft: false
---

First of all we need two programs :

- [Xming](http://sourceforge.net/projects/xming/)
- [putty](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html)

Procedure:

- Start Xming (as administrator) (if asked for "Access Control" say NO)
- Configure putty on X11 forwarding.

*(screenshot lost)*

- connect to remote machine able to export X11
- lauch application with & at the end.

*(screenshot lost)*

That’s all.

## 2026 note

The technique still works: an X server on Windows plus an SSH client with X11 forwarding enabled (`ssh -X`, or the X11 checkbox in PuTTY). Xming itself is old and no longer actively developed; VcXsrv is a commonly used free replacement, and Windows 11 with WSL2 can run Linux GUI applications directly through WSLg. Answering "no" to the access control question is only safe on a trusted network; with SSH forwarding it is not needed at all, since the connection is authenticated by SSH.
