---
title: "On my first day I was given a second-hand account"
date: 2026-07-22
tags: [leadership, operations]
aliases: ["/war-stories/identity-is-normal-now/"]
---

On my first day, I didn't have an account. The IT person I was replacing created one for me, removed the previous holder's alias, and handed it over — recycled, like a locker. I don't know whether that was standard procedure or just how it happened that morning; either way it could not happen today. My contract? Signed a week later. HR saw no relationship between contracts and accounts.

That should have been the warning. It took years before identity became my problem officially, but the day it did — I was asked to run the data transfer services — the very first question was unanswerable: who owns each of these accounts? To answer it you need a CMDB. To build that you need a relational model of who manages what. And that's when we found the real gem:

• Since HR had no connection to accounts, every manager managed themselves. Having nobody above you in the account tree was, in practice, what identified someone as a manager.
• None of it related to the actual HR systems. Two parallel realities, one payroll.
• Five separate directories across the organisation, never merged — and they couldn't be: the same numeric UID meant different people at different sites, with access to different data. Merging as-is would have been an access-control lottery.
• Accounts "closed" fifteen years earlier still had their data — and the password they were closed with.
• And why had nobody fixed any of this? Follow the money: HR's budget and IT's budget were completely separate, and joiners-movers-leavers is a problem that lives exactly in the gap. Problems that cross department budgets are orphan problems. Nobody funds the seam.
• Managers were creating accounts three months before people joined, because everyone believed a new joiner needed their account email to board the bus on day one. I phoned the bus company. Not true. Fixing the wrongly documented page took two more weeks — of a script that nudged the next responsible person every time the previous one didn't reply.

Meanwhile the pressure from above was for a quick win: "let's move mail to the cloud." My answer never changed. We should not go to the cloud alone; we should go as one organisation, across all sites. And to do that you need unified identity first — with identity staying home. The cloud authenticates against us, not the other way round. Get that right and there is no overlapping-identity mess, and joiners-movers-leavers finally makes sense. Until the last manager I worked for, I don't think management understood a word of it. The counter-plan was to keep nursing the existing stack — a Python 2 identity manager held together with MySQL, Oracle, Go and Bash, permanently one incident away from the whole team "saving the system" again.

Convincing the organisation to pay back this debt took allies — Grenoble, Hamburg and Heidelberg had my back, and when hundreds of accounts needed renaming to make the merge possible, Heidelberg renamed several hundred on their side so we wouldn't have to. The cleanup itself found what fifteen years of nobody-owns-this accumulates: two hundred accounts nobody could claim, over a hundred of them alive for more than five years, kept breathing for the academic perks attached to an active address. And one deliberate leadership decision I'd defend anywhere:

I removed the complexity from my explanations, not from reality. I recruited the best people I could find from other teams, and we agreed on the plan openly between us: we would tell everyone it was easy, and then work hard enough to make it feel easy. This wasn't spin — it was the only way through. Say it's hard and it goes to a committee; the committee is where things I proposed went to wait out my tenure. I had already done the business case, the three-year roadmap, the one-month plan, the tool pilots. Framing it as easy was how I stopped that work from being buried, not a substitute for doing it. Managers approve what feels simple. They fear what sounds like a fifteen-year excavation. It was a fifteen-year excavation. They never felt it.

Where it landed: today, a signed contract triggers the account. It's created on the first day, the manager is notified, the joiner gets onboarding mail at the private address HR captured during contracting. On the last day plus one, the account closes, the password is randomised immediately, archiving begins. Leavers stopped being immortal.

Nobody celebrates it, and that's the point. It's normal now. "Normal" is the highest state infrastructure can reach.

Except once, when normal saved us. Months after the new system went live, a serious security incident hit. I'll stay deliberately vague about it — but I can tell you the kind of thing an audit of that estate turned up, because it's the real lesson: an administrator account with a four-character password that had not changed since 2014, which also happened to be an admin on the virtualisation platform and on the team wikis. That is what "we're not big enough to need process" compounds into over a decade.

With the old stack, changing everyone's password in response would have been simply impossible — there was no "everyone", there were five directories and a Python 2 script. With the new one, we knew we could rotate the credentials of the entire institution within a week — and we did, coordinating across the sister sites while others couldn't even list which accounts their own systems used. The margin between those two worlds was a few months of finished work that almost nobody had wanted to fund.

Identity is the least glamorous system you own, right up until the day it's the only one that matters.

I didn't make many friends in IT along the way. But several thousand researchers now work in a place with less accumulated absurdity, and the phone call to the bus company remains the highest-leverage five minutes of my career.

What's the "everyone knows you have to" belief in your organisation that nobody has ever actually checked?

## Sources

- [NIST's digital identity guidelines (SP 800-63)](https://pages.nist.gov/800-63-3/)
- [Technical debt, the original metaphor](https://en.wikipedia.org/wiki/Technical_debt)
- [How I think about identity at scale, longer form](https://blog.riera.co.uk)
