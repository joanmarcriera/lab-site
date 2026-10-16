---
title: "NIC bonding, then and now: from ifenslave to a ten-line YAML file"
date: 2026-10-16
draft: true
tags: [networking, linux, bonding, netplan]
summary: "The 2011 bonding recipe rebuilt on a current Ubuntu with iproute2 and netplan, including what happens to the bond when the active link is cut."
---

## Problem

In 2011 I wrote [a short post on bonding two NICs on Debian and
Ubuntu](/archive/2011/fast-debian-ubuntu-bonding/): a `modprobe.d` file, an `ifenslave` line in
`/etc/network/interfaces`, restart the network. In 2014 I did the same thing
[together with InfiniBand](/archive/2014/configure-infiniband-and-bonding-at-once/).

Neither of those works as written on a current Ubuntu. `ifenslave` and `/etc/network/interfaces`
are gone from a default install, and the network is described in YAML by netplan, which hands it
to systemd-networkd. The idea of bonding has not changed. The way you say it has.

## Approach

Build the same thing three ways in a throw-away Ubuntu 24.04 container, so nothing touches a real
interface:

1. **By hand with `ip`**, to see what the kernel is actually being asked to do.
2. **In netplan**, the way a current install would do it.
3. **Read what netplan generates**, because that is what systemd-networkd really runs.

The container is privileged and has its own network namespace. The "NICs" are two virtual
ethernet pairs, `eth1`/`sw1` and `eth2`/`sw2`. The `sw` ends play the part of switch ports, and I
can pull their cables by setting them down.

## Steps

**By hand.** Make the bond, put the two links under it, bring everything up:

```bash
ip link add eth1 type veth peer name sw1
ip link add eth2 type veth peer name sw2
ip link add bond0 type bond mode active-backup miimon 100
ip link set eth1 down; ip link set eth2 down      # a link must be down to be enslaved
ip link set eth1 master bond0; ip link set eth2 master bond0
ip link set sw1 up; ip link set sw2 up; ip link set bond0 up
```

`miimon 100` is the same `miimon=100` as in 2011: check the link state every 100 ms. The mode is
different on purpose. The 2011 post used `mode=0`, round-robin across both links. I use
`active-backup` here because its failure behaviour is the easiest to read.

**In netplan.** The same bond as a file:

```yaml
network:
  version: 2
  ethernets:
    eth1: {}
    eth2: {}
  bonds:
    bond0:
      interfaces: [eth1, eth2]
      addresses: [192.0.2.10/24]
      parameters:
        mode: active-backup
        mii-monitor-interval: 100
        primary: eth1
```

Saved as `/etc/netplan/60-bond.yaml` with mode `600`. Netplan warns about looser permissions.
`netplan apply` would make it live. I stopped at `netplan generate`, which writes the real
configuration without applying it.

## Verify

The bond as the kernel reports it right after the hand-built version:

```
$ grep -E "Bonding Mode|Currently Active Slave|MII Status|Slave Interface" /proc/net/bonding/bond0
Bonding Mode: fault-tolerance (active-backup)
Currently Active Slave: eth1
MII Status: up
Slave Interface: eth1
MII Status: up
Slave Interface: eth2
MII Status: up
```

Then cut the cable on the active link and ask again:

```
$ ip link set sw1 down
$ grep -E "Currently Active Slave|Slave Interface|MII Status" /proc/net/bonding/bond0
Currently Active Slave: eth2
MII Status: up
Slave Interface: eth1
MII Status: down
Slave Interface: eth2
MII Status: up
```

The bond stays `up`, eth1 is reported `down`, and traffic moves to eth2. That one-second
experiment is the whole point of a bond, and it is the check I would run after any change.

What netplan generated from the YAML, trimmed to the lines that matter:

```
/run/systemd/network/10-netplan-bond0.netdev
    [NetDev]
    Name=bond0
    Kind=bond
    [Bond]
    Mode=active-backup
    MIIMonitorSec=100ms

/run/systemd/network/10-netplan-bond0.network
    [Match]
    Name=bond0
    [Network]
    LinkLocalAddressing=ipv6
    Address=192.0.2.10/24
    ConfigureWithoutCarrier=yes

/run/systemd/network/10-netplan-eth1.network
    [Network]
    LinkLocalAddressing=no
    Bond=bond0
    PrimarySlave=true

/run/systemd/network/10-netplan-eth2.network
    [Network]
    LinkLocalAddressing=no
    Bond=bond0
```

Each line of the old `ifenslave` recipe has a counterpart. The module options became the `[Bond]`
section. The `up ifenslave bond0 eth1 eth0` line became a `Bond=bond0` in each member's file.
The `pre-up ifconfig ... up` ceremony is gone, because networkd brings the links up itself.

## Gotchas

- **What I did not test.** The container has no systemd running, so `netplan generate` printed
  `Failed to connect to bus` when it tried to reload the daemon. The files are real and complete,
  but I did not watch networkd consume them, and I did not test `mode=0` (the 2011 mode) or
  802.3ad. The failover above is `active-backup` only.
- **`miimon` only sees the local link.** If the switch behind the port dies and the cable stays
  up, MII still says up. `arp_ip_target` with `arp_interval` is the answer to that.
- **A link must be down before it is enslaved.** The `ip link set ... down` lines are not
  decoration. Without them the kernel refuses.
- **Round-robin (`mode=0`) can reorder packets**, which TCP dislikes. For switches that support
  it, `802.3ad` (LACP) is what most people want today.
- **Netplan's `primary:` is not a promise.** It prefers eth1 whenever eth1 is back, which means a
  flapping cable causes repeated failovers. `primary_reselect` controls that.
- **The old recipe's `ifenslave` is still installable**, and `/etc/network/interfaces` still
  works on Debian with ifupdown. It is a choice now, not a default.

## Further reading

- The kernel's own document, `Documentation/networking/bonding.rst`, covers every mode and
  option.
- `man netplan` and the netplan reference, for the bond parameters.
- `man systemd.netdev`, for what `[Bond]` accepts.
