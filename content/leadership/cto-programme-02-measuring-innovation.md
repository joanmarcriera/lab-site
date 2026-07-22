---
title: "Measure the work, not just the outcome"
date: 2026-07-19T21:50:00+01:00
series: "CTO programme · 2/10"
---

"You get what you measure" is the most repeated line in management. For innovation and novel technical work, it is at best half true — and the reasons collide directly with how engineering organisations actually behave. After years of running services, and of watching measurement done badly and occasionally well, this is the set of principles I keep coming back to.

### Why outcomes lie about novel work

The core claim: the link between effort and outcome in innovation is unreliable, for four reasons.

- **Time.** Innovation takes years. By the time the outcome lands, a dozen other factors have contaminated the signal.
- **Non-linearity.** Results compound from many contributions. Who "caused" the idea that emerged from a brainstorm — the person who talked most, the one with the seed, or the one who made it concrete? Unanswerable.
- **Cross-functionality.** Marketing, engineering, finance and operations all feed the result. Disentangling credit is guesswork dressed as analysis.
- **Uncertainty.** Genuinely new work fails for reasons beyond anyone's control. A good decision with the information available can still produce a bad outcome.

Poker players know this as resulting — [Annie Duke](https://en.wikipedia.org/wiki/Annie_Duke)'s term for judging the decision by the outcome. Ops people know it from incidents: sometimes flawless response, terrible day; sometimes sloppy response, lucky escape. R&D and innovation portfolios suffer the same distortion, at larger budgets.

### Three uses of measurement, and why mixing them is fatal

The sharpest distinction I know in this area: measurement serves three different masters, and they must be kept apart.

1. **Evaluation** — bonuses, promotions, careers.
2. **Operational control** — spotting surprises early enough to react.
3. **Learning** — understanding why something happened so you can correct the inputs.

Attach evaluation to a metric and people will curate what it shows — [Goodhart's law](https://en.wikipedia.org/wiki/Goodhart%27s_law) in its natural habitat. Perfectly rational behaviour on their part; catastrophic for you, because that same metric now fails at jobs two and three. You wanted an early-warning system and a learning loop. You built a theatre.

I watched a version of this at EMBL-EBI, where I ran data and infrastructure services for years. Monitoring and metrics were long considered a hobby — something enthusiasts did on the side. Sharing metrics across teams was, for a period, practically taboo. My reading, then and now: teams that withhold their metrics are rarely being shy. Opacity is a rational defence in a culture where numbers are only ever used against you. The fix is not more dashboards. The fix is separating the numbers used to steer and learn from the numbers used to judge. SRE culture reached the same conclusion by a different road: [blameless postmortems](https://sre.google/sre-book/postmortem-culture/) exist precisely so that the learning channel is not poisoned by the evaluation channel.

### Process measures: not bureaucracy, insurance

If outcomes are noisy, what do you add? Process measures. Did we align the portfolio with strategy? Did we consider a diverse enough set of options? Did we kill failing projects early, or drag them on hoping the weather would change? How resourcefully did the team respond when the plan met reality?

The instinctive objection from engineers is that process measures reward beautiful process over results. The failure mode is real: rely only on process measures and you get elegant procedure and no output. The principle is proportionality. The more novel and risky the work, the more weight process deserves, because the less the outcome tells you about the quality of the effort. For routine work, outcomes remain king.

One R&D lab I studied — inside a mining company — showed what this looks like in practice. The lab did four different kinds of work: new technology development, second-line technical support, knowledge and reputation building, and research process execution. Each got its own measures. Support work got customer-service metrics: response time, answer quality. Publications counted for the reputation function only, which calmed the operations people who feared the "geeks" would optimise for papers. Nobody carried all the metrics; each person carried the subset matching their actual work. The lesson generalises to any platform or infrastructure group: your team almost certainly does three or four distinct kinds of work. One uniform scorecard will misrepresent all of them.

### Measure the thing you actually wanted

Third principle, deceptively obvious: strategic specificity. If the innovation exists to fix conformance quality, measure quality in the market. Not ROI, not velocity, not a proxy chosen because it was easy to collect. Generic metrics imported from the professional literature measure someone else's strategy.

And for the riskiest bets, there is an approach most organisations find uncomfortable: upward rewards. We agree upfront this will probably fail, and failure carries no penalty; success against the odds makes you a hero. Used alone this breeds recklessness, so it rides alongside process measures. But without it, nobody sensible volunteers for the hard projects. They second-guess what management wants instead, which is how ambitious roadmaps quietly fill with safe bets.

### What I'd actually do on Monday

My condensed version, tested against years of running services:

- You cannot improve what you don't measure — processes as much as systems.
- Never let one metric serve evaluation and learning simultaneously. Decide each metric's job and write it down.
- Match the metric to the work: customer-service metrics for support, process metrics for novel builds, outcome metrics for routine delivery.
- If people are hiding numbers from you, the numbers are not the problem.

A fair criticism of all this: the principles are easier than the politics of introducing them. Announcing "these metrics won't be used for evaluation" is easy; being believed takes years of not breaking the promise. One violation resets the clock.

Which metric in your organisation would people stop gaming tomorrow if you credibly removed it from performance reviews?

## Sources

- [Goodhart's law](https://en.wikipedia.org/wiki/Goodhart%27s_law)
- [Annie Duke, who named "resulting" (judging decisions by outcomes)](https://en.wikipedia.org/wiki/Annie_Duke)
- [Google SRE on blameless postmortem culture](https://sre.google/sre-book/postmortem-culture/)
