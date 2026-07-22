---
title: "Nobody owns all of innovation — not even the CTO"
date: 2026-07-19T22:00:00+01:00
series: "CTO programme · 1/10"
---

The title "CTO" tells you almost nothing about what the person does. It took me two decades in infrastructure — consultancy, HPC, then leading IT services at [EMBL-EBI](https://www.ebi.ac.uk/about) — to see how much that matters, and it reframed how I think about my own scope.

### The same title, five different jobs

In a startup, the CTO is often the technical founder pushing one technology to the point where a business can grow on it. In a multi-product company, the CTO might run product development, or long-term research, or both. In a multinational, the CTO may run a corporate lab that serves many business units. And in service companies, the CTO is frequently the head of IT and process development, because IT effectively is the operations of the business.

None of these is the "real" CTO job. They are different jobs wearing the same badge. The consequence, which keeps proving itself: very few CTOs own all of innovation. Continuous improvement often sits with operations. Business model changes sit with the executive team. Product ideas may arrive through acquisition. The CTO who believes the org chart implies otherwise is heading for a collision.

One case made this vivid for me: an Indian IT services firm that built its product line almost entirely through M&A. The CTO's actual remit was software process maturity, making acquired products compatible, and limiting the customisations that salespeople promised to customers. When I describe this to other engineers, they bristle: it offends their pride. But the positioning was deliberate and coherent. The strategic role existed; it just wasn't the role people imagine when they hear "CTO". As long as the scope is explicit and agreed, everyone can do a good job.

### Strategy is the "how", and most people skip it

Underneath this sits a working definition of strategy that I now use constantly. Strategy is not where you want to be. It is how you intend to get there, given where you actually are. Objectives dressed up as strategy — "we will be the most innovative company in our sector" — are just wishes. A strategy has to name the trade-offs, admit the weaknesses, and hang together as a story people can follow. [Richard Rumelt](https://en.wikipedia.org/wiki/Richard_Rumelt)'s [Good Strategy/Bad Strategy](https://www.penguinrandomhouse.com/books/207137/good-strategy-bad-strategy-by-richard-rumelt/) covers this ground better than anything else I have read, and is worth your time.

That sounds abstract until you apply it to your own scope. The exercise I recommend: answer, in writing, what your organisation provides, to whom, how, why you rather than a competitor, and what happens if the environment shifts. Five questions. One page. Harder than it looks.

### Doing the exercise on my own job

I ran the exercise against my role at EMBL-EBI, where I coordinated service and data management infrastructure. Writing it down forced precision I had been avoiding:

- We ran an in-house software-defined object storage backend for scientific archives above 100PB — essentially a self-hosted S3, cheaper than public cloud at that scale, hiding hardware lifecycles so that data URLs from the 1990s still resolve today. That last property quietly supports peer review of decades-old papers.
- We ran the transfer services moving roughly 4PB of data in and out per month.
- We ran identity management for over 50,000 accounts across internal and external collaborators.

Three products. All of it process and platform innovation. None of it product invention, none of it research. My core strategic priority for years had been reducing technical debt — making services stable, predictable and cheap to maintain.

Two things fell out of the exercise. First, relief: I stopped judging my work against a fantasy job description. Platform work is a strategic role, the same way that CTO-as-customisation-police was a strategic role in the case above. Second, a gap became visible: I could describe my stepping stones precisely, but the milestone they were stepping towards was never clearly articulated at the organisational level. Institutional strategy focused on the research mission without saying much about how technology should deliver it. You cannot align to a target that hasn't been named. Spotting that gap — and being able to say it in strategy language rather than as an engineer's complaint — was worth the whole exercise on its own.

A small, telling outcome: doing it made me discover my organisation had a strategy department. I had worked there for years without knowing. I emailed them.

### Why clarity of scope compounds

My argument, tested against my own experience, is that clarity about your innovation scope pays in three currencies:

- **Accountability.** You can be measured on what you actually own, not on vibes.
- **Collaboration.** Once you know which innovation happens elsewhere, you can work with those owners instead of silently competing with them.
- **Resources.** The clearer the story of the value your activities create, the easier it is to defend budget. Vague scope gets vague funding.

There is a caveat worth stating. On paper this is a tidy analytical exercise. In real organisations, scope is contested, historical, and political. Some of the ambiguity is load-bearing: people benefit from it. Writing your scope down will surface disagreements that were comfortably buried. That is the point, but do not expect applause.

If you lead technology at any level — you do not need the C-title — take thirty minutes this week. List the types of innovation your organisation does: offerings, processes, delivery, business model. Mark which are developed, which are bought, which are ignored. Then circle what is yours. The circles are usually smaller than your job title implies, and far more defensible.

## Sources

- [Richard Rumelt, Good Strategy/Bad Strategy](https://www.penguinrandomhouse.com/books/207137/good-strategy-bad-strategy-by-richard-rumelt/)
- [Richard Rumelt](https://en.wikipedia.org/wiki/Richard_Rumelt)
- [EMBL-EBI, where I ran infrastructure services](https://www.ebi.ac.uk/about)
