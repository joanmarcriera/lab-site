---
title: "How I ran a creativity workshop for infrastructure engineers (and nobody rolled their eyes)"
date: 2026-07-19T18:10:00+01:00
---

Engineers distrust brainstorming, and they are right to. Most sessions are unstructured opinion exchanges that converge on whatever the loudest person suggested in minute three. So when I needed genuinely new ideas for a stubborn problem — identity and access management at EMBL-EBI — I did not book a "creativity session". I built a structured workshop from the classic idea-generation techniques, and told the team exactly what would happen and why.

### The problem worth a workshop

Our challenge statement was concrete: how might we eliminate the chaos and uncontrolled access around account creation, management and closure for employees, so that we reduce the overhead on HR and IT? Years of accumulated identity debt meant everyone had opinions. That was precisely the issue. When a team has lived with a problem for years, they do not lack ideas — they lack *new* ideas. Working closely together makes people think similarly. [Groupthink](https://en.wikipedia.org/wiki/Groupthink) — the term [Irving Janis](https://en.wikipedia.org/wiki/Irving_Janis) coined studying how cohesive groups talk themselves into bad decisions — is not a character flaw; it is the natural sediment of collaboration.

### The recipe

I adapted five idea-generation techniques into a workshop:

**0. Off the chest.** Before anything else, everyone dumps every idea they already have — the obvious ones, the pet ones, the ones proposed in 2019. This is not filler. People cannot think freshly while mentally guarding their existing favourite. Writing it down acknowledges it and frees the room.

**1. Re-expression.** Reframe the challenge by replacing its key terms. "Improve authentication and authorisation" became "improve identity lifecycle management for better access control". It sounds cosmetic. It is not — different words summon different mental models, and half the room starts describing onboarding flows instead of login boxes.

**2. Related world.** How have other industries solved this? Banking runs secure identity verification at massive scale. Healthcare grants privacy-sensitive access to critical data under regulatory pressure we can only imagine. Neither considers identity an unsolved problem. That observation alone recalibrates ambition.

**3. Regeneration.** How does nature solve it? Bees organise hive access through specific signals. Wolves do not expand territory; the pack simply moves. Yes, this round gets laughs. The laughs are the point — absurdity switches off the internal reviewer that kills half-formed ideas. And "access based on signals rather than stored lists" is not a bad seed for a capability-based access model.

**4. Revolution.** Break all the rules. What if there were no centralised user management at all? What would decentralised authentication look like? You will probably not ship the revolutionary answer. But it marks the edge of the possibility space, and everything inside it suddenly looks less radical.

### Facilitation choices that made it work

• **Start with off-the-chest, then choose only two of the remaining techniques.** Five full rounds would flatten the room. The techniques are a menu; the facilitator's job is portion control.
• **One person takes notes; everyone else sends theirs RAW.** I asked the team to dump notes into Slack or email and send them unedited — "no filters, please". Polished submissions are censored submissions. The novelty lives in the half-sentences.
• **Filter afterwards, visibly, on three axes:** feasibility (can we implement it within current systems?), novelty (is it actually new?), and impact (will it move security and usability?). Engineers accept idea-filtering when the criteria are stated before the filtering starts.
• **Articulate one solution properly at the end** — next steps and stakeholders included. A workshop that ends with a wall of sticky notes and no owner is a team-building exercise pretending to be work.

### The companion tool: journey mapping the sad paths

A second workshop applied a different lens to the same domain: a customer journey map for IAM. We mapped the happy path for common scenarios — a new researcher joins and needs access; a staff member changes roles; a password reset — and then spent the session hunting *sad paths*: delays, confusing interfaces, unclear policies, dead ends.

The prioritisation was deliberately unsophisticated: frequency, severity, cost to fix. Rank, pick, act. The output was a visual of where identity actually hurts our users, which turned out to be far more persuasive with stakeholders than any architecture diagram I have produced. A prioritised list of user pain beats a prioritised list of technical debt in every funding conversation. Same backlog, different language, different result.

### What I would tell a sceptical engineering lead

Structured creativity is not about believing bees will design your IAM system. It is about the statistics of idea generation: the first ideas out of any experienced team are the ideas they have already had. The techniques exist to force the second and third wave out, cheaply, in ninety minutes. The scaffolding was borrowed; the team supplied ideas none of us would have listed on day one.

[Walter Lippmann](https://en.wikipedia.org/wiki/Walter_Lippmann) was right that when all think alike, no one thinks at all — and the eye-rolling never came, for one reason: every round had a rule, a time-box, and a stated purpose. Engineers do not resist creativity. They resist vagueness.

Which technique would your team tolerate first — reframing the words, raiding another industry, or breaking all the rules?

## Sources

- [Groupthink — the concept, its symptoms and famous fiascos](https://en.wikipedia.org/wiki/Groupthink)
- [Irving Janis, the psychologist who named and studied it](https://en.wikipedia.org/wiki/Irving_Janis)
- [Walter Lippmann, source of the "when all think alike" line](https://en.wikipedia.org/wiki/Walter_Lippmann)
