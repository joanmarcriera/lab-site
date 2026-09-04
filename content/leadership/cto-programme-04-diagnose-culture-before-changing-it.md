---
title: "Diagnose the culture before you try to change it"
date: 2026-07-19T21:30:00+01:00
tags: [leadership]
---

For years I carried around a puzzle about the large publicly funded research institute where I ran infrastructure: nearly everyone left before a fixed-term limit. Brilliant people, world-class science, genuinely pleasant campus — and still, a steady conveyor belt out of the door. What I only later appreciated is that this is not drift. It is design. Some research organisations build regular staff turnover into policy — a fixed-term staff rule intended to keep trained people circulating back into the wider research community.

I also knew a second fact that I never connected to the first: annual pay rises were largely uniform — a common feature of public-sector pay scales — whether you had carried a datacentre migration on your back or quietly coasted. I was probably a bit naive about how corrosive that is. If effort and reward are decoupled, disengagement is not a character flaw. It is the rational response. The interesting question is not "why do people leave" — the institution answers that by design. The interesting question is what that design, combined with flat rewards, teaches the people who stay.

Reading [Edgar Schein](https://en.wikipedia.org/wiki/Edgar_Schein) finally gave me the vocabulary for what I had been observing.

### Culture is a loop, not a poster

Schein's frame: organisations have visible artifacts and practices on the surface, and shared beliefs and assumptions underneath. The bit most leaders skip is that the two form a loop. Practices express beliefs; beliefs are constantly re-confirmed by practices. Give everyone the same rise regardless of contribution, and you are not merely running a compensation policy. You are teaching, year after year, the belief that individual effort is invisible. Then you wonder why your best engineers update their CVs.

The second lesson: artifacts are easy to misread. A leadership team can preach collaboration in every all-hands while running processes that quietly rank individuals against each other. People believe the process, not the speech. In my world the equivalent was announcing "we are a service organisation" while the actual daily practice was responding fastest to whoever sat closest — the colleagues and friends in our own buildings — rather than the scientists across all sites who depended on us equally. The practice was the culture. The announcement was noise.

### The institute that science built

The institute's culture made perfect sense historically. It was set up by scientists to serve science, with public funding, and it inherited the norms of academia: autonomy, rigour, peer credibility, suspicion of anything that smells of corporate management. Funding arrived on multi-year cycles, and the organisation's value to the world was, by any reasonable estimate, many multiples of its cost. With a ratio that flattering, internal service metrics were never going to be anyone's first priority — mine included, for longer than I would like to admit.

The result, on the ground, will be familiar to anyone who has run infrastructure in academia, and I was part of it: legacy systems I defended past their sensible retirement date; teams, mine among them, rebuilding tooling that already existed two corridors away; plenty of training but no feedback loop telling any of us which technical skills the organisation would need in five years. None of this was malice. It was a culture doing exactly what cultures do — reproducing itself.

### Repurpose before you replace

Here is the reframe I now consider the most practically useful: stop treating the existing culture purely as the obstacle. Ask what parts of it you can point at the new goal.

A scientific institute's culture contains enormous assets for anyone trying to build a modern service organisation. Rigour maps beautifully onto [SLOs and error budgets](https://sre.google/sre-book/embracing-risk/). Peer review maps onto blameless postmortems and design reviews. Autonomy maps onto empowered on-call teams. The move is not "stop being academics, start being a service desk". The move is "let us apply the same standards of evidence to our own services that you apply to your science". The first framing triggers the immune system. The second recruits it.

That is also why my original prescription — IT needs to grow up and behave like a service provider — was correct as a destination and useless as a plan. You cannot install a belief. You can only install practices: publish service metrics, review them publicly, tie recognition to outcomes, set retirement dates for legacy systems and hold them. Beliefs follow practices with a lag measured in years.

### Where the frameworks oversell

Two caveats, because the textbooks are sunnier than reality.

First, cultural inertia is stronger than any framework makes it look. A decades-old organisation has decades of evidence that it can safely ignore the new initiative, because it has outlived every previous one. Expect the culture to defend itself, politely and indefinitely.

Second, some things genuinely are structural, not cultural. Flat pay rises were partly a constraint of public-sector pay scales, not just a belief; the fixed-term staff rule is likewise institutional design, not cultural drift. Diagnosis matters precisely because the remedy differs: beliefs respond to changed practices; structures respond to negotiation with whoever owns the structure. Confuse the two and you will spend years running culture workshops against a rule that sits well above anyone in the building.

The diversity side of that same structure, by the way, was a genuine strength — international hiring gave us teams most companies could only dream of. Honest diagnosis means writing down what the culture gets right, too, or nobody will believe the rest of your assessment.

If you lead a technical organisation, do the diagnosis before the surgery. List the five practices people actually experience — how rewards land, whose tickets get answered first, what happens when someone admits a mistake. Then write down the belief each practice teaches. That one-page exercise told me more about my institute than any engagement survey ever did.

## Sources

- [Edgar Schein, whose layers model underpins the practices/beliefs loop](https://en.wikipedia.org/wiki/Edgar_Schein)
- [Google SRE on SLOs and error budgets, the "rigour as service craft" toolkit](https://sre.google/sre-book/embracing-risk/)
