---
title: "vmware server 2 - failed to initialize monitor device"
date: 2009-10-05
post_lang: en
tags: [debian, linux, server, shell]
original_url: http://www.joanmarcriera.es/2009/10/05/vmware-server-2-failed-to-initialize-monitor-device/
summary: "Fix for VMware Server 2 on Ubuntu failing with 'Failed to initialize monitor device' by unloading and blacklisting the kvm_intel module."
draft: false
---

So, yes, I need a windows OS because ... whatever. I've just registered myself in vmware and downloaded from [here](http://www.vmware.com/download/server/). To install the server you can follow [this instructions](http://www.howtoforge.com/ubuntu_vmware_server). I've installed it on my 9.04 ubuntu and it's pretty much the same. So I copied the files form a friend and when I would like to turn the virtual machine on I found myself with this error: "Failed to initialize monitor device" (in a very nice interface) This is because when compiling my modules something give me an error, and I just gone on.

Solution:

```bash
# rmmod kvm_intel
# /usr/bin/vmware-config.pl
```

It will maintain your configuration and your serial number, it's just a couple of minutes. And Ale-Hop, it's working smoothly.

And what will happen when we reboot the system. MMM, good point. So we don't need kvm_intel any more and to prevent the kernel from loading it we will create a file like /etc/modprove.d/blacklist-kvm.conf with one line "blacklist kvm_intel". Now it's done, it will not load again.

## 2026 note

VMware Server was discontinued years ago and its download no longer exists. The underlying conflict, two hypervisor modules both wanting the CPU's virtualisation extensions, is why `kvm_intel` had to be unloaded. The directory is `/etc/modprobe.d/` (the post has a typo), and today KVM with QEMU/libvirt, or VirtualBox, would be the usual way to run a Windows guest on Linux.
