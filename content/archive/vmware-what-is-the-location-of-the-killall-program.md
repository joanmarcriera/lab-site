---
title: "vmware : What is the location of the \"killall\" program ?"
date: 2009-11-12
post_lang: en
tags: [divertimento, server]
original_url: http://www.joanmarcriera.es/2009/11/12/vmware-what-is-the-location-of-the-killall-program/
summary: "The VMware Tools installer asks for the killall path on Debian; the fix is to install the psmisc package, and do not try killall5 as a test."
draft: false
---

I was installing vmware tools on a debian server and it asked where my killall program was. First I was smilling because this is silly. So I looked with whereis and certainly it was not there. So I executed killall5 expecting an error like killall will do if you do not pass any paramenter, sudently my conection went out. Killall5 is from system5 and it's hevyer compared with killall. So finally, the solution is to install the pmisc package. easy.

## 2026 note

The package is called `psmisc` (the post says "pmisc"), and `apt install psmisc` provides `killall`. `killall5` signals every process outside your own session, so running it over SSH without arguments is dangerous. On current VMs the VMware Tools installer is normally replaced by the `open-vm-tools` package.
