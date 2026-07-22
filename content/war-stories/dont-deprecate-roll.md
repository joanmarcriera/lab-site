---
title: "Don't deprecate — roll"
date: 2026-07-20
series: "War stories"
---

We replaced the archive's front door — the public entry point researchers around the world push data through — and kept a set of DNS names that go back to the 1980s alive through the whole thing. Not one of those old addresses broke. That's the headline, and the method behind it is the only part worth copying: don't deprecate, roll.

Start with the mess we inherited. Five users, and for those five users we had five databases — a mix of MySQL and Oracle — sitting behind five slightly different implementations of the same Python API. Five near-identical things, none of them quite the same, each one its own little maintenance burden. It was obviously wrong. Nobody sat down and designed it that way; it accreted, one well-meaning decision at a time, until we were running five of everything to do one job.

The good news about something that's obviously wrong is that when it finally breaks, replacing it is easy to justify. So when it broke, we didn't patch the five — we built one new API that did the job properly and pointed at it.

Then came the patient part. We ran the old and the new in parallel for a full year. That was deliberate. These are researchers pushing real data through a live service; you do not yank the floor out from under them to hit a migration deadline. Four of the five users moved over reasonably well. The fifth did not.

That last user was a long-standing one with no intention of moving on my timetable. And because we had no SLA, I could play a long game. So I did. I stopped pouring effort into propping up the old service's rough edges, and each time something creaked I offered the new API that was already working perfectly well for everyone else. No drama, no deadline — just letting the old path show its age while a better one sat right there. It might have taken another year.

Then the pandemic hit, and the games stopped. Suddenly nobody had the luxury of a two-decade standoff over an API. So we did the direct thing: took their code, did the migration ourselves, and moved on. In one month, the users who'd been dug in for years were across. Sometimes an external shock does the political work you couldn't.

But the real lesson isn't the API rebuild. It's what we did with the public face of the service — and here's the playbook.

We didn't deprecate. We rolled. For an external user hitting a transfer service — FTP, Aspera and the rest — you simply cannot deprecate the address. It's public. Somewhere in the world there is a script written years ago, by someone you'll never meet, that hard-codes one of those hostnames and runs unattended at 3am. Turn it off and you break science you didn't know was happening. So the rule was: every DNS name comes with us, no exceptions, including ones minted in the 1980s. We didn't retire them — we made them more robust.

Here's the trick that made it manageable:

• **Every historical DNS name survives.** Names going back to the 80s were carried forward untouched, so every old URL out in the wild still resolves and still works.
• **Build an alias matrix instead of a service per name.** A lot of those 39 names were really the same service wearing different labels — one per protocol, one per historical process. We mapped them out and collapsed 39 DNS names down to 9 actual services, with the DNS names as aliases pointing at the right one.
• **One endpoint now serves what many used to.** Where an old DNS name historically saw one folder on the FTP server, it now sees twenty folders on one consolidated server — but the folder that name always pointed at is still there, in the same place, so the old URL behaves exactly as it always did.
• **The user sees continuity; we get consolidation.** Nothing changed for the outside world. Everything changed for us: 9 services to maintain instead of 39. Easier. Cheaper. Fewer things to break.

That's the whole philosophy. Deprecation is a message you send to your users: stop what you're doing, come change your scripts, on my timetable. For a public research service that message mostly gets ignored and then something silently breaks. Rolling is the opposite — you take on the burden of continuity yourself so the user never has to act. You keep the promise the old address made, forever, and quietly rearrange everything behind it.

The consolidation is where it pays back. Preserving 39 dead-looking DNS names sounds like hoarding until you realise they only cost you nine real services once you've built the alias matrix. You get the compatibility of never breaking anything and the operational simplicity of running a fraction of the estate. You don't have to choose between "don't break the users" and "don't drown in legacy." The alias matrix gives you both.

If you run a public-facing service with addresses older than some of your engineers: are you planning to deprecate the ones you'd rather not maintain — or could you roll them, keep every promise, and still collapse the estate behind them?

## Sources

- [IBM Aspera](https://www.ibm.com/products/aspera)
- [DNS (Domain Name System)](https://en.wikipedia.org/wiki/Domain_Name_System)
- [EMBL-EBI](https://www.ebi.ac.uk/)
