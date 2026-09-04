---
title: "The week we rotated every password"
date: 2026-07-20
tags: [leadership, operations]
aliases: ["/war-stories/rotating-every-password/"]
---

We rotated every credential in the institute in one week. Not because we were clever under pressure, but because of boring work we had finished months earlier: every account was tied to an owner, that owner to a contract, that contract to a manager, and that manager to another manager. When a serious security incident hit, the question "who owns this account?" had an answer for every single account. That is the whole story. Everything else is detail.

*A note before the detail: everything here is historical. The weaknesses it touches on were fixed at the time, the environment has moved on since under people doing good work, and I have no current access to it or knowledge of it.*

If you read the earlier field note about making identity normal — https://blog.riera.co.uk/field-notes/identity-is-normal-now/ — this is the sequel where that groundwork paid for itself in a single, very bad fortnight. Under the old system there was no relationship between HR and the accounts. We would have been rotating passwords for people we could not name, could not reach, and could not hold responsible. Instead we had a graph. A graph is what you want at 2am.

What can I say publicly about the incident? Deliberately little, and I will keep it that way. It was serious. The root cause was mundane in the way these things always are — a configuration gap of the kind every large estate has somewhere — and it was closed. We had a lot of very knowledgeable, very organised outside help, and I learned a great deal from how they communicated, but I am not going to name responders or dramatise it. The useful, honest lesson is a management one: it is very hard to say certain things from inside an organisation, and much easier to say them from outside during a crisis. A crisis makes previously unsayable things obvious, and a surprising amount of overdue modernisation moved forward on the back of it.

Now the part everyone asks about, because a chart of it looks strange. The password-compliance curve that sat around 45% for weeks and then climbed to the high nineties — the slow, famous one — was the **second** rotation, not the first.

- The **first** rotation was the incident-driven one. It was fast and it was blunt. Change your password now, or your account is closed. We got through everyone in a week.
- The **second** rotation was the one we let breathe. Because we already knew from the first round that we *could* change every password in a week, we deliberately relaxed. We let people take their time, let it run through the summer, and did not push.
- Non-compliers at the end of the relaxed window simply had their accounts closed. If you would not change a password over an entire summer with repeated reminders, you probably were not using the account — and you could re-onboard if you actually needed it.

So the scary-looking flat line was not panic or failure. It was a choice. We had already proven the fast path worked, so the second time we optimised for calm instead of speed.

The closures are where the culture of the place showed itself. Not everyone with an account was staff. Plenty were collaborators on loose agreements rather than contracts. When we enforced that every account must map to a contract or an agreement with a responsible manager, a surprising number of accounts turned out to have no one willing to claim them. They had been renewed and extended for years — friends of someone, favours that never expired. Close to a third of our "users" were accounts nobody would own once ownership carried a cost. I do not think anyone believed we would actually close them, because closing them risked cutting off someone important. We closed them anyway. That was the point.

Some of those closures exposed how much informal process had quietly grown up around dormant accounts — old mailboxes doubling as shared archives, access that existed because it had always existed. None of it was malicious. All of it was invisible until an account had to have an owner. Each closure was a conversation, and each conversation made the graph a little more honest.

The one holdout who kept us from a clean 100%? I do not remember who it was. Probably a rounding error. I have made my peace with it.

The lesson I keep coming back to is unglamorous. The heroics people remember — rotate everything in a week — were only possible because of the unloved identity plumbing nobody thanks you for. Owners, contracts, managers, a clean graph. Do that work when there is no crisis, and the crisis becomes a scheduling problem instead of an archaeology dig.

What is the account in your estate that nobody would claim if claiming it meant becoming responsible for it?

## Sources

- [NIST SP 800-63B — digital identity guidelines, authentication and lifecycle management](https://pages.nist.gov/800-63-3/sp800-63b.html)
- [NCSC — password administration for system owners](https://www.ncsc.gov.uk/collection/passwords)
- [Joiners, movers and leavers — identity lifecycle overview](https://en.wikipedia.org/wiki/Identity_management#Identity_lifecycle)
