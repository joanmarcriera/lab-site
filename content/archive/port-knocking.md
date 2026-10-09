---
title: "Port Knocking!"
date: 2011-10-03
post_lang: en
tags: [divertimento, linux, server, shell]
original_url: http://www.joanmarcriera.es/2011/10/03/port-knocking/
summary: "Hiding the SSH port behind a knock sequence with knockd, which opens and closes the firewall rule on demand."
draft: false
---

Would you like to hide a port until a certain knock-knock procedure is received?

Like this:

```bash
knock3000 4000 5000 && ssh -puser@host && knock5000 4000 3000
```

Knock on ports to open a port to a service (ssh for example) and knock again to close the port.

First you need to install knockd.
See example config file below.

```ini
[options]

logfile = /var/log/knockd.log

[openSSH]

sequence = 3000,4000,5000

seq_timeout = 5

command = /sbin/iptables -A INPUT -i eth0 -s %IP% -p tcp --dport 22 -j ACCEPT

tcpflags = syn

[closeSSH]

sequence = 5000,4000,3000

seq_timeout = 5

command = /sbin/iptables -D INPUT -i eth0 -s %IP% -p tcp --dport 22 -j ACCEPT

tcpflags = syn
```

Hope you found it userful.

## 2026 note

`knockd` is still packaged and works, but on current distributions the firewall is often nftables or firewalld rather than raw iptables, so the `command` lines need adapting, and `-I` (insert) is safer than `-A` (append) if a drop rule already exists earlier in the chain. Port knocking only hides the port; for real protection use SSH key authentication, and consider putting SSH behind a VPN such as WireGuard. The one-liner at the top lost its spaces somewhere along the way; with the `knock` client it would read `knock host 3000 4000 5000 && ssh user@host && knock host 5000 4000 3000`.
