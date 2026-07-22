---
title: "Closing the same ticket forty times is not service"
date: 2026-07-20
tags: [operations]
aliases: ["/war-stories/closing-the-same-ticket-forty-times/"]
---

We ran a world-class institute on a ticketing system nobody could report on. That was just silly, and I tried to retire it.

Here's the failure that convinced me. If you close the same ticket forty times, you have not provided service forty times. You've failed to fix something forty times and called it work. But the old system couldn't show you that, because it couldn't answer the questions that would have exposed it.

Three questions, specifically, that I could not answer with the old tool:

• **How many tickets were raised for the same reason?** If the answer is "forty," you don't have forty incidents. You have one problem and thirty-nine symptoms, and every close is a small lie you're telling yourself about being productive.

• **How many tickets were raised by the same person?** A single frustrated user hitting the same wall over and over looks, in a bad system, like healthy demand. It isn't. It's one unmet need wearing forty costumes.

• **How many tickets were raised in different queues by the same team?** This is the one that hides the most. A team splits its pain across half a dozen queues and no single queue owner ever sees the shape of it. The problem is real and large; the data makes it look like scattered noise.

You cannot manage what you cannot see, and we couldn't see any of it. A migration to a system that could actually report was worth it for that reason alone — not because reporting is nice, but because reporting is the difference between fixing a problem and re-closing it forever.

Now, ITIL. To hands-on engineers in a science institute, "ITIL" sounds corporate, and that was exactly my problem selling it. So I stopped selling the word.

It's just service management. You need service management because you manage services — that's the whole argument. ITIL is a proven framework, and a framework is not a cage. You adapt it. You do not implement it to the very bottom, and you do not need to. You find your biggest pain point and you start there.

And I did not start from the ticket system. I started from the pain that actually frightened the people holding the budget.

We were losing about 10% of our people every year — and it was the people who had stayed the longest. The deepest knowledge in the building was walking out of the door on a steady annual schedule, and most of it lived in nobody's documentation. That is a knowledge-management problem before it is anything else, and service management is how you attack it. Funnel the work through a service desk. Put a metric on it — for example, how many processes the service desk has automated away. The more, the better. Every automated resolution is a piece of knowledge captured once and reused forever, instead of leaving with the next long-tenured person who retires.

Then the economics, because this is what makes it land with management. A service desk is far cheaper than senior SREs or senior managers. When everybody is doing tickets at all times — and in the old world, everybody was — nobody can drive a project that needs sustained concentration. Put people on a service desk to absorb the funnel, and you buy back the expensive people's attention. You relieve your senior engineers' time by spending junior time deliberately. That's not a cost. That's the cheapest capacity trade in the building.

I'll be honest about what didn't work, because the honest part is the useful part.

I went and got myself ITIL certified, thinking it would give the argument weight. It bought me exactly zero internal credibility. They really didn't care. A certificate on my side of the table changed nobody's mind, because credibility in a science institute is earned by fixing their actual problems, not by naming the framework you used to do it.

And the buy-in never fully arrived. I pushed service management from the very beginning, and I'm not sure they've bought it even now. It stayed a thing the operations team did, rather than a thing the institute believed. I'd still make every one of these arguments again — the reporting, the pain-first sell, the service desk as knowledge capture — because they're right. But I'd tell any leader trying the same thing: your certification is for you, not for them. Lead with their biggest pain, in their own words, and never once say the word "ITIL" if the word is what's getting in the way.

If you had to justify a service desk to people who think it's bureaucracy, what's the one pain you'd lead with — and would you dare start with the people you're quietly losing every year?

## Sources

- [ITIL (IT service management framework)](https://en.wikipedia.org/wiki/ITIL)
- [EMBL-EBI](https://www.ebi.ac.uk/)
