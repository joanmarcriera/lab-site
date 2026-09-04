---
title: "A month-long rebalance, and the post-mortem we weren't ready to hold"
date: 2026-07-20
tags: [operations]
aliases: ["/war-stories/the-rebalance-nobody-could-post-mortem/"]
---

The storage wasn't slow because of the network. The network was saturated because the storage had been quietly rebuilding itself across three data centres for over a month, and nobody — vendor, infrastructure team, or me — had joined that up with what users were feeling. It took a month of asking the same question every two days, and one vendor call I asked to sit in on, to get that sentence said out loud.

I'd been given responsibility for the archive. The infrastructure team, reasonably, trusted the vendor's first answer; they had the relationship and the vendor had the telemetry. My position was simple and, I thought, well-evidenced: something was wrong with the storage. We had massive monitoring across everything, and it was telling us the storage network was saturated. I wanted to know whether that saturation was causing the problem, or was a symptom of it. The answer I kept getting was "no". And, in fairness to everyone, I kept asking it the same way, which is not the same thing as making progress.

So I asked for permission to drop into one of the regular vendor calls the infrastructure team held. I didn't ambush anyone. I said what I'd already said many times: the network is saturated, please look for packet loss, please look at the logs, please tell me whether this is hurting the storage. Do you have monitoring? Can you look? They looked. And then, in real time, someone said: "Oh — there's something here we need to look at."

I didn't want to keep jumping into their calls like a jack-in-the-box. So I asked one thing: can we meet tomorrow, and can you invite me? They said yes. And the next day they brought their actual experts, not the usual contacts. The experts explained it in a sentence: more than one disk had failed in a single rack, which had triggered a rebalance across all three data centres. It had been running for one month and one week — longer than we'd even been complaining — and it would take several more weeks to finish. Dozens of disks had failed across the three sites.

And here's the detail that turned a bad week into a bad quarter. The first thing they had to do was replace all the failed disks. But every time they fixed a disk, the rebalance restarted — because you can't leave a fresh empty disk sitting in an otherwise full system. Fix a disk, restart the rebalance. Fix another, restart it again. The remedy kept resetting the clock on the recovery.

Meanwhile, the tickets coming in didn't say "storage is degraded". They complained about transfer services. That makes sense once you trace it: transfer services read from the archive, the archive was slow, so the number of open sockets on the transfer machines climbed, until Linux ran out of sockets. We were lucky. We'd already migrated to the S3 backend for the archive, so we could cut down some of those connections and keep the front door open. Without that we'd have had a second outage stacked on top of the first.

What I take from the incident itself:

• The symptom and the cause were on different teams' dashboards. The users saw "transfers are failing". The truth was dozens of dead disks and a rebalance nobody had surfaced. If your monitoring and your ownership are split across silos, the person feeling the pain and the person holding the cause never meet.
• "No" is not a diagnosis. A month of "no" cost us weeks we could have spent planning around the rebalance instead of arguing about whether it existed. And a month of my asking the same question the same way was not a diagnosis either.
• You get the experts in the room by being specific and by lowering the cost of saying yes. I didn't demand escalation. I asked to be invited to one meeting.
• Ego is an outage multiplier — mine included. The fastest path was never to be right; it was to get the vendor to check what they needed to check, and the way to do that was an invitation, not an argument.

But the part that actually kept me up wasn't the incident. It was what happened after. I tried to run a post-mortem. I tried to raise a major incident. And I found we didn't yet have the machinery for either: no configuration record we all agreed on, no major-incident process, no established way to get the right people in a room and say "this was major, let's learn from it". The organisation — including me, in a role that should have owned a share of this — hadn't built it yet. So we didn't learn from it the way we should have.

Several months later, after I'd spent that time trying to build the processes that would have let us learn, it happened again. Another huge batch of disks pending replacement, another rebalance. The one improvement was that this time the vendor's experts joined the meeting directly, and it was solved in three or four weeks instead of dragging. It happened again because, in those months, none of us had yet turned the first incident into a structural change. A post-mortem needs an organisational memory to live in, and building that memory was still the work in front of us.

That is what pushed me, hard, toward two things I kept arguing for afterwards: real incident management, and capacity planning for storage. I couldn't credibly promise service levels to my own internal customers until the layer beneath me could promise them to me. In the meantime the mitigation was human: monthly meetings with every internal customer, so at least they heard from me exactly what was happening and what my team was doing about it.

An incident is a bad day. An incident you can't hold a post-mortem for is a bad day you've agreed to repeat.

If your last serious outage happened again next quarter, is there anything in your organisation that would stop it — or just people hoping to get lucky twice?

## Sources

- [Erasure coding and RAID rebalancing, background](https://en.wikipedia.org/wiki/Standard_RAID_levels)
- [Amazon S3](https://aws.amazon.com/s3/)
