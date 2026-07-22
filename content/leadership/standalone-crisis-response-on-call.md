---
title: "What chemical-industry crisis planning taught me about on-call"
date: 2026-07-19T17:50:00+01:00
tags: [leadership, operations]
---

Tech did not invent incident response. We are, at best, enthusiastic late adopters.

I was reminded of this reading a [crisis and disaster response article by Caroline Brooks](https://www.pcimag.com/articles/113441-best-practices-for-crisis-and-disaster-response) of the Alliance for Chemical Distribution, published in Paint & Coatings Industry magazine. It is written for facilities that handle hazardous chemicals — hurricanes, spills, evacuations, the lot. It is one of the pieces I kept from my leadership reading pile, and it aged better than most of the management literature next to it. Reading it as an infrastructure person was uncomfortable, because an industry that plans for actual disasters keeps reaching conclusions we in tech keep rediscovering after every messy outage.

Here is what translated, through the lens of a decade running production infrastructure at EMBL-EBI — petabyte-scale archives, thousands of users, and a pager that did not care what time it was in Cambridge.

### Plans decay faster than systems

The chemical distributors treat plan maintenance as an explicit, recurring task: whenever someone leaves or changes role, the crisis plan gets revised, and emergency contact numbers are verified during drills and audits because they silently change.

In tech we version-control everything except the thing that matters at 3am. Escalation paths quietly rot. The vendor support number is for a contract that lapsed. The "database owner" left two reorganisations ago. My rule now: an on-call rota or runbook that has not been touched in six months is presumed wrong until proven otherwise. Tie the update to the HR event, not to good intentions.

### Drills, not tabletops

The article is blunt that tabletop exercises are only "one approach", and that members are encouraged to run full-scale drills — because people do not know how they will react in an emergency until they feel a version of the stress.

This matches my experience exactly. The first time an engineer leads a real incident should not be the first time they have led any incident. The [Google SRE book's chapter on managing incidents](https://sre.google/sre-book/managing-incidents/) makes the same argument from the tech side: rehearsed roles and procedures are what keep an incident from becoming a crisis. Game days, chaos exercises, restoring the backup for real — these feel expensive right up until the day they are cheap. In one DR project I led, the uncomfortable finding was never the technology; it was that the humans had never actually executed the failover steps in anger. And the debrief matters more than the drill. A drill you do not write up and act on is a team-building day with extra steps.

### Communication fails first, and all at once

Crisis planners assume water, electricity, internet and mobile coverage may vanish together. Households, businesses and even governments may be out of commission simultaneously.

Our version of this is subtler but real. The status page hosted on the platform that is down. The incident bridge that needs SSO, when SSO is the incident. The runbook wiki that lives in the affected datacentre. At home I run a self-hosted lab precisely because I like understanding failure modes end to end, and the same lesson holds at every scale: your incident tooling must not share fate with the thing it manages. Decide your out-of-band channel before you need it.

### Know your materials

One detail I loved: they warn that safety data sheets are less helpful than people assume, because blended chemicals are not covered by the datasheet of any single ingredient.

Every infrastructure engineer has lived this. The vendor documentation describes the component; production is a blend. The failure mode that hurts you is emergent — the interaction between the storage layer, the network policy and that one cron job. Which is why institutional knowledge, captured in honest post-incident reviews, beats any amount of generic documentation.

### The cyber section reads like our day job

The piece closes with cyber preparedness: phishing, fraud, MFA, patching. When the chemical industry's crisis guidance and your CISO's newsletter converge on the same advice, the message is that security incidents are now ordinary disasters, to be drilled like fires and floods — not treated as an exotic speciality.

### The honest caveat

One thing the article cannot say, but I will: preparedness has diminishing returns and real costs. You cannot drill weekly and also ship. The leadership judgement is choosing the two or three failure scenarios that would genuinely hurt — data loss, regional outage, compromised credentials — and rehearsing those properly, rather than maintaining a thick binder that covers everything and prepares no one.

Regulation forced the chemical industry into this discipline. Nothing forces most tech teams, which is why so many discover their crisis plan's flaws during the crisis. The good news: unlike hurricanes, most of our disasters are kind enough to offer rehearsals — if we choose to schedule them.

When did your team last verify, end to end, that the escalation path actually reaches a human?

## Sources

- [Caroline Brooks, "Best Practices for Crisis and Disaster Response" — PCI Magazine](https://www.pcimag.com/articles/113441-best-practices-for-crisis-and-disaster-response)
- [Google SRE book, "Managing Incidents" — the tech-side counterpart](https://sre.google/sre-book/managing-incidents/)
