---
title: "The leader who answers every question becomes the bottleneck"
date: 2026-07-19T21:10:00+01:00
tags: [leadership]
---

The most dangerous sentence in my vocabulary as an infrastructure leader was: "Just do it like this."

It was dangerous because it was usually pretty good advice. I had built the systems my teams now ran. I had opinions about storage layouts, identity plumbing and failover design that were earned the hard way. And that is exactly the trap. It took me years of leading engineers — many of them former peers — to see it clearly.

### Innovation is search, and the landscape is rugged

The framing I find most useful is borrowed from evolutionary biology: solving a hard technical or organisational problem is a search across a [fitness landscape](https://en.wikipedia.org/wiki/Fitness_landscape) with an absurd number of dimensions. Even a mundane product involves dozens of interacting design choices. The landscape is rugged: full of local peaks that look good from where you stand, with better peaks hidden behind valleys. You cannot climb it by incremental optimisation from one starting point, and no single person's head holds the whole terrain.

That is a physics argument against the heroic leader. It is not that your answer is bad. It is that your answer is one probe into a space that needs many probes. When the boss's probe is declared the answer, all other probes stop.

### The double damage of imposed solutions

A leader who imposes solutions damages the organisation twice.

First, they extinguish the search. People learn quickly that proposing is pointless, and settle into waiting. A team lead once described his role to me, in effect, as waiting for instructions — and I have learned to hear that sentence as an indictment of the leader, not the team. Second, and more subtly, the organisation becomes hostage to the leader's decaying expertise. I will say it plainly about myself: I am methodologically obsolescing. My hands-on knowledge peaked when I still carried a pager for the systems I designed. Since then, every technology cycle widens the gap between my instincts and the current state of the art. An organisation wired to my instincts inherits my staleness.

Authoritarian decision-making does have one genuine advantage: speed. If the building is on fire, command and control is correct. The mistake is running the whole organisation in fire-drill mode. You get fast, confident marches to mediocre peaks.

### Overlap, wrestling, and leading former peers

The alternative is not abdication. It is designing productive friction: give people overlapping responsibilities around the hard problem and let them negotiate over the joint territory. The overlap forces knowledge to collide; the wrestling is where better solutions come from. The canonical example is [Watson and Crick](https://www.nature.com/articles/171737a0), who famously refused to partition the DNA problem — each worked on all of it, criticising the other freely.

This lands differently when you have led former peers, as I have. The instinct is to prove you still deserve the technical crown — to win the design review. Resist it. Your ex-peers know the current systems better than you now do; that is not a threat, it is the point. What they need from you is the frame (what problem, what constraints, what "good" means), protection of the search space, and a decision when the wrestling has run its course. Fair process — voice, not vote — covers the decision part; I wrote about that separately. The identity shift is accepting that your value moved from having answers to hosting the argument that produces them.

### The evidence: frontlines beat masterplans

What separates this from management poetry is the evidence. My favourite public case is [BMW's experiment at its Dingolfing plant](https://hbr.org/2010/03/the-globe-how-bmw-is-defusing-the-demographic-time-bomb), documented in Harvard Business Review. In 2007 the plant projected that by 2017 its workforce would be dramatically older, with obvious productivity implications, and headquarters had no answer. Instead of imposing one, the plant built a pilot production line staffed to match the 2017 age profile and asked the workers themselves to propose modifications. Dozens of small, unglamorous fixes — flooring, footwear, seating, screen magnification, rotation patterns — accumulated. Within months the pilot line matched the young line's productivity, and the solutions spread to other plants. The experts on ageing knees were the people with ageing knees.

[Amazon's restructuring into small autonomous "two-pizza" teams](https://aws.amazon.com/executive-insights/content/amazon-two-pizza-team/) points the same way: when coordination overheads strangled innovation, the answer was not better coordination from the centre but removing the need for it — small teams, clean interfaces, authority pushed down. Different industry, same physics of search.

I saw the domestic version at EMBL-EBI. Every durable improvement I can credit myself with came from framing a problem and getting out of the way; my monuments to "just do it like this" mostly needed rework within two years. The frontline knew things about the workload that no architecture diagram captured.

### What I actually changed

Three habits I have adopted.

First, I answer questions with constraints instead of solutions where I can: here is the budget, the deadline, the compliance line we cannot cross — bring me two options. Second, I deliberately assign overlapping ownership on genuinely hard problems, and I tell people the overlap is intentional, so the friction is understood as design rather than politics. Third, when I do impose — and sometimes you must — I say so explicitly and time-box it, so nobody mistakes the exception for the operating model.

One caveat the tidy version of this argument under-plays: wrestling has a cost. Overlap without a decision deadline degenerates into a standing argument, and senior engineers are world-class at standing arguments. The leader still owns convergence. Search wide, then decide once, out loud.

Your expertise got you the role. Spending it down answer by answer is the one way to guarantee it is the last role it gets you.

## Sources

- [Fitness landscapes — why hard problems are "rugged"](https://en.wikipedia.org/wiki/Fitness_landscape)
- [Watson & Crick's 1953 DNA structure paper (two people, one undivided problem)](https://www.nature.com/articles/171737a0)
- [How BMW is defusing the demographic time bomb (Harvard Business Review, 2010)](https://hbr.org/2010/03/the-globe-how-bmw-is-defusing-the-demographic-time-bomb)
- [Amazon's two-pizza teams](https://aws.amazon.com/executive-insights/content/amazon-two-pizza-team/)
