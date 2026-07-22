---
title: "We killed the Aspera ticket queue by teaching the service desk"
date: 2026-07-20
tags: [leadership, operations]
aliases: ["/war-stories/killing-the-ticket-queue/"]
---

We were logging two or three Aspera tickets a week. After we trained the service desk, we logged zero. Not fewer. Zero. That is the whole argument for teaching people, and I'll spend the rest of this post explaining why it was ever an argument at all.

At one point I had a boss who told me to focus on the tickets. Reasonable-sounding instruction. Work the queue, close the queue. I said no — not out of stubbornness, but because we had no SLA, which meant nobody was contractually waiting on a clock. So I was going to spend my time on the root cause first: stop new tickets being created, then clear the ones already sitting there. He was not happy about it. He wanted the queue worked in order, top to bottom, forever.

Here is the thing that settled it for me. He had been at it for years, and the same problems were still there. Years of closing tickets and the tickets kept coming back. My system worked and his didn't — and the proof was that his had already had years to work and hadn't. Closing a ticket is not fixing anything. It's tidying. The ticket comes back next week wearing a slightly different hat.

So we went after the source. Two moves:

• **Train the people using the tool.** We started a Puppet teaching programme, on a simple bet: if people understood the tool they were operating, they'd make fewer mistakes and use it more. That's exactly what happened. Same logic then carried into Aspera and the service desk — teach the first line what the system actually does, and the tickets that were really "I don't understand this" evaporate. That's where the 2-3 a week went to zero.

• **Document only what can't be Googled.** My documentation rule is strict and I've never regretted it: if you can Google it, I don't write it down. Public tools have public manuals — I'm not going to maintain a worse copy of IBM's docs that rots the moment they update theirs. What I document is the in-house logic. The bits that are specific to us: why this queue feeds that box, which path a transfer takes, the local wiring nobody outside can know. That's the knowledge that actually walks out the door when a person leaves. The Googleable stuff never does.

Now the exchange that stuck with me. When I pushed to spend engineer time on this, the resistance wasn't about the teaching — it was about the learning. I heard, from senior managers, the line: "if we spend time teaching the service desk, they'll leave."

It's an old joke, and it has a second half. A CFO asks, "What if we train them and they leave?" The CEO answers, "What if we don't, and they stay?" I was waiting for someone to say the second part. And they did — they got there themselves — and then, remarkably, they landed on the wrong side of it. "Yes, we want them to stay — but then they wouldn't know what to do." And I said: fine, but at least they stay, and we don't have to hire anyone else.

Sit with that for a second. The stated preference was untrained people who stay put over trained people who might leave. An organisation actively choosing that its staff not know how to do their jobs, because ignorant-and-present felt safer than capable-and-mobile. I didn't have the word for what I felt. Something between astonished and delighted, because it laid the whole problem bare in one sentence.

That fear — "if we teach them they'll leave" — is the quiet engine behind a lot of bad infrastructure. It's why knowledge stays locked in three senior heads. It's why the service desk is treated as a bounce-board that reads scripts instead of a first line that can actually resolve things. It's why the same ticket gets closed forty times instead of once. You keep people deliberately under-skilled to keep them, and then you pay for it every single week in a queue that never drains.

The maths is not subtle. A service desk is far cheaper than a senior SRE. Every ticket the first line can genuinely close is an interruption that never reaches an expensive engineer. Teaching them isn't charity or staff development for its own sake — it's the cheapest capacity you can buy. You already employ these people. Teaching them what the tools do is the highest-return training in the building, and it shows up immediately: two or three tickets a week, gone.

And the retention worry is backwards on its own terms. People are far more likely to leave a job where they're kept ignorant and set up to fail than one that invests in them. If someone becomes brilliant and moves on, you had a brilliant person for a while and they made everything better while they were there. That is not a loss. Choosing to keep them useless so they can't leave — that's the loss, and you carry it every week the tickets keep arriving.

If your team is drowning in a repeating ticket queue: are you working the queue, or are you working the reason the queue exists — and would your organisation rather its people couldn't leave than that they knew what they were doing?

## Sources

- [IBM Aspera](https://www.ibm.com/products/aspera)
- [Puppet](https://www.puppet.com/)
- [EMBL-EBI](https://www.ebi.ac.uk/)
