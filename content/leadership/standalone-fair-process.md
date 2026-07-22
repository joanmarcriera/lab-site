---
title: "People accept decisions they dislike, if the process was fair"
date: 2026-07-19T19:10:00+01:00
---

Some of the worst fallout I have seen in technology teams followed decisions that were, on the merits, correct. A justified migration, a sensible deprecation, a defensible on-call change — and still resentment, attrition, quiet sabotage. For years I filed this under "people dislike change". Eventually I found a sharper diagnosis: the decisions were fine; the process was unfair. And process fairness, it turns out, is a studied thing with a small, learnable structure.

### Outcome fairness is not enough

Procedural justice — fair process — is a well-established idea in [organisational research](https://en.wikipedia.org/wiki/Procedural_justice); [Kim and Mauborgne's Harvard Business Review work](https://hbr.org/2003/01/fair-process-managing-in-the-knowledge-economy) made it famous in strategy circles. The framing that helped me most is also the most practical I have met. Its starting observation: we instinctively focus on whether the outcome is fair (equal shares? by merit? by need?) and assume satisfaction follows. It does not. People judge how the decision was made at least as strongly as what was decided.

The anecdote that stuck with me: a professional appealed a budget decision, won, got everything reinstated — and came away angrier than when he started, because the people deciding were dismissive and grudging throughout. Full marks on outcome, zero on process, net negative on trust. Anyone who has "won" an argument with a vendor, a landlord or an HR department in that fashion will recognise the feeling.

### The four conditions

Fair process, boiled down, rests on four principles:

1. **Consistency.** The rules are the same for everyone and stable over time. The moment an exception appears for a favourite, the process is dead.
2. **Transparency and explanation.** The reasoning behind the decision is laid out. Not defended to exhaustion — explained.
3. **Engagement, or voice.** Affected people are genuinely heard before the decision closes. Crucially: a voice is not a vote. You are not promising democracy; you are promising to listen and be influenceable.
4. **Clear expectations.** Once decided, what happens, who does what, by when — stated plainly.

What struck me is how cheap these are. None requires consensus, committees, or delay measured in months. A migration announcement that includes "here is why, here is what we heard from the teams we consulted, here is what changed because of it, here is the timeline" costs one page of writing.

### Why leaders skip it anyway

The most honest observation I have on this: when leaders are pressed in private about why they avoid fair process, the socially acceptable answer is time pressure. The real answer, more often, is fear of losing control — the fear that engagement will reveal a subordinate had a better idea, in front of everyone.

This connects to a second idea that deserves its own frame: as a senior technical leader, you are professionally obsolete, and the rate of decay is not negotiable. The methods, tools and instincts that made you good are ageing while you sit in meetings. The people closest to the work hold more current knowledge than you do. I have heard senior researchers admit as much about themselves relative to their own postdocs, which I always found disarming. In that light, imposing solutions top-down is not just interpersonally clumsy — it actively destroys value, because your solution is drawn from a stale map. One useful way to picture innovation is as search over rugged landscapes: complex problems where the best solutions are found by specialists negotiating and wrestling with each other, not by a smart person at the top dictating coordinates. Friction between experts is a feature. Your job is to referee it fairly, not to replace it.

There is a supporting story I think about often: a highly competent factory manager who decided everything himself, correctly, for years — and produced a foreman who simply waited for instructions. Every top-down decision was locally right and globally corrosive. The organisation learned helplessness from a leader who was never wrong.

### What this looks like in platform work

Translate the four conditions into the decisions infrastructure leaders actually make:

- **Deprecating an internal service.** Voice: consult the heaviest users before the decision, and show what their input changed. Transparency: publish the reasoning, including the costs of keeping it. Expectations: dates, migration support, escalation path. Consistency: the same sunset rules for the team's own pet service as for everyone else's.
- **Changing on-call.** Nothing generates resentment faster than compensation and rota changes announced from orbit. The people carrying the pager have the most current knowledge of where the load really falls; engagement here is not politeness, it is data collection.
- **Choosing a standard.** When two teams champion different tools, a fair-process bake-off with published criteria beats a quiet decision after the meeting, even when the outcome is identical. Especially then.

My own experience backs the theory. At EMBL-EBI I spent years pushing changes — ITIL practices, shared metrics, identity system consolidation — from a position with limited formal authority. The changes that stuck were the ones where the affected teams had been genuinely heard and the rationale was written down and repeated. The ones that bounced were usually procedurally rushed, whatever their technical merit. I would not have used the phrase "procedural justice" at the time. I would now.

### The caveat

Fair process is not a euphemism for softness, and the boundary matters: voice without a vote means you still decide, and some people will still be unhappy. It also cannot launder a genuinely bad decision; explaining nonsense transparently produces well-documented nonsense. And it only works while it is believed — one inconsistent exception, one consultation whose input visibly changed nothing, and you are rebuilding from a deficit.

But as a discipline for the decisions technology leaders make weekly, I know nothing with a better effort-to-payoff ratio. Four conditions, one page of writing, and the difference between a team that carries your decision and one that merely complies with it.

What is the next unpopular decision on your desk — and could you honestly tick all four boxes before announcing it?

## Sources

- [W. Chan Kim & Renée Mauborgne, "Fair Process: Managing in the Knowledge Economy", Harvard Business Review](https://hbr.org/2003/01/fair-process-managing-in-the-knowledge-economy)
- [Procedural justice (the research tradition behind fair process)](https://en.wikipedia.org/wiki/Procedural_justice)
