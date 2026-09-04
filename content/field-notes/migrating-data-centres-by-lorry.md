---
title: "We used to migrate data centres by lorry"
date: 2026-07-22
tags: [operations]
aliases: ["/war-stories/migrating-data-centres-by-lorry/"]
---

When I arrived, the organisation had just finished a data centre migration. The method: power everything down, put the servers on a lorry, drive the lorry to the new building.

While holding a virtualisation licence that already included live migration.

Some context. The institution leased its data centres on roughly five-year terms, three of them, staggered — so by the end of year four you were always tendering for the next site and planning the next move. Migration wasn't an event. It was a lifestyle.

And yet:

- No live migration of running machines; we moved them by truck.
- No resource pools, no stretched networking, no host profiles. Most of what the licence was for, unused.
- The migration window was chosen by polling users for the least-bad date, and people were pleased that users were involved in the planning. I understand the instinct, and I think it's backwards. Users should never see a migration. It should be invisible.

The previous move had put machines down for two to three weeks. Thousands of machines. Multiply machines by hours and the number stops being an IT inconvenience and becomes stolen research time.

I had done this differently before, for several clients at Bull and at Atos, going back to the start of my career: you call the connectivity provider, they extend the layer-2 between the two sites, and the machines move live without noticing. The providers barely charge for it; it's a standard request for them.

I proposed it in my first week — because that's how I had done it for the previous ten years. It didn't land. Partly that was the estate — thousands of machines, deep storage dependencies, real reasons to be cautious — and partly it was me: a new arrival forwarding an email is not a business case. So I turned it into a ritual: every migration, I forwarded the same email. The same one. "This should be done this way. I have seen it done. I have done it myself." Years passed between the first send and the migration that finally did it, and in hindsight the email was exactly the kind of technically-right, organisationally-inert warning I have written about elsewhere.

The objection, when it finally came, was almost a compliment: yes, we know you'll say it can be done live — but have you seen how many petabytes we have?

You don't migrate petabytes that way. That's the point:

- The virtual machines move live across the stretched network.
- The data goes read-only where it sits. Nothing copies under pressure.
- Flip priority to the replica in the destination centre. Change DNS. Remount.
- Done. The petabytes never got on the lorry either way.

The way to actually staff it, I'd learned at Bull: when you have thousands of machines to move, you don't build a committee, you ask for volunteers. People sign up for a day, you hand them a tested process, and it gets done.

For the last one, I brought in a network architect I trusted. I translated the organisation; they designed the network. We stretched the VLANs between sites ourselves, and it got done. Most machines were never powered down at all. The ones people insisted "had to go down because of NFS mounts" didn't: you move the machine live, it runs a bit slow for a while, then you migrate the storage and remount. That's it.

Here's what the old way actually cost, machine by machine. You power a cluster down, and its storage — the VMware datastores, everything — goes with it. Load it onto a lorry Wednesday, drive it over, it arrives at the weekend when nobody works, and Monday you start re-checking everything from scratch. Two weeks of downtime per machine, whole clusters at once. From the outside, the services simply went dark for weeks. And that was when it went well.

The scariest moment of doing it the new way wasn't technical, it was nerve. Mid-migration, everyone was crowding into a destination centre that wasn't fully ready. The file-replicator layer that fronts the archive — a Kubernetes layer hiding the different storage tiers and copying live data to the tape DR — was mine to protect. So I did the opposite of everyone else: I moved half the Kubernetes cluster back to the old, emptying data centre and served entirely from there, while the rest of the institution piled into the new one. We were the first service fully moved and the last to depend on the new room. When the new room had teething problems mid-migration — new rooms do — our services never noticed, because we were deliberately somewhere else.

The rest of the estate went through the established procedure that time, with a planned shutdown; that was the right call for services whose dependencies had not yet been untangled. This was the middle of the pandemic, when every researcher on Earth needed the data, and my services — the data transfer services and the archive behind them — crossed that migration with zero downtime. Nobody announced it, and that is as it should be: the best migration is the one nobody notices. But it was the proof that the whole estate could.

There's a small coda. The network upgrade afterwards, 20Gb/s to 100Gb/s, sounds impressive. Most of it was deleting embarrassments: machines still on forgotten 1Gb links, storage mounted along routes nobody would have designed on purpose, servers full to the brim with logs. I added monitoring, found the wrong things, removed them. Half of "upgrading" is just looking.

Here's why I'm still pleased about it, and it's not the technology. Every research and services manager who lived through a zero-downtime migration has a new baseline. The next time someone proposes weeks of downtime to move a data centre, they will be questioned by people who have seen it done invisibly. That baseline is permanent, and it's worth thousands of hours nobody will ever have to lose again.

Infrastructure work at its best is exactly this: not the clever weekend, but the ratchet — the new floor under what an organisation considers acceptable.

What's the "we've always done it this way" in your infrastructure that one good counter-example would kill?

## Sources

- [Live migration, the concept](https://en.wikipedia.org/wiki/Live_migration)
- [Stretched VLANs / LAN extension for workload mobility (VMware architecture guide)](https://download3.vmware.com/vcat/vmw-vcloud-architecture-toolkit-spv1-webworks/Hybridity/Architecting%20a%20Hybrid%20Mobility%20Strategy/Architecting%20a%20Hybrid%20Mobility%20Strategy.2.14.html)
- [Why data centre interconnects need stretched layer 2](https://www.packetmischief.ca/2013/04/09/dci-the-need-for-stretched-layer-2/)
- [Cisco's DCI design guide for virtualised workload mobility](https://www.cisco.com/c/en/us/td/docs/solutions/Enterprise/Data_Center/DCI/4-0/EMC/dciEmc/EMC_1.html)
