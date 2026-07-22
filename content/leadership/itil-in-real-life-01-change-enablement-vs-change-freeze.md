---
title: "Change enablement beats the change freeze"
date: 2026-07-19T19:40:00+01:00
series: "ITIL in real life · 1/3"
---

Freezes feel safe. Mostly they just move risk around the calendar.

I'm [ITIL 4](https://en.wikipedia.org/wiki/ITIL) certified, and I spent years running infrastructure services at EMBL-EBI: identity, mail, transfer services, and the account lifecycle for a campus full of scientists. I also run a serious homelab, a three-host ZFS fleet with replication between machines, which is where I test whether an idea survives contact with 2 a.m. reality. This series is about the parts of ITIL 4 that actually earn their keep for a working infrastructure lead. Change is the right place to start.

### The freeze reflex

Every organisation I have worked with has reached, at some point, for the blanket freeze. No changes during the conference. No changes in December. No changes while the auditors are in.

I understand the instinct. A freeze is easy to announce, easy to police, and it makes leadership feel that risk has been handled. But three things happen in practice:

First, changes do not stop arriving. They queue. When the freeze lifts, you deploy a month of changes in a week, often with the people who wrote them already on to other work. You have converted a steady trickle of small risks into one large, correlated one.

Second, urgent work punches through anyway. Security patches, broken certificates, a storage array filling up. So you invent an exception process, and now the freeze is really a slower, grumpier change process with extra meetings.

Third, and worst, the freeze teaches people that change control is an obstacle to route around rather than a tool that protects them.

### What ITIL 4 actually says

ITIL 4's change enablement practice is often caricatured as CAB bureaucracy. Read properly, it argues nearly the opposite. Three ideas matter:

**Not all changes are equal.** The practice distinguishes standard changes (routine, well understood, pre-authorised), normal changes (assessed case by case), and emergency changes (expedited, reviewed after). The whole game is moving as much volume as possible into the standard category, safely. A templated user-account creation, a certificate rotation, a config change deployed through a tested pipeline: these should not wait for a committee.

**Authority belongs where the risk can be judged.** This is the point I keep coming back to about decision-making generally: put the decision at the lowest level with the competence and context to make it. Applied to change, it means the person who can read the diff and knows the blast radius approves it. A senior panel that cannot evaluate the technical content adds latency, not safety.

**Scrutiny is a scarce resource; spend it on the big stuff.** While I was at EBI, the organisation was planning genuine heavy lifting, including data-centre moves from Hinxton to new sites. That is what senior review time is for. If your change board spends its hour debating a firewall rule, the data-centre migration gets the leftovers.

One small, honest note from my own logseq journal at the time: in the middle of the operational noise I wrote, "Where do I put future changes? Like the EMPIAR storage change." That is the unglamorous foundation of the whole practice. Before you can classify or authorise anything, every planned change needs one obvious home. If your engineers do not know where a future change gets recorded, you do not have a change practice, you have folklore.

### The homelab version

Strip away the committees and the practice still holds at the scale of one person. My rule at home: before any risky storage operation, I verify that replication to my second host is current. If the disaster-recovery copy is stale, the change waits until it is not.

That is a gate, but a risk-based one. It asks "can I recover if this goes wrong?" rather than "what month is it?". It takes two minutes, it is automated, and it has saved me at least twice. Calendar freezes ask the wrong question; recovery gates ask the right one.

### Where I part company with the purists

Two caveats, from experience rather than the syllabus.

Standard changes are only safe if they are genuinely well understood. The classification is a claim about knowledge, not paperwork. When we automated parts of the account lifecycle at EBI, some steps we thought were routine turned out to depend on upstream data quality we did not control. A mislabelled standard change removes the safety net and keeps the confidence, which is the worst combination.

And there is a legitimate, narrow use for a freeze: when the organisation itself is the variable. During a cutover weekend, or the first days of a new HR system feeding your identity pipeline, freezing everything else reduces the number of moving parts while you learn. The difference is scope and duration. A one-weekend freeze around a defined event is a control. A six-week seasonal freeze is an abdication.

### What I would tell a new infrastructure lead

Make the change record cheap and the classification honest. Push volume into standard changes and audit a sample of them ruthlessly. Give change authority to the people closest to the risk, and hold them accountable for it. Save the heavyweight review for the handful of changes that can genuinely hurt the organisation. And replace every calendar freeze you can with a recovery-readiness gate.

Change enablement, done this way, is not the department of no. It is how you keep shipping when everyone else is hiding under a freeze.

Which of your current change gates could you honestly replace with an automated recovery check?

## Sources

- [ITIL (IT service management framework)](https://en.wikipedia.org/wiki/ITIL)
- [Kaizen / continuous improvement, the mindset behind standard changes](https://en.wikipedia.org/wiki/Kaizen)
- [How I run change gates in my own fleet](https://blog.riera.co.uk)
