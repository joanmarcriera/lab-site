---
title: "Your project portfolio is not a stock portfolio"
date: 2026-07-19T21:40:00+01:00
series: "CTO programme · 3/10"
---

The word "portfolio" does a lot of damage in technology organisations. It arrives carrying financial baggage: diversification, risk-return optimisation, maximising yield. Dismantling exactly that framing changed how I look at roadmap decisions more than anything else in my years of running infrastructure.

### The false friend

A financial portfolio exists to maximise returns for a chosen risk profile. An innovation portfolio exists to execute your strategy. Those are different objectives, and importing the tools of the first into the second produces confident-looking nonsense.

Consider what goes into a project [NPV](https://en.wikipedia.org/wiki/Net_present_value): costs, a discount rate, and projected value. Of these, only cost is knowable. There is no market trading your internal projects, so the discount rate is a convention; the value projection is a hope. Nobody audits either. The consequence: the flexibility of the numbers invites manipulation on one side and suspicion on the other. Project sponsors learn to use the optimistic end of every range. Reviewers learn to distrust everything. And because a six-month projection is inherently more credible than a five-year one, financial gatekeeping systematically starves long-horizon work. You end up short-sighted by arithmetic rather than by intent.

Multi-criteria scoring models — weighted attributes, one-to-five scales, strategic-fit columns — do not escape the trap. They evaluate projects in isolation when real projects depend on each other. Publishing the criteria invites gaming; smart people always beat the system. And a "4 out of 5 on strategic fit" means different things to different scorers, so the apparent precision hides genuine disagreement instead of resolving it.

Even in pharma, where the modelling discipline is as strong as anywhere, [AstraZeneca's published post-mortem of its 2005–2010 pipeline](https://www.nature.com/articles/nrd4309) concluded that volume-based goals had pushed the portfolio towards quantity over quality — and proposed the 5R framework, which is at heart a set of strategy-derived questions, not a spreadsheet. If they cannot forecast value reliably with their budgets, your platform team's spreadsheet is not going to manage it either.

### Bubble charts: useful, then quietly harmful

The standard alternative is the bubble chart: risk versus return, product change versus process change, ring fences and quadrants. These deserve a fair hearing. They dimensionalise a messy problem and give a leadership team something concrete to argue over. That is genuine value — the chart as conversation scaffold.

The failure mode is subtler: the standard charts embody someone else's trade-offs. If your strategy hinges on, say, cracking three specific application markets while keeping a base platform alive, then "process vs product novelty" is a peripheral lens. Use it anyway and you are shoehorning your strategy into a consultant's template. A comparison I studied of three solar companies — identical technology domains, different strategies — made the point well: the right portfolio categories for each company came from its own strategic goals, and none matched a generic diagram.

### Buckets first, finance second

The constructive proposal is almost embarrassingly simple:

1. The leadership team — CTO included, not consulted afterwards — agrees the strategic goals.
2. Define portfolio buckets that correspond to those goals.
3. Fill buckets with candidates from both directions: top-down wishes and bottom-up proposals from the people with the expertise.
4. A project that supports no bucket is out, regardless of its business case.
5. Now apply the professional checks — financial solidity, risk balance, consensus — to catch duds. As a filter, not as the selector.

The order matters. Numbers scrutinise the portfolio; they must not shape it. And the approach has a cost worth being honest about: it demands real time from senior people, arguing until they share one view. A scoring formula you can throw over the wall is cheaper. It is also how you fund a pile of individually justified projects that add up to no strategy — the numerical version of what [Richard Rumelt](https://www.penguinrandomhouse.com/books/207137/good-strategy-bad-strategy-by-richard-rumelt/) calls bad strategy: uncoordinated actions dressed up as a plan.

One practical corollary I found valuable: prioritisation is incomplete until it is explained. When a programme gets deprioritised, the people inside the sponsoring unit usually understand why. The supporting teams — in my world the storage, network and identity teams — just see a top priority vanish and conclude leadership is erratic. The discipline of equipping every affected leader to explain the rationale is unglamorous and pays for itself in trust.

### Fewer things, better chosen

The line I have repeated most since forming this view: doing ten times more does not yield ten times the output. Working on fewer things of higher quality does. In infrastructure terms: a roadmap with thirty parallel initiatives is not a portfolio, it is a queue with delusions. My own version of this at EMBL-EBI was learning that the hardest portfolio decisions were never about killing obviously bad ideas — those die on their own — but about slowing down good ones because they served no current goal. That is painful precisely because the idea deserves to exist. It just doesn't deserve your team's next quarter.

A caveat: "wrestle it out as a leadership team" assumes a leadership team capable of wrestling productively. Where decision-making is committee-driven and risk-averse — a culture I have worked in — the buckets process can degenerate into the same horse-trading with nicer diagrams. The method is sound; it does not replace the courage it requires. Optimisation is an elusive concept under high uncertainty anyway. Covering your strategic goals with a reasonable collection of projects is not settling for less. It is the actual job.

Next time your project list is being ranked by a spreadsheet, try asking one question first: which strategic goal does each row serve? Rows with no answer are the interesting ones.

Which project in your current portfolio would survive the buckets test — and which one is only alive because its spreadsheet is well written?

## Sources

- [AstraZeneca's published 5R analysis of its own pipeline (Cook et al., Nature Reviews Drug Discovery)](https://www.nature.com/articles/nrd4309)
- [Net present value, and what goes into it](https://en.wikipedia.org/wiki/Net_present_value)
- [Richard Rumelt, Good Strategy/Bad Strategy](https://www.penguinrandomhouse.com/books/207137/good-strategy-bad-strategy-by-richard-rumelt/)
