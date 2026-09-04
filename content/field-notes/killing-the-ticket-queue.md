---
title: "We killed the Aspera ticket queue by teaching the service desk"
date: 2026-07-20
tags: [leadership, operations]
aliases: ["/war-stories/killing-the-ticket-queue/"]
---

We were logging two or three Aspera tickets a week. After we trained the service desk, we logged zero. Not fewer. Zero. That is the whole argument for teaching people, and I'll spend the rest of this post explaining why it was ever an argument at all.

At one point the instruction I was given was to focus on the tickets. Reasonable-sounding instruction. Work the queue, close the queue. I pushed back — not out of stubbornness, but because we had no SLA, which meant nobody was contractually waiting on a clock. So I was going to spend my time on the root cause first: stop new tickets being created, then clear the ones already sitting there. That was not a popular position, and I understand why: a visible queue going down is reassuring in a way that root-cause work never is.

Here is the thing that settled it for me. The queue had been worked diligently for years, and the same problems were still there. Years of closing tickets and the tickets kept coming back. That's not a criticism of anyone who worked it; it's the nature of queues. Closing a ticket is not fixing anything. It's tidying. The ticket comes back next week wearing a slightly different hat.

So we went after the source. Two moves:

• **Train the people using the tool.** We started a Puppet teaching programme, on a simple bet: if people understood the tool they were operating, they'd make fewer mistakes and use it more. That's exactly what happened. Same logic then carried into Aspera and the service desk — teach the first line what the system actually does, and the tickets that were really "I don't understand this" evaporate. That's where the 2-3 a week went to zero.

• **Document only what can't be Googled.** My documentation rule is strict and I've never regretted it: if you can Google it, I don't write it down. Public tools have public manuals — I'm not going to maintain a worse copy of IBM's docs that rots the moment they update theirs. What I document is the in-house logic. The bits that are specific to us: why this queue feeds that box, which path a transfer takes, the local wiring nobody outside can know. That's the knowledge that actually walks out the door when a person leaves. The Googleable stuff never does.

Now the part that stuck with me. When I pushed to spend engineer time on this, the resistance wasn't about the teaching — it was about the learning. I heard the old worry, the one I have since heard in more than one organisation: if we spend time teaching the service desk, they'll leave.

It's an old joke, and it has a second half. A CFO asks, "What if we train them and they leave?" The CEO answers, "What if we don't, and they stay?" The joke lands because the second half is the one nobody wants to say out loud.

Sit with that for a second. It's a preference many organisations hold without ever stating it: untrained people who stay put over trained people who might leave. You can't argue with a belief nobody will state, so the first job was to state it, in the open and without blame, and then put a number next to it.

That fear — "if we teach them they'll leave" — is the quiet engine behind a lot of bad infrastructure. It's why knowledge stays locked in three senior heads. It's why the service desk is treated as a bounce-board that reads scripts instead of a first line that can actually resolve things. It's why the same ticket gets closed forty times instead of once. You keep people under-skilled to keep them, and then you pay for it every single week in a queue that never drains.

The maths is not subtle. A service desk is far cheaper than a senior SRE. Every ticket the first line can genuinely close is an interruption that never reaches an expensive engineer. Teaching them isn't charity or staff development for its own sake — it's the cheapest capacity you can buy. You already employ these people. Teaching them what the tools do is the highest-return training in the building, and it shows up immediately: two or three tickets a week, gone.

And the retention worry is backwards on its own terms. People are far more likely to leave a job where they're kept ignorant and set up to fail than one that invests in them. If someone becomes brilliant and moves on, you had a brilliant person for a while and they made everything better while they were there. That is not a loss. Choosing to keep them useless so they can't leave — that's the loss, and you carry it every week the tickets keep arriving.

If your team is drowning in a repeating ticket queue: are you working the queue, or are you working the reason the queue exists — and would your organisation rather its people couldn't leave than that they knew what they were doing?

## Sources

- [IBM Aspera](https://www.ibm.com/products/aspera)
- [Puppet](https://www.puppet.com/)
