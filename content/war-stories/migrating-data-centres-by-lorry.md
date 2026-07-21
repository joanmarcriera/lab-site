---
title: "We used to migrate data centres by lorry"
date: 2026-07-22
series: "War stories"
---

When I arrived, the organisation had just finished a data centre migration. The method: power everything down, put the servers on a lorry, drive the lorry to the new building.

While paying for VMware. All of it.

Some context. The institution leased its data centres on roughly five-year terms, three of them, staggered — so by the end of year four you were always tendering for the next site and planning the next move. Migration wasn't an event. It was a lifestyle.

And yet:

• No vMotion. The licence covered live migration of running machines; we moved them by truck.
• No resource pools. Open the VMware manual: resource pools are the first chapter. We were on page zero.
• No VLAN stretching, no host profiles. Everything you actually pay VMware for, unused.
• The migration plan was coordinated with Doodle polls, and people were proud that users were involved in the planning. That's backwards. Users should never see a migration. It should be invisible. The users should not care at all.

The previous move had put machines down for two to three weeks. Thousands of machines. Multiply machines by hours and the number stops being an IT inconvenience and becomes stolen research time.

I had done this differently before, for several clients at Bull and at Atos, going back to the start of my career: you call the connectivity provider, they extend the layer-2 between the two sites, and the machines move live without noticing. The providers barely charge for it; it's a standard request for them.

I proposed it in my first week — because that's how I had done it for the previous ten years. There was never a counterproposal — they simply kept doing it the old way, and the one argument offered was that "the virtual machines would not move". That's what VMware is for. So I turned it into a ritual: every migration, I forwarded the same email. The same one. "This should be done this way. I have seen it done. I have done it myself." Nine years passed between the first send and the migration that finally did it.

The objection, when it finally came, was almost a compliment: "Come on, Marc, again? You'll tell us we can migrate live, but don't you see how many petabytes we have?"

You don't migrate petabytes that way. That's the point:

• The virtual machines move live across the stretched network.
• The data goes read-only where it sits. Nothing copies under pressure.
• Flip priority to the replica in the destination centre. Change DNS. Remount.
• Done. The petabytes never got on the lorry either way.

The way to actually staff it, I'd learned at Bull: when you have thousands of machines to move, you don't build a committee, you ask for volunteers. People sign up for a day, you hand them a tested process, and it gets done. Instead, here, a data-centre move was being organised by Doodle poll — hunting for the window that annoyed the fewest services. That is a true detail, not a joke. It was just painful.

For the last one, I pulled in a friend who holds two CCIEs and doesn't speak much English. I translated; he designed. We stretched the VLANs between sites ourselves — we ended up paying for what a provider would have thrown in, but it got done. Most machines were never powered down at all. The ones people insisted "had to go down because of NFS mounts" didn't: you move the machine live, it runs a bit slow for a while, then you migrate the storage and remount. That's it.

Here's what the old way actually cost, machine by machine. You power a cluster down, and its storage — the VMware datastores, everything — goes with it. Load it onto a lorry Wednesday, drive it over, it arrives at the weekend when nobody works, and Monday you start re-checking everything from scratch. Two weeks of downtime per machine, whole clusters at once. From the outside, the services simply went dark for weeks. And that was when it went well — the previous time, someone forgot to change some access points and it was a mess.

The scariest moment of doing it the new way wasn't technical, it was nerve. Mid-migration, everyone was crowding into a destination centre that wasn't fully ready. FIRE — the file replicator that fronts the archive, a Kubernetes layer hiding the different storage tiers and copying live data to the tape DR — was mine to protect. So I did the opposite of everyone else: I moved half the Kubernetes cluster back to the old, emptying data centre and served entirely from there, while the rest of the institution piled into the new one. We were the first service fully moved and the last to depend on the new room. When the new centre hit power problems mid-migration — and it did — our services never noticed, because we were deliberately somewhere else.

Then we waited while the rest of the estate went through the old procedure: shut down for one to two weeks. This was the middle of the pandemic, when every researcher on Earth needed the data. My services — the data transfer services and FIRE, the archive behind them — were the only ones that crossed that migration with zero downtime. The only ones.

Nobody announced it internally. It hadn't been anyone's idea upstairs, so there was nothing to announce.

There's a small coda. The network upgrade afterwards, 20Gb/s to 100Gb/s, sounds impressive. Most of it was deleting embarrassments: machines still on forgotten 1Gb links, NFS mounted through the external firewall, servers full to the brim with logs. I added monitoring, found the wrong things, removed them. Half of "upgrading" is just looking.

Here's why I'm still pleased about it, and it's not the technology. Every research and services manager who lived through a zero-downtime migration in 2025 has a new baseline. The next time someone proposes weeks of downtime to move a data centre, they will be questioned by people who have seen it done invisibly. That baseline is permanent, and it's worth thousands of hours nobody will ever have to lose again.

Infrastructure work at its best is exactly this: not the clever weekend, but the ratchet — the new floor under what an organisation considers acceptable.

What's the "we've always done it this way" in your infrastructure that one good counter-example would kill?

## Sources

- [Live migration, the concept](https://en.wikipedia.org/wiki/Live_migration)
- [Stretched VLANs / LAN extension for workload mobility (VMware architecture guide)](https://download3.vmware.com/vcat/vmw-vcloud-architecture-toolkit-spv1-webworks/Hybridity/Architecting%20a%20Hybrid%20Mobility%20Strategy/Architecting%20a%20Hybrid%20Mobility%20Strategy.2.14.html)
- [Why data centre interconnects need stretched layer 2](https://www.packetmischief.ca/2013/04/09/dci-the-need-for-stretched-layer-2/)
- [Cisco's DCI design guide for virtualised workload mobility](https://www.cisco.com/c/en/us/td/docs/solutions/Enterprise/Data_Center/DCI/4-0/EMC/dciEmc/EMC_1.html)
