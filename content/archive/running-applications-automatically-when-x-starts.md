---
title: "Running applications automatically when X starts"
date: 2011-10-02
post_lang: en
tags: [debian, gnome, linux, ubuntu]
original_url: http://www.joanmarcriera.es/2011/10/02/running-applications-automatically-when-x-starts/
third_party: true
summary: "A note pointing to a third-party Debian article on starting programs automatically at X11 login."
draft: false
---

This post was a copy of a Debian Administration article explaining how to start programs automatically when X11 starts: through the KDE Autostart directory or the GNOME session settings, and for other setups through a script in `/etc/X11/Xsession.d` (global) or `~/.xsession` (per user). The text is not mine, so please read the original at [debian-administration.org](https://www.debian-administration.org/).

## 2026 note

`/etc/X11/Xsession.d` and `~/.xsession` still exist on Debian-based systems that start X11 through an Xsession-aware display manager. Current desktops use XDG autostart, that is `.desktop` files in `~/.config/autostart/`, and a Wayland session does not run the Xsession scripts at all.
