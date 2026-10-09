---
title: "Reboot machine when everything is hanging"
date: 2010-01-05
post_lang: en
tags: [linux, server, shell]
original_url: http://www.joanmarcriera.es/2010/01/05/reboot-machine-when-everything-is-hanging/
summary: "Using the Magic SysRq key combination to reboot a frozen Linux machine as cleanly as possible."
draft: false
---

`<alt> + <print screen/sys rq> + <R> - <S> - <E> - <I> - <U> - <B>`

If the machine is hanging and the only help would be the power button, this key-combination will help to reboot your machine (more or less) gracefully.

- R - gives back control of the keyboard
- S - issues a sync
- E - sends all processes but init the term singal
- I - sends all processes but init the kill signal
- U - mounts all filesystem ro to prevent a fsck at reboot
- B - reboots the system

Save your file before trying this out, this will reboot your machine without warning!

<http://en.wikipedia.org/wiki/Magic_SysRq_key>

Note: Your kernel needs CONFIG_MAGIC_SYSRQ=y

## 2026 note

Magic SysRq still works on Linux, but many distributions restrict which functions are allowed through `/proc/sys/kernel/sysrq` (or `kernel.sysrq` in sysctl), so it may need enabling first. The sequence usually recommended is R E I S U B, that is, sync after the terminate and kill signals rather than before them.
