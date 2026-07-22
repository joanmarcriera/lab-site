---
title: "You can't copy a culture, only its furniture"
date: 2026-07-19T19:00:00+01:00
tags: [leadership]
---

Every few years a company becomes the one to imitate. Toyota, then Google, then Spotify, then Netflix. Playbooks circulate; rituals get adopted; org charts are redrawn to match a conference talk. The results are reliably disappointing, and I eventually landed on a satisfying explanation of why — one that starts unusually far from management literature.

### Imitation is the engine, and the bug

Comparative research on cognition — the [Herrmann et al. study published in Science in 2007](https://www.science.org/doi/10.1126/science.1146282) is the reference — tested human toddlers against chimpanzees and orangutans across spatial reasoning, counting, causality. Performance was broadly similar, with one glaring exception: social learning. Human children imitate vastly better. On this account, imitation, not raw intelligence, is what compounds into cumulative culture and, eventually, civilisation. We learn almost everything we know from other people.

The definition of culture I find most useful builds on that base: socially transmitted knowledge that is no longer questioned. Not the values poster. The stuff everyone knows without knowing why they know it.

Here is the catch. Imitation runs on proxies. We copy the conforming behaviour around us; we copy people who appear successful; we copy people with prestige. What we cannot copy is the causal machinery, because it is invisible. Nobody imitates "the decade of incentive design that made this behaviour rational". They imitate the visible artefact.

Hence the anecdote I have retold most often: in Amazon's early years, other companies copied its [famous desks made of doors on trestles](https://www.aboutamazon.com/news/workplace/how-a-door-became-a-desk-and-a-symbol-of-amazon). Frugality made visible. The imitators bought the furniture and waited for the innovation. The desks were an output of a system; copying outputs does not install the system. Football-mad readers will enjoy the parallel example — kids worldwide imitating a famous striker's free-kick stance, legs planted, breathing theatrically. The stance was never the mechanism.

If that sounds quaint, replace desks with: adopting "Spotify model" squad names, minting SRE job titles without error budgets, holding blameless postmortems in a company that punishes visible failure. The tech industry is a cargo-cult machine of remarkable throughput.

### Cultures drift; nobody is steering

The more unsettling half of the argument: because imitation copies proxies, cultures can drift into dysfunction that nobody designed and nobody controls. The darkest illustration I know is a journalist's study of London investment banking after 2008 — [Joris Luyendijk's interviews](https://en.wikipedia.org/wiki/Joris_Luyendijk). The picture was not monsters or fools at the top. It was ordinary, mostly decent people locked into a culture of conformity: brutal hours, opaque firing, status competition, contempt for customers — each individually trapped by mortgages and peer expectation. The recklessness was cultural, transmitted by imitation, owned by no one.

Engineering organisations produce milder strains of the same disease. Consider the on-call hero culture. Nobody ever decides "we shall reward firefighting and neglect prevention". It emerges: an outage gets fixed at 3am, the fixer is publicly praised, promotion follows. Every engineer watching just learned what success looks like here. Quiet prevention work — the unglamorous capacity planning that means no outage happens — generates no stories and no visible heroes. Within a few cycles you have engineers who, rationally, let systems run hot. I have watched this dynamic in infrastructure teams for twenty years. It gave me the mechanism: people imitate what is rewarded and prestigious, not what is effective, because effectiveness is the invisible part.

### Practices eat pronouncements

The practical half is about how culture actually changes. In [Edgar Schein's model](https://en.wikipedia.org/wiki/Edgar_Schein), culture lives in a loop between practices (visible, daily) and beliefs (invisible, underlying). Change fails when leaders announce new beliefs while leaving contradictory practices running. A textbook example: a multinational preaching teamwork and collaboration while operating a closed-door individual ranking system. Employees are not confused by this. They correctly identify the ranking as the real culture and the slogan as decoration. The fix was not better communication; it was removing the contradicting practice.

The corollary I found most useful: you understand a culture fastest by getting it wrong. Push a change, watch what the organisation rejects, and you have located a basic assumption. Expensive, but reliable — and a good reason to run small probes before betting a transformation on your read of the room.

### What a leader can actually do

The honest answer is refreshingly modest here. You cannot decree culture. But leaders are high-visibility, high-prestige figures — precisely the people the imitation machinery locks onto. Three things follow:

- **Choose two or three values and embody them physically.** Not posters: behaviour. What you do in meetings, what you praise in public, what you tolerate. If you claim reliability matters and then ship past a red SLO to hit a date, the organisation learns the real rule instantly.
- **Audit what gets rewarded against what you claim to value.** Promotions and public praise are the strongest imitation signals you control. One promoted firefighter outweighs a year of prevention rhetoric.
- **Before copying any famous company's practice, name the mechanism.** Ask: what incentive structure makes this work there, and do we have it? If the answer is "unclear", you are buying door-desks.

A caveat on the whole area: this framing can slide into fatalism — "culture is emergent, nothing can be done". That is not the claim. The claim is that the levers are indirect: practices, rewards, and your own imitated behaviour, applied consistently for a long time. Slower than a values workshop. Considerably more real.

I keep a personal shortlist of behaviours I want cloned when people watch me work: measure before opining, write things down, say "I don't know" out loud. Modest. Also, on this evidence, most of the actual mechanism.

If your team copied only what you did last week — not what you said — what culture would they be building?

## Sources

- [Herrmann, Call, Hernández-Lloreda, Hare & Tomasello, "Humans Have Evolved Specialized Skills of Social Cognition: The Cultural Intelligence Hypothesis", Science, 2007](https://www.science.org/doi/10.1126/science.1146282)
- [Edgar Schein, whose practices/beliefs model of organisational culture sits under all of this](https://en.wikipedia.org/wiki/Edgar_Schein)
- [Joris Luyendijk, "Swimming with Sharks", on the culture of London banking](https://en.wikipedia.org/wiki/Joris_Luyendijk)
- [How a door became a desk, and a symbol of Amazon (official history)](https://www.aboutamazon.com/news/workplace/how-a-door-became-a-desk-and-a-symbol-of-amazon)
