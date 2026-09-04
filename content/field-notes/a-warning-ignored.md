---
title: "A warning ignored becomes an accepted risk"
date: 2026-07-20
tags: [leadership, operations]
aliases: ["/war-stories/a-warning-ignored/"]
---

We had already reported the problem before it became the problem. That's the whole story, really, and it's the part that gets left out of every tidy incident write-up. By the time there was a security incident to respond to, weaknesses in that part of the estate had been on the record for a while — raised, written down, and, for reasons that all looked sensible at the time, deferred.

*Everything here is historical. The gaps were closed at the time, the environment has moved on since under people doing good work, and I have no current access to it or knowledge of it.*

The weaknesses were in the identity layer — the plumbing a lot of things quietly depend on. My team had flagged them. Not once, not as a drive-by comment, but repeatedly, over a stretch of time. The reports were clear about what was wrong and what it could lead to. And then nothing much happened, because at that moment it was still theoretical. A warning about something that hasn't broken yet is the easiest thing in the world to file under "later." It costs nothing to nod at and defer. Until it costs a great deal.

I'm going to keep the incident itself deliberately vague, and I'll tell you plainly why. Publishing the anatomy of a real security event — who responded, what exactly was exposed, the specific mechanism — helps the wrong readers more than the right ones. The lesson doesn't live in the gory detail anyway. So: there was an incident, it was serious, it was in the neighbourhood of what we'd been warning about, and a lot of people spent a large amount of time cleaning it up. That's as far into it as I'll go, and it's far enough.

What I want to sit with is the before and the after, because the contrast is the entire point.

**Before**, the warnings were free to ignore. Fixing the identity problems would have meant planned work, some disruption, some budget, some inconvenience for teams that didn't feel the urgency. So it kept sliding. Every deferral looked individually reasonable. Nobody decided "let's have a breach." They just decided, again and again, that this particular fix could wait — which, added up, is the same decision wearing a more comfortable face.

And I own a share of that. I had raised the risk in the language of the people who understood it already. I had not yet translated it into a form that generated organisational action — a cost, a scenario, a decision with a name and a date on it. A warning that is technically correct and organisationally inert is only half a warning.

**After**, everything I asked for was granted. Suddenly the disruption was acceptable, the budget appeared, the work got prioritised. I put a number on the remediation — on the order of a hundred hours of work to actually close the gaps, and proper recognition for the people who'd burned themselves out doing the emergency cleanup — and senior management said yes to essentially all of it. The same request that had been "not now" for months became "whatever you need" overnight.

That swing is worth staring at, because it teaches the thing I most want people to take away:

• **A warning ignored is not neutral. It's a decision.** Choosing not to act on a known, documented risk is choosing to accept that risk. The acceptance is silent and it's rarely written down, but it's real, and it belongs to the organisation as a whole — the people who could have acted, and the people who could have made it impossible not to.
• **The cost of a fix doesn't disappear when you defer it. It moves — and it grows.** The identity work was cheaper, calmer, and entirely schedulable before. After, it came bundled with an incident, overtime, and a scramble. Same work. Much worse conditions.
• **Vindication is a terrible way to be proven right.** I'd rather have been wrong. Being the person who said "this will hurt us" and then watching it hurt us is not a win. Nobody on my team celebrated. They were exhausted, and quietly frustrated that it had taken a breach to make an old warning suddenly worth listening to.

I made sure the people who did the recovery were recognised for it, properly, because heroics that go unacknowledged are how you lose your best engineers. But recognition after the fact is a patch on a wound that a decision months earlier would have prevented.

Here's the uncomfortable symmetry I keep coming back to. When you flag a risk and it is deferred, it's natural to feel that the responsibility has passed to whoever deferred it. In a sense it has. But you're still the one who lives in the blast radius when it goes wrong, and the bill for a warning ignored never lands neatly on any one desk. Which is exactly why the job of the person raising it does not end at raising it.

So report things clearly, in writing, with the consequence spelled out in the language of the people who will decide. Not to build a file for the day you get to say "I told you so" — that day is no fun at all — but because a warning on the record, framed as a decision, is the one thing that turns a silent accepted risk back into a visible choice someone has to own.

When someone hands you a documented risk and you choose to defer it: are you deciding "not yet" — or are you quietly signing your name under "acceptable"?

## Sources

- [NIST SP 800-30 — guide for conducting risk assessments](https://csrc.nist.gov/pubs/sp/800/30/r1/final)
- [ISO/IEC 27005 — information security risk management](https://www.iso.org/standard/80585.html)
