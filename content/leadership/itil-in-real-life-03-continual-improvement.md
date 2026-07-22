---
title: "Continual improvement is a queue, not a quest"
date: 2026-07-19T19:20:00+01:00
series: "ITIL in real life · 3/3"
tags: [operations, leadership]
---

Improvement work does not fail for lack of ideas. It fails for lack of a queue.

This is the last of three pieces on the [ITIL 4](https://en.wikipedia.org/wiki/ITIL) concepts that genuinely help a working infrastructure lead. ITIL 4 weights continual improvement as heavily as anything else it covers, and for once the framework and my operational experience agree.

### What my own notes say

While studying the material, I kept scrappy logseq notes alongside my day job at EMBL-EBI. My continual improvement page boils down to four lines: [kaizen](https://en.wikipedia.org/wiki/Kaizen) means improvement in small pieces; service delivery is a series of building blocks, and improving blocks improves the whole; the model is flexible, agile or waterfall, it does not matter; and when one improvement ends, find the next, it is not the end of anything.

That last line is the whole practice. Improvement is not a project with a closing ceremony. It is a permanent, prioritised queue with a heartbeat.

### The #paydebt tag

Here is what continual improvement actually looked like in my working notes, no framework diagrams involved.

I tagged debt-paying work with #paydebt and pattern work with #currency. Under those tags: OS baselines to be redone every six months, on a schedule, because "current" is a state you maintain, not a state you reach. A Foreman upgrade that was not any baseline's fault, just keeping the platform honest, including replacing old provisioning scripts with webhooks before they failed at a worse time. A backlog-cleaning habit, going through old tickets deciding kill, keep, or do. And a steady drumbeat of retirements: an ageing password script for a submission service, a legacy one-time-password system, an internal service that had outlived its purpose, each with a ticket and a named successor arrangement.

None of this is impressive individually. Collectively it is the difference between a platform that quietly compounds and one that quietly rots. Infrastructure debt behaves like the financial kind; the interest is invisible until it isn't.

### What the ITIL model adds

If teams already improve things, why bother with ITIL's continual improvement model at all? Because ad-hoc improvement has three predictable failure modes, and the model exists to counter exactly these.

**Improvements without direction.** The model insists you start from vision and a clear picture of where you are versus where you want to be, before choosing what to fix. My #paydebt tag had no such filter; it accumulated whatever annoyed me. The model forced a better question: which of these items moves the service towards where the organisation is going? At EBI, that meant retirements tied to the strategic consolidation of transfer services scored above pet refactors. Prioritising by strategic alignment sounds like management-speak until you watch a team spend a quarter polishing something the organisation was about to switch off.

**Improvements without evidence.** The model brackets the doing with measurement: know your baseline, then check whether the improvement worked. This is where I was weakest, and I suspect most operations teams are. We upgraded, migrated, retired, and rarely went back to confirm the promised benefit had arrived. My study notes contain a small confession in the form of a to-do: "Find information about Balanced Scorecard." Measurement was the bit I had to be taught. Leading indicators, not just after-the-fact counts, are the part I now insist on: a backlog that is shrinking is evidence; a feeling that things are better is not.

**Improvements without an owner.** A register, however humble, converts "we should" into "who, by when". Mine was a notes file with tags; yours might be a Jira label. The tooling is irrelevant. The properties that matter are that it is one list, it is ranked, items have owners, and it is reviewed on a heartbeat. The ITIL model is explicitly method-agnostic, run the items as sprints or as waterfall projects as their size dictates, which removes the last excuse.

### The homelab as a discipline gym

My home fleet, three hosts, ZFS everywhere, replication between them, is where I practise the loop honestly, because no one is watching. A weekly audit checks that replication is current. Failures go on the list. Improvements come off the list one at a time: a pool rebalance here, a monitoring gap closed there, an app migrated to better storage. Small pieces. The next item is always known before the current one finishes.

If that sounds obsessive for a home network, it is also why the discipline survives at work, where the stakes argue for it and the interruptions argue against it.

### Two honest caveats

First, the model can become ritual. Seven steps, dutifully documented, wrapped around improvements nobody needed. The step most worth protecting is the first one, the why. If you cannot connect an improvement to a service outcome or a risk, it is a hobby. Hobbies are fine; just fund them as hobbies.

Second, ITIL guidance undersells stopping. Retirement is the highest-leverage improvement an infrastructure team can make, because every system you switch off pays dividends in attention forever. Yet it demos badly, nothing new exists afterwards, so it loses priority fights. As a lead, I learned to celebrate decommissions as loudly as launches. Some of my proudest work at EBI was absence.

### The queue test

You can assess a team's continual improvement in one question: show me the list. If the answer is a ranked queue with owners, recent completions, and a next item already chosen, the practice is alive, whatever it is called. If the answer is a slide from last year's strategy day, you have a quest, not a queue. Quests end. Queues compound.

When one improvement ends, find the next. It is not the end of anything.

If I asked your team to show me the list right now, what would I actually see?

## Sources

- [ITIL continual improvement (framework overview)](https://en.wikipedia.org/wiki/ITIL)
- [Kaizen — improvement in small pieces](https://en.wikipedia.org/wiki/Kaizen)
- [My weekly homelab audits and rolling fix list](https://blog.riera.co.uk)
