---
title: "A month-long rebalance nobody could hold a post-mortem for"
date: 2026-07-20
tags: [operations]
aliases: ["/war-stories/the-rebalance-nobody-could-post-mortem/"]
---

The storage wasn't slow because of the network. The network was saturated because the storage had been quietly rebuilding itself across three data centres for over a month, and nobody had told us. It took me a month of asking the same question every two days, and one uninvited appearance on a vendor call, to get that sentence said out loud.

I'd been given responsibility for the archive by the section head. The infrastructure side sided with the vendor on this one. My position was simple and, I thought, well-evidenced: something was wrong with the storage. We had massive monitoring across everything, and it was telling us the storage network was saturated. I wanted to know whether that saturation was causing the problem, or was a symptom of it. The answer I kept getting was "no". Not "let's check" — just "no".

So I asked the section head for permission to drop into one of the regular vendor calls the infrastructure team held. I didn't ambush anyone. I said what I'd already said many times: the network is saturated, please look for packet loss, please look at the logs, please tell me whether this is hurting the storage. Do you have monitoring? Can you look? They looked. And then, in real time, someone said: "Oh — there's something here we need to look at."

I didn't want to keep jumping into their calls like a jack-in-the-box. So I asked one thing: can we meet tomorrow, and can you invite me? They said yes. And the next day they brought their actual experts, not the usual contacts. The experts explained it in a sentence: more than one disk had failed in a single rack, which had triggered a rebalance across all three data centres. It had been running for one month and one week — longer than we'd even been complaining — and it would take several more weeks to finish. Around 25 disks had failed on that HGST array across the three sites.

And here's the detail that turned a bad week into a bad quarter. The first thing they had to do was replace all the failed disks. But every time they fixed a disk, the rebalance restarted — because you can't leave a fresh empty disk sitting in an otherwise full system. Fix a disk, restart the rebalance. Fix another, restart it again. The remedy kept resetting the clock on the recovery.

Meanwhile, the tickets coming in didn't say "storage is degraded". They complained about transfer services. That makes sense once you trace it: transfer services read from the archive, the archive was slow, so the number of open sockets on the transfer machines climbed, until Linux ran out of sockets. We were lucky. We'd already migrated to the S3 backend for the FIRE archive, so we could cut down some of those connections and keep the front door open. Without that we'd have had a second outage stacked on top of the first.

What I take from the incident itself:

• The symptom and the cause were on different teams' dashboards. The users saw "transfers are failing". The truth was roughly 25 dead disks and a rebalance nobody had surfaced. If your monitoring and your ownership are split across silos, the person feeling the pain and the person holding the cause never meet.
• "No" is not a diagnosis. A month of "no" cost us weeks we could have spent planning around the rebalance instead of arguing about whether it existed.
• You get the experts in the room by being specific and by lowering the cost of saying yes. I didn't demand escalation. I asked to be invited to one meeting.
• Ego is an outage multiplier. If you belong to an organisation, you side with the organisation's needs and push the vendor to check what they need to check — not defend the vendor's first answer.

But the part that actually kept me up wasn't the incident. It was what happened after. I tried to run a post-mortem. I tried to raise a major incident. And I couldn't — because there was no CMDB, no incident process, nothing. There was no mechanism to get the right people in a room, no shared record of what we owned, no agreed way to say "this was major, let's learn from it". So we didn't learn from it.

Several months later, after I'd spent that time trying to build the processes that would have let us learn, it happened again. Another huge batch of disks pending replacement, another rebalance. The one improvement was that this time the vendor's experts joined the meeting directly, and it was solved in three or four weeks instead of dragging. But it happened again because nothing structural had changed. You cannot do a post-mortem on an organisation that has no memory.

That is what pushed me, hard, toward two things I kept arguing for afterwards: real incident management, and capacity planning for storage. I could not present service levels to my own internal customers — ENA, EGA, the BioImage Archive — if the storage team underneath me presented none. The only mitigation I had in the meantime was human: monthly meetings with every internal customer, so at least they heard from me exactly what was happening and what my team was doing about it.

An incident is a bad day. An incident you can't hold a post-mortem for is a bad day you've agreed to repeat.

If your last serious outage happened again next quarter, is there anything in your organisation that would stop it — or just people hoping to get lucky twice?

## Sources

- [HGST (Western Digital)](https://en.wikipedia.org/wiki/HGST)
- [Erasure coding and RAID rebalancing, background](https://en.wikipedia.org/wiki/Standard_RAID_levels)
- [Amazon S3](https://aws.amazon.com/s3/)
- [EMBL-EBI data resources (ENA, EGA, BioImage Archive)](https://www.ebi.ac.uk/services)
