---
title: "The week we rotated every password"
date: 2026-07-20
series: "War stories"
---

We rotated every credential in the institute in one week. Not because we were clever under pressure, but because of boring work we had finished months earlier: every account was tied to an owner, that owner to a contract, that contract to a manager, and that manager to another manager. When the serious security incident hit, the question "who owns this account?" had an answer for every single account. That is the whole story. Everything else is detail.

If you read the earlier war story about making identity normal — https://blog.riera.co.uk/war-stories/identity-is-normal-now/ — this is the sequel where that groundwork paid for itself in a single, very bad fortnight. Under the old system there was no relationship between HR and the accounts. We would have been rotating passwords for people we could not name, could not reach, and could not hold responsible. Instead we had a graph. A graph is what you want at 2am.

What can I say publicly about the incident? Deliberately little, and I will keep it that way. It was a serious security incident. The root cause was mundane in the way these things always are: someone connected the on-prem Active Directory to Entra ID without change management. The two-factor-authentication registration gates in Entra ID were left open, which meant an account that had never set up 2FA could have an authenticator app registered against it — by anyone who could reach it. So an attacker could register their own authenticator and then work on the password. Microsoft flagged it to us. We had a lot of very knowledgeable, very organised outside help, and I learned a great deal from how they communicated — but I am not going to name responders or dramatise it. The useful, honest lesson is a management one: it is very hard to say certain things from inside a company, and much easier to say them from outside during a crisis. A crisis makes previously unsayable things obvious, and a surprising amount of overdue modernisation moved forward on the back of it.

Now the part everyone asks about, because a chart of it looks strange. The password-compliance curve that sat around 45% for weeks and then climbed to roughly 99% — the slow, famous one — was the **second** rotation, not the first.

- The **first** rotation was the incident-driven one. It was fast and it was blunt. Change your password now, or your account is closed. We got through everyone in a week.
- The **second** rotation was the one we let breathe. Because we already knew from the first round that we *could* change every password in a week, we deliberately relaxed. We let people take their time, let it run through the summer, and did not push.
- Non-compliers at the end of the relaxed window simply had their accounts closed. If you would not change a password over an entire summer with repeated reminders, you probably were not using the account — and you could re-onboard if you actually needed it.

So the scary-looking flat line was not panic or failure. It was a choice. We had already proven the fast path worked, so the second time we optimised for calm instead of speed.

The closures are where the culture of the place showed itself. Not everyone with an account was staff. Plenty were collaborators on loose agreements rather than contracts. When we enforced that every account must map to a contract or an agreement with a responsible manager, about 200 accounts turned out to have no one willing to claim them. They had been renewed and extended for years — friends of someone, favours that never expired. The user count fell from 1,700 to 828. Nearly a third of our "users" were accounts nobody would own once ownership carried a cost. I do not think anyone believed we would actually close them, because closing them risked cutting off someone important. We closed them anyway. That was the point.

One of the first we closed belonged to a long-departed head of HR operations. Funny thing: HR had been quietly using that closed manager's mailbox as a shared document archive — several people, maybe everyone in the team, had access to it as a filing cabinet. So when we closed the account, HR's response was not to migrate the documents. It was to **rehire the person** on a zero-salary agreement, purely so the account could be reopened and the mailbox archive would come back. A dead account resurrected as an unpaid employee to keep a filing cabinet online. If you want a single image of the culture we were working against, that is it.

The holdout in the final 99.88%? I genuinely do not remember who it was. Probably a rounding error. I have made my peace with the missing 0.12%.

The lesson I keep coming back to is unglamorous. The heroics people remember — rotate everything in a week — were only possible because of the unloved identity plumbing nobody thanks you for. Owners, contracts, managers, a clean graph. Do that work when there is no crisis, and the crisis becomes a scheduling problem instead of an archaeology dig.

What is the account in your estate that nobody would claim if claiming it meant becoming responsible for it?

## Sources

- [Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/)
- [Multi-factor authentication in Entra ID](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mfa-howitworks)
- [Entra Connect (AD to Entra ID sync)](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/whatis-azure-ad-connect)
