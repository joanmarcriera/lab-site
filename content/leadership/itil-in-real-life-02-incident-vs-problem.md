---
title: "Incidents get you praised. Problems get you peace."
date: 2026-07-19T19:30:00+01:00
series: "ITIL in real life · 2/3"
tags: [operations, leadership]
---

If one distinction from ITIL 4 earns its place on a whiteboard, it is this: incidents are about restoring service, problems are about removing causes. Confuse the two and you will be busy forever and better never.

Some context for why I care. I ran infrastructure services at EMBL-EBI, including identity and the joiners-movers-leavers (JML) lifecycle, through the rollout of a new HR system feeding our accounts pipeline. And I run a homelab with enough real storage and real users, my family, that failures are not hypothetical.

### Two clocks

Incident management runs on a fast clock. A service is degraded, someone is blocked, and the only question that matters is how quickly you can restore it. Workarounds are legitimate. Elegance is optional. The definition of done is "the user is working again".

Problem management runs on a slow clock. It asks why the incidents happen, finds the error underneath, and either removes it or consciously documents a workaround. The definition of done is "this class of incident stops occurring", which might take a quarter and three teams.

The trap is cultural, not conceptual. Incident response is visible and dramatic; it produces grateful users and impressive response-time stats. Problem work is invisible when it succeeds, because success looks like nothing happening. Left to natural incentives, every organisation over-invests in firefighting and under-invests in fire prevention. I have not seen an exception, including teams I led.

### A real one: the accounts that would not work

During the HR integration at EBI, a steady stream of new starters could not log in. Each case looked slightly different: a temporary password that had been overwritten, an onboarding email pointing at the wrong credentials, an account locked for no visible reason. The service desk handled each one competently. The stream did not slow.

Treated as incidents, these were dozens of unrelated annoyances. Treated as a problem, they had one sentence at the bottom: people were being hired into the system with start dates in the past. Every automated step that assumed "onboarding happens before day one" fired retrospectively, out of order, or not at all. The onboarding email was correct for the process as designed and wrong for the process as lived.

Three things turned it around, and none of them were faster ticket handling:

**A single issue log.** We kept every occurrence in one shared integration issue log rather than scattered tickets. Patterns you can see are patterns you can argue budget for. This is the unglamorous core of problem management: aggregation.

**Naming the cause without blame.** "The root issue is hiring with past dates" is a process fact, not an accusation. Once it was written down, HR, the HR-systems team and IT could work on the same object instead of lobbing tickets at each other. We fixed templates, clarified which attributes each JML step actually required, and agreed what could not be automated at all while data quality was still poor.

**Accepting a documented workaround.** Some of it we could not fix quickly; account locking, for instance, could not be safely automated on bad data. ITIL is refreshingly honest here: a known error with a deliberate workaround is a legitimate state, as long as it is a decision and not an accident. We chose to keep a manual step, wrote down why, and revisited it when the data improved.

None of that shortened any individual incident. It made most of them stop existing.

### The homelab test

Small systems teach the same lesson with less politics. When my TrueNAS box emails me about a degraded pool, that is an incident: swap the disk, resilver, verify, back to bed. When I noticed I had replaced several disks across the fleet in a year, that was a problem, and the honest response was a redesign, rebalancing pools and rebuilding with better redundancy, rather than congratulating myself on how quick I had become at resilvering.

The tell is pride. If you are getting proud of how good you are at handling a certain failure, you have probably stopped asking why it keeps happening.

### Where ITIL oversells it

A caveat the tidy framework tends to soften: not every problem deserves an investigation. Root-cause work costs senior engineering time, which is your scarcest resource. A recurring incident that costs ten minutes a month does not justify a two-week hunt. The discipline I do endorse is prioritising by value and risk; applied here, it means keeping an explicit, ranked problem list and being comfortable saying "known, accepted, not worth fixing" out loud. An accepted problem written down is management. The same problem unwritten is negligence with better manners.

There is also a [DevOps-flavoured criticism](https://dl.acm.org/doi/10.1145/3372114) that the incident/problem split creates hand-offs and silos. Fair, if you staff separate teams for each. In a small infrastructure group, the split is temporal, not organisational: the same engineer restores service today and investigates cause on Thursday. What matters is protecting Thursday.

### For the infrastructure lead

Count repeat incidents, not just resolution times; the repeat rate is the number that indicts you. Keep one issue log per suspected problem, however scrappy. Name causes in neutral, process language so other departments can join you rather than defend themselves. Budget problem work explicitly, because it will never win a fair fight against a live outage. And when a problem is not worth fixing, say so in writing.

Praise the firefighters. Promote the people who make the fires stop.

What is the oldest recurring incident in your queue, and does anyone own it as a problem?

## Sources

- [ITIL incident and problem management (framework overview)](https://en.wikipedia.org/wiki/ITIL)
- [Galup, Dattero & Quan, "What Do Agile, Lean, and ITIL Mean to DevOps?", Communications of the ACM, 2020](https://dl.acm.org/doi/10.1145/3372114)
