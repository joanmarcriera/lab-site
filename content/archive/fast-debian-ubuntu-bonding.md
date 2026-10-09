---
title: "Fast debian / ubuntu bonding"
date: 2011-04-18
post_lang: en
tags: [debian, linux, server, ubuntu]
original_url: http://www.joanmarcriera.es/2011/04/18/fast-debian-ubuntu-bonding/
summary: "A minimal example of NIC bonding on Debian and Ubuntu using modprobe options and /etc/network/interfaces."
draft: false
---

On debian : [HOWTO](http://www.5dollarwhitebox.org/wiki/index.php/Howtos_NIC_Bonding_Debian)

There is just one different thing on Ubuntu , aliases becomes modprobe.d/bonding.conf. (it should work anyway I guess. )

```bash
root@host01:~# cat /etc/modprobe.d/bonding.conf
```

```ini
alias bond0 bonding
options bonding mode=0 miimon=100
```

```bash
root@host01:~# cat /etc/network/interfaces|grep -v ^#
```

```
auto lo
iface lo inet loopback

auto bond0
iface bond0 inet static
pre-up ifconfig bond0 up
pre-up ifconfig eth1 up
pre-up ifconfig eth0 up
address 192.0.2.131
netmask 255.255.255.192
gateway 192.0.2.129
dns-nameservers 192.0.2.2 192.0.2.3
dns-search example.com
up ifenslave bond0 eth1 eth0
down ifconfig eth1 down
down ifconfig eth0 down
down ifenslave -d bond0 eth1 eth0
```

And then just restart the network.

Enjoy.

## 2026 note

This ifenslave and `/etc/network/interfaces` recipe is the old Debian style and still works on systems that use ifupdown, though `ifconfig` and `ifenslave` come from deprecated packages. Current Ubuntu uses netplan (`bonds:` section in a YAML file) and Debian can use `bond-slaves` and `bond-mode` options in `/etc/network/interfaces` or NetworkManager. Note that mode 0 (balance-rr) can reorder packets, so modes such as active-backup or 802.3ad (LACP, needs switch support) are the usual choices now.
