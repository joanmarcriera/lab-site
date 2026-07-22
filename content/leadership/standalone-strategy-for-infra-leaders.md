---
title: "Strategy frameworks are wasted on the boardroom"
date: 2026-07-19T18:00:00+01:00
tags: [leadership]
---

Most strategy education is aimed at people who set corporate direction. Most value from it, I suspect, is captured by people who run things. I have spent years working through the strategy canon — [Porter's Five Forces](https://en.wikipedia.org/wiki/Porter%27s_five_forces_analysis), network effects, ecosystem thinking, execution — while leading infrastructure and IT services, and the recurring surprise is how directly boardroom frameworks apply to infrastructure and platform leadership, a level where nobody bothers to use them.

### Strategy is a set of choices, and infrastructure teams refuse to choose

A working definition I hold on to: strategy is an integrated set of choices that lets an organisation achieve its vision. Mission is why you exist; vision is what you want to achieve; strategy is how; tactics are the specific moves. Unremarkable — until you apply the test questions to an internal IT function. Does your strategy tell you what you are *not* going to do?

Infrastructure teams are chronically bad at this. We accumulate services the way lofts accumulate boxes: every system someone once needed, still running, still on-call, still patched. An infrastructure strategy that does not include a kill list — services we will retire, requests we will decline — is a hosting arrangement, not a strategy.

The "four Cs" make a serviceable audit for any platform organisation. Choice: what are we deliberately not doing? Clarity: does everyone understand the strategy, including the engineer deciding at 2 a.m. which system gets saved first? Commitment: does the budget match the stated priorities? Congruence: do all activities align — or does the roadmap say "cloud first" while the hiring plan says "more SAN administrators"?

### Five Forces, pointed inward

[Porter's Five Forces](https://hbr.org/2008/01/the-five-competitive-forces-that-shape-strategy) analyses industry attractiveness: rivalry, buyer power, supplier power, entry barriers, substitutes. The standard examples are Walmart and Ryanair as cost leaders. Fine. Now point the model at an internal platform team, because internal services live in a competitive market whether or not anyone says it aloud:

• **Substitutes** are shadow IT. A research group with a grant and a credit card can be running on a public cloud by Friday. Your barrier to entry protecting you is procurement policy, and policies erode.
• **Buyers** are your internal users, and they grow more powerful as they grow more knowledgeable — the same mechanism Porter describes in industries where informed buyers comparing specifications squeeze the whole market's profitability, as PC buyers did in the 1980s. Users who can benchmark your storage service against S3 pricing are informed buyers.
• **Suppliers** are the cloud vendors and enterprise software licensors. As standalone tools consolidate into a few large platforms, supplier power rises — anyone who has renewed an enterprise agreement recently has felt it. The IBM PC story carries an uncomfortable lesson: commoditise everything except the layer you control, and the profits migrate to the suppliers of the non-commoditised layer. In our industry today, that layer is increasingly the hyperscaler and the GPU vendor, not the in-house platform.
• **Cost leadership**, Porter's generic strategy, is the honest strategic position of most central IT: we exist because shared infrastructure at scale is cheaper. But cost leadership is a discipline, not a birthright — high asset utilisation, economies of scale, efficient supply chain. Walmart earned it through logistics investment. A central platform that is both more expensive *and* less pleasant than the substitutes is a differentiator without a difference, and it will lose.

### Network effects decide platform battles, including internal ones

[Network effects](https://en.wikipedia.org/wiki/Network_effect) reframe the platform wars: value grows with adoption, and everything hinges on reaching the tipping point. Apple's 1990s near-death is instructive — a strong product and famous margins, yet close to bankruptcy, because a small market share meant developers would not build for the platform.

Internal platforms obey the same law. An internal tool at low adoption is in a death spiral regardless of technical quality: few users means few integrations, means less investment, means fewer users. If you run internal products, your first strategic objective is not feature parity with commercial alternatives — it is reaching the internal tipping point where teams adopt it because other teams already have. Aggressive early onboarding, seeded integrations and loud reference customers are not marketing vanity; they are the mechanism.

### Ecosystems: nobody dominates alone

Ecosystem thinking argues that industry boundaries are dissolving and value is created by constellations of partners. For a research infrastructure provider, this is simply true rather than metaphorical: data resources, funders, member institutions, cloud providers and thousands of downstream services form an ecosystem in which no single operator controls the experience. Strategising means choosing your role in it, and knowing which relationships you are ignoring. When I mapped ours, the neglected connections were exactly where the friction lived.

### The honest caveats

Two things worth saying plainly. First, the canonical case studies — Apple, Walmart, Starbucks — are engaging but corporate; translating them to a non-profit research institute, or any organisation whose "profit" is scientific output, is left entirely as an exercise. That exercise is the actual work. Second, frameworks are lenses, not answers. The Five Forces will not tell you what to do about shadow IT. It will only stop you being surprised by it, which — in strategy as in operations — is most of the job.

The senior engineers I know make strategic choices daily: what to build, buy, retire, standardise. They just make them without the vocabulary, which means they cannot defend them upward. That, more than any framework, is what learning strategy properly fixes: it teaches infrastructure people to explain their good instincts in the language budget-holders trust.

Try the four Cs on your platform team this week: which C fails first — and what would it cost to fix?

## Sources

- [Michael Porter, "The Five Competitive Forces That Shape Strategy" (HBR, 2008)](https://hbr.org/2008/01/the-five-competitive-forces-that-shape-strategy)
- [Porter's Five Forces — overview](https://en.wikipedia.org/wiki/Porter%27s_five_forces_analysis)
- [Network effects — why platform adoption is winner-takes-most](https://en.wikipedia.org/wiki/Network_effect)
