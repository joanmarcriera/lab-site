---
title: "Configure Infiniband and bonding at once"
date: 2014-08-19
post_lang: en
tags: [divertimento]
original_url: http://www.joanmarcriera.es/2014/08/19/configure-infiniband-and-bonding-at-once/
summary: "A bash script that configures an Ethernet bond and an InfiniBand interface on a cluster node, deriving both IP addresses from the hostname."
draft: false
---

Just after the deploying of several nodes, running this on each of them gets them configured to be able to reboot and start running. The condition here is that each node will get its IP addresses from its own name, If hostname is cn10 , the ip addresses will be 10.1.1.10 and 10.2.0.10 . Of course we didn't have any cn0. And there were about 100 nodes.

```bash
#!/bin/bash

HOST=$(hostname)
HOSTNUM=${HOST/cn/}

echo ${HOSTNUM}

if [[ "${HOSTNUM}" -gt 108 ]]; then
	echo "This is not a compute node, bailing out..."
	exit 1
fi

for interface in eth2 eth3
do
	cat > /etc/sysconfig/network-scripts/ifcfg-${interface} <<EOF
DEVICE="${interface}"
BOOTPROTO=none
ONBOOT=yes
MASTER=bond0
SLAVE=yes
EOF

done

cat > /etc/sysconfig/network-scripts/ifcfg-bond0 <<EOF
DEVICE=bond0
BOOTPROTO=none
ONBOOT=yes
IPADDR=10.1.1.${HOSTNUM}
NETMASK=255.255.0.0
NETWORK=10.1.0.0
EOF

ifdown eth2
ifdown eth3
ifdown bond0
ifup bond0

cat > /etc/sysconfig/network-scripts/ifcfg-ib0 <<EOF
DEVICE=ib0
BOOTPROTO=none
ONBOOT=yes
IPADDR=10.2.0.${HOSTNUM}
NETMASK=255.255.0.0
NETWORK=10.2.0.0
EOF

ifdown ib0
ifup ib0
```

## 2026 note

The `ifcfg-*` files under `/etc/sysconfig/network-scripts` and the `ifup`/`ifdown` scripts are the legacy Red Hat network-scripts layout; current RHEL-family releases use NetworkManager and `nmcli` (or keyfiles) instead. The same result today is a bond connection created with `nmcli connection add type bond ...` plus the two Ethernet ports as bond slaves, and an InfiniBand (IPoIB) connection of type `infiniband` for `ib0`. The idea of deriving each node's addresses from its hostname still works fine in any provisioning script.
