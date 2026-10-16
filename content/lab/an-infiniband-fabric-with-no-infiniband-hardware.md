---
title: "An InfiniBand fabric with no InfiniBand hardware"
date: 2026-10-09
draft: false
tags: [infiniband, hpc, networking]
summary: "A simulated four-switch InfiniBand fabric in one Docker container, run by a real subnet manager. Cut a link and watch the forwarding tables change."
---

## Problem

I designed and cabled InfiniBand fabrics for HPC clusters between 2011 and 2014. In 2014 I
wrote [a script that configured the IPoIB and bonding interfaces from the hostname](/archive/2014/configure-infiniband-and-bonding-at-once/),
and then I spent a decade on storage and identity. Coming back to it for AI clusters, I
wanted to practise the management side again: who assigns the addresses, who computes the
routes, what happens when a cable dies. A switch and two cards to practise on cost more
than I wanted to spend to relearn `ibroute`.

## Approach

An InfiniBand fabric does nothing until a **subnet manager** has discovered it, given every
port a local identifier (LID) and written a forwarding table into every switch. All of that
happens in management datagrams, and those can be simulated.

[ibsim](https://github.com/linux-rdma/ibsim) loads a topology file and answers management
datagrams on a local socket. A preloaded library, `libumad2sim.so`, replaces the user-space
library the tools normally use to reach the kernel. So the *real* OpenSM and the *real*
`infiniband-diags` run unchanged and talk to a fabric that exists only in memory.

I packaged this as [infiniband-lab](https://github.com/joanmarcriera/infiniband-lab): one
container, two topologies and 14 exercises. The interesting topology is a diamond, with two
paths between the left and right hosts:

```
HCA01 ─┐         ┌─ SW02 ─┐         ┌─ HCA03
       ├─ SW01 ──┤        ├── SW04 ─┤
HCA02 ─┘         └─ SW03 ─┘         └─ HCA04
```

## Steps

```bash
git clone https://github.com/joanmarcriera/infiniband-lab && cd infiniband-lab
scripts/lab up            # builds Ubuntu 24.04 + ibsim-utils, opensm, infiniband-diags
scripts/lab shell         # a prompt inside the container
reset-lab.sh redundant    # start the diamond fabric and OpenSM on HCA01
```

```
ibsim up with topology 'redundant'. Next: start-opensm.sh
OpenSM on HCA01 (0x0002c90000000011): SUBNET UP
```

`SUBNET UP` is the line that matters. It means OpenSM has swept the fabric, assigned LIDs
and programmed the switches. Now ask the fabric what it is:

```
$ ibnetdiscover -l
Ca	 : 0x0002c90000000040 ports 1 devid 0x1017 vendid 0x2c9 "HCA04"
Ca	 : 0x0002c90000000030 ports 1 devid 0x1017 vendid 0x2c9 "HCA03"
Ca	 : 0x0002c90000000020 ports 1 devid 0x1017 vendid 0x2c9 "HCA02"
Ca	 : 0x0002c90000000010 ports 1 devid 0x1017 vendid 0x2c9 "HCA01"
Switch	 : 0x0002c90000000400 ports 8 devid 0xd2f0 vendid 0x2c9 "SW04"
Switch	 : 0x0002c90000000300 ports 8 devid 0xd2f0 vendid 0x2c9 "SW03"
Switch	 : 0x0002c90000000200 ports 8 devid 0xd2f0 vendid 0x2c9 "SW02"
Switch	 : 0x0002c90000000100 ports 8 devid 0xd2f0 vendid 0x2c9 "SW01"

$ sminfo
sminfo: sm lid 1 sm guid 0x2c90000000011, activity count 190 priority 0 state 3 SMINFO_MASTER
```

The subnet manager is the master, at LID 1. Trace a packet from HCA01 (LID 1) to HCA04 (LID 8):

```
$ ibtracert 1 8
From ca {0x0002c90000000010} portnum 1 lid 1-1 "HCA01"
[1] -> switch port {0x0002c90000000100}[1] lid 2-2 "SW01"
[4] -> switch port {0x0002c90000000300}[1] lid 4-4 "SW03"
[2] -> switch port {0x0002c90000000400}[4] lid 5-5 "SW04"
[2] -> ca port {0x0002c90000000041}[1] lid 8-8 "HCA04"
To ca {0x0002c90000000040} portnum 1 lid 8-8 "HCA04"
```

It goes through SW03. The reason is in SW01's linear forwarding table, which is nothing more
than "for destination LID x, send out of port y". `ibroute` prints it; a small helper in the
repo draws it as a table:

```
$ ibroute 2 | lft-table.py
SW01  (LID 2, GUID 0x0002c90000000100)
┌──────┬─────────────┬─────────────┐
│ DLID │ Egress port │ Destination │
├──────┼─────────────┼─────────────┤
│ 1    │ 1           │ HCA01       │
│ 2    │ 0           │ SW01        │
│ 3    │ 3           │ SW02        │
│ 4    │ 4           │ SW03        │
│ 5    │ 3           │ SW04        │
│ 6    │ 2           │ HCA02       │
│ 7    │ 3           │ HCA03       │
│ 8    │ 4           │ HCA04       │
└──────┴─────────────┴─────────────┘
```

Destination 8 leaves by port 4, towards SW03. Destination 7, the host next to it, leaves by
port 3 towards SW02. OpenSM has spread the two hosts across the two paths.

## Verify: cut a link

Unplug SW01 port 4, the link to SW03, and give the subnet manager a sweep to notice:

```
$ simcmd 'Unlink "S-0002c90000000100"[4]'
$ sleep 15
$ ibtracert 1 8
From ca {0x0002c90000000010} portnum 1 lid 1-1 "HCA01"
[1] -> switch port {0x0002c90000000100}[1] lid 2-2 "SW01"
[3] -> switch port {0x0002c90000000200}[1] lid 3-3 "SW02"
[2] -> switch port {0x0002c90000000400}[3] lid 5-5 "SW04"
[2] -> ca port {0x0002c90000000041}[1] lid 8-8 "HCA04"
To ca {0x0002c90000000040} portnum 1 lid 8-8 "HCA04"
```

The route now goes through SW02. Nobody reconfigured anything. OpenSM logged an off-schedule
sweep, recomputed the routes and rewrote the table. These are the two rows that changed:

```
$ ibroute 2 | lft-table.py
│ 4    │ 3           │ SW03        │
│ 8    │ 3           │ HCA04       │
```

Every destination on SW01 that used port 4 now uses port 3, including SW03 itself, which is
reached the long way round through SW04. On a real cluster this is the moment a job either
carries on or dies, depending on how long the sweep took and what the application's
timeouts were.

## Gotchas

- **It failed on my Mac the first time.** The environment script had the preload path
  hard-coded to `/usr/lib/x86_64-linux-gnu/`. On Apple Silicon the container is `aarch64`,
  the library is somewhere else, and the loader only prints a warning:
  `object ... from LD_PRELOAD cannot be preloaded ... ignored`. OpenSM then looked for real
  hardware, found none and never reached `SUBNET UP`. The fix is one line,
  `/usr/lib/$(uname -m)-linux-gnu/umad2sim/libumad2sim.so`.
- **ibsim itself must not be preloaded**, or it intercepts its own calls. The start script
  strips `LD_PRELOAD` for that one process.
- **Management plane only.** There is no data plane: no RDMA, no verbs, no `ibping`, and
  `perfquery` counters are always zero. The "10 Gbps 4X" link speed is a number in a text
  file. Partition keys are not simulated either.
- **Restored routes are not the old routes.** Relink the cable and OpenSM computes a valid
  set of routes again, but not necessarily the set you started with. Do not write a check
  that expects them to be identical.

I built infiniband-lab with Claude Code as a pair programmer.

## Further reading

- [infiniband-lab](https://github.com/joanmarcriera/infiniband-lab): the exercises, a
  cheat sheet and a matrix of which diagnostic tools work against the simulator.
- [linux-rdma/ibsim](https://github.com/linux-rdma/ibsim) and
  [OpenSM](https://github.com/linux-rdma/opensm).
- What the simulator cannot teach is the data plane. I did that part on a rented pair of
  InfiniBand machines, and wrote it up in
  [part 2: Two H100 nodes, eight rails](/lab/two-h100-nodes-eight-rails-what-the-fabric-actually-does/).
