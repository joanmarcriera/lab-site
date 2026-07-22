---
title: "Strategy dies at the operational level (unless you cascade it)"
date: 2026-07-19T21:05:00+01:00
---

Execution is a design problem, not a willpower problem. It took me years of running IT services — and a lot of watching good strategies evaporate between the slide and the shift rota — to accept that. The turning point was when I stopped nodding along to strategy documents and started rewriting my own team's KPIs.

### The cascade, in both directions

Strategy cascading is an old idea with a bad reputation, mostly because organisations only run half of it. The top-down half is familiar: set a mission, give it a target, define the actions, repeat one level down. Done alone, this produces the classic pathology — every department dutifully maximising a local number that has nothing to do with the strategic position, or worse, actively undermining it.

The half that matters is bottom-up. The people closest to the work know the limitations and the opportunities the strategy documents missed. If the cascade does not carry that knowledge back up, you have built a megaphone, not a nervous system. This connects to fair process, which I wrote about earlier in this series: people commit to targets they helped shape, even when the targets are demanding.

There is a structural component too. Span of control, layers of reporting, centralised versus decentralised decision rights — structure drives behaviour as surely as incentives do. My shorthand: your org chart is a compiled artefact of your strategy. If the two disagree, the org chart wins.

### What you measure is what you get

The most immediately useful part of thinking about operational measures comes down to two distinctions.

First, effectiveness versus efficiency. Effectiveness is the outward view — does the outcome meet the user's need? Efficiency is the inward view — how well did we use resources getting there? Infrastructure teams love efficiency metrics because they are easy to gather. Users only ever experience effectiveness. The [balanced scorecard](https://hbr.org/1992/01/the-balanced-scorecard-measures-that-drive-performance-2) exists precisely to stop one lens crowding out the others.

Second, the [sand cone model from Ferdows and De Meyer](https://smusg.elsevierpure.com/en/publications/lasting-improvements-in-manufacturing-performance-in-search-of-a-): capabilities build in sequence — quality first, then delivery, then flexibility, then cost. You do not get to optimise cost first and buy quality later. Anyone who has inherited a "cost-optimised" platform knows how that story ends.

And underneath both sits [Goodhart's law](https://en.wikipedia.org/wiki/Goodhart%27s_law): process metrics drive behaviour, including behaviour you never intended. Measure ticket closure speed and you will get tickets closed fast — sometimes by people closing them before the problem is actually fixed. Incentives must align with the metric, the metric with the strategy, or the organisation pulls in three directions at once.

### Applying it: from reactive KPIs to proactive ones

I put all of this into a strategic plan I wrote for our leadership, about the estate I actually run at EMBL-EBI, the European Bioinformatics Institute.

Our reality was recognisable to anyone in scientific infrastructure: ITIL processes in place, monitoring spread across several tools, headline KPIs of incident resolution time and system uptime, and escalation happening through weekly meetings. Nothing broken. Everything reactive.

The plan I proposed had three moves:

1. **Centralise monitoring and open it up.** Fragmented monitoring means the Service Desk — the single point of contact for users — is the last to know. We already had the pieces: [Foreman](https://theforeman.org/), Puppet and [Checkmk](https://checkmk.com/), with PuppetDB able to act as a de facto CMDB for change management. The innovation was not new tooling; it was integrating the free tools we already ran and giving the Service Desk full visibility.

2. **Change the KPIs.** I proposed two new headline measures: internal issue detection rate (did we spot it before a user reported it?) and percentage of systems monitored centrally. The first points the team at prevention. The second keeps us honest about coverage, because a detection rate over a partial estate is a vanity number.

3. **Run the cascade as a workshop, not a memo.** Monthly reports from the Service Desk feed a recurring session where technical and operational staff review what actually happened and set priorities. The textbook name is strategy cascading with a bottom-up component. I call it an information radiator with opinions.

The call to action was deliberately unglamorous: a policy naming the standard toolchain, guidelines making the Service Desk the single point of contact, and instructions to retire the shadow monitoring stacks. Execution discipline is mostly the discipline of switching things off.

### Innovation needs more than one process

Execution machinery also has to carry innovation, and the honest headline is that stage-gate is neither villain nor saviour. It gives you risk management, structure, tracking and accountability — which is exactly why it kills anything genuinely uncertain. Radical ideas fail stage-gate reviews by definition: the evidence a gate demands does not exist yet.

The answer is a portfolio of processes. Incremental work flows through the systematic pipeline. Long-horizon research lives in its own protected space. The awkward middle — too uncertain for the pipeline, too applied for research — needs something like corporate incubation, with its own funding bucket so it is not fighting the operational budget every quarter. [Amazon's two-pizza teams](https://aws.amazon.com/executive-insights/content/amazon-two-pizza-team/) and its habit of promoting the people behind a failed product tell the cultural half of that story.

The caveat I would add from the infrastructure trenches: none of these cases show you the years of unglamorous plumbing that made autonomous teams possible. Loose coupling in the org chart requires loose coupling in the architecture first.

### What I took away

• Cascade in both directions, or do not bother. Top-down alone is theatre.
• Your metrics are your real strategy. Audit them for the behaviour they reward.
• Prefer forward-looking measures (detection, prevention) over backward-looking ones (resolution time) where you can.
• Match the process to the uncertainty of the work. One pipeline cannot serve both.
• Most execution wins come from integrating and retiring, not from buying.

Eighteen months on, "internal detection rate" remains the single most useful number I have argued for.

## Sources

- [Kaplan & Norton, "The Balanced Scorecard — Measures that Drive Performance" (HBR, 1992)](https://hbr.org/1992/01/the-balanced-scorecard-measures-that-drive-performance-2)
- [Ferdows & De Meyer, the sand cone model (Journal of Operations Management, 1990)](https://smusg.elsevierpure.com/en/publications/lasting-improvements-in-manufacturing-performance-in-search-of-a-)
- [Goodhart's law — when a measure becomes a target, it ceases to be a good measure](https://en.wikipedia.org/wiki/Goodhart%27s_law)
- [Checkmk, part of the free toolchain that carried our monitoring consolidation](https://checkmk.com/)
