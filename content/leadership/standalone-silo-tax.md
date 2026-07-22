---
title: "The silo tax: why your smartest engineers produce less than they should"
date: 2026-07-19T18:50:00+01:00
tags: [leadership]
---

Ask people how creativity is distributed across a population and you will usually get one of two answers: evenly ("everyone can be creative"), or normally ("most people are average, a few are geniuses, a few are hopeless"). Both are wrong. Measured output — patents, publications, citations, improvement suggestions on a factory floor — follows a power law: a long tail of modest contributors and a tiny number of towering outliers. This has been rediscovered often enough to earn two names, [Lotka's law](https://en.wikipedia.org/wiki/Lotka%27s_law) and [Price's law](https://en.wikipedia.org/wiki/Price%27s_law).

I met this result properly a few years ago, and my first reaction was the obvious one: fine, then the job is to find and hire the outliers. The counter-argument was the reason I am writing this. Concentrating outliers barely works — they are scarce, and a room full of them tends to compete rather than compound. The lever that actually moves the curve is the network. Put people — all of them — into rich, diverse networks of contacts and the entire distribution shifts upward. The collaborative inventor beats the lone inventor on average productivity, and even the quiet middle of the curve produces more.

The evidence I found most convincing: [research comparing the patent-collaboration networks of Silicon Valley and Boston](https://en.wikipedia.org/wiki/AnnaLee_Saxenian). Silicon Valley out-innovated Boston not on raw talent but on network structure — more diversity across domains (universities, computing, printing, pharma sharing members), more connectivity, and crucially, gatekeeper individuals who bridged otherwise separate clusters. Ideas travelled further, collided more often, and compounded.

If networks are the multiplier, then anything that fragments the network is a tax on your best people. I have paid that tax, watched it collected, and occasionally helped levy it.

### The anatomy of the tax

[Work on why collaboration fails in large organisations](https://hbr.org/2009/04/when-internal-collaboration-is-bad-for-your-company) sorts the barriers into two families, and the split is diagnostic.

The first family is won't share. Silo loyalty: each group has its own goals and metrics, so listening to outsiders feels like a distraction — or worse, a status concession. Status asymmetry makes it uglier: high-status groups neither tell nor listen. And then there is hoarding, the one nobody admits to: keeping a little expertise in reserve because being the only person who understands the backup system feels like job security. It works, too — for the individual. For the organisation it means the knowledge base develops deliberate holes, and once one person hoards visibly, everyone else learns to.

The second family is can't share. People who would happily collaborate but do not know what the other team does, cannot decode its jargon, do not know whom to ask, or lack any agreed channel for handing knowledge across. These failures are mundane — a missing directory, an unsearchable wiki, no norm about whether knowledge moves over coffee or through a ticket — and precisely because they are mundane, nobody senior owns them.

### What it looked like where I worked

At EMBL-EBI I watched teams operate in silos and duplicate each other's work — an observation that cost me nothing to make and years to sit with. Two groups would each build their own monitoring stack, their own deployment scripts, their own flavour of the same automation, each sincerely unaware or quietly dismissive of the other's. In a scientific institute the irony is sharp: the science side lives by publication and shared data, while the infrastructure side, serving that very openness, could hoard runbooks like trade secrets. "Need to know" is a security principle; applied to operational knowledge, it is just a silo with a badge.

The counter-experience that convinced me the tax is optional came from my homelab. I open sourced tooling I considered half-finished, and strangers improved it — issues, patches, better patterns from contexts I would never have encountered. Mediocre code plus a diverse network outperformed careful code plus isolation. That is the Lotka's-law lesson in miniature: I did not get smarter; my network did.

### The tax is management-addressable

The encouraging part: every one of these barriers responds to deliberate management, and mostly cheap management at that.

For the won't-share family: watch your status gradients and flatten them where you can — if one guild (research software, or platform, or data science) audibly outranks the rest, ideas will only flow downhill, and slowly. Reward visible reuse at least as loudly as invention; the engineer who adopted another team's tool saved you a project, and nobody ever thanks them. And treat hoarding as the incentive problem it is: people stop keeping aces up their sleeves when demonstrated redundancy — documented, transferred knowledge — is what earns promotion, not indispensability.

For the can't-share family: manufacture the collisions. Regular cross-team demos, internal tech talks, rotations, shared documentation standards with actual search. Appoint and honour your gatekeepers — the people who translate between clusters are doing the highest-leverage work in the network and usually get zero credit for it because it belongs to no silo's metrics. And accept some duplication of capability deliberately: a bit of overlap and autonomy in multiple places keeps idea-diversity alive. The goal is not one central committee filtering every idea — a single filter, however clever, becomes the bottleneck and eventually the groupthink.

One caveat where I part company with the sunnier reading: openness has real costs. Security, compliance and plain focus sometimes genuinely require walls, and a leader's job is to price each wall honestly rather than pretend all barriers are pathologies. The failure mode I am arguing against is not the existence of walls; it is walls nobody decided to build, collecting a tax nobody measures, from exactly the people whose output you can least afford to halve.

Your organisation almost certainly knows more than it thinks it knows. The question is whether the knowledge can travel.

## Sources

- [Lotka's law (the productivity power law)](https://en.wikipedia.org/wiki/Lotka%27s_law)
- [Price's law (Derek de Solla Price's square-root version)](https://en.wikipedia.org/wiki/Price%27s_law)
- [AnnaLee Saxenian, "Regional Advantage", on Silicon Valley vs Route 128 network structure](https://en.wikipedia.org/wiki/AnnaLee_Saxenian)
- [Morten Hansen, "When Internal Collaboration Is Bad for Your Company", Harvard Business Review](https://hbr.org/2009/04/when-internal-collaboration-is-bad-for-your-company)
