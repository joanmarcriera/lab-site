---
title: "Nine and a half years to a CMDB we still didn't have"
date: 2026-07-20
series: "War stories"
---

I have implemented CMDBs before — at Barcelona Media, at the Sant Feliu town council, at the insurer ARAG, at Bull, at Atos. So when I joined a petabyte-scale scientific institution with close to a hundred IT people and found no CMDB and no change management, I said so.

I got four answers, in sequence, over years. Learn this ladder — you will meet it too:

• First answer: silence. Nothing. The proposal simply did not exist.
• Second, when I pushed a week later and asked why nobody was responding: "We're not big enough. We don't do change management." A hundred IT professionals, petabytes of data — not big enough.
• Third: "The others won't buy in. It will be very difficult." Note the shift — no longer wrong, merely hard.
• Fourth, and my favourite: "I only have five years left here. This is impossible." Not wrong, not hard: inconvenient for one person's remaining tenure.

At no point did anyone say the CMDB was a bad idea. The ladder never does.

Meanwhile a lightweight standard appeared instead: FitSM. Nobody could quite say where it came from. Colleagues were disappointed I wasn't studying for the exams; I passed them anyway. It is a subset of ISO 20000 — if you know the parent, you know the child.

And I stopped quietly absorbing the chaos. Every time a change broke something, I asked the same questions, in public: was this change recorded anywhere? Was it done in order? Did two people just change the same thing in two different ways? The answers were no, no, and yes.

Management heard the questions. They did not hear the argument.

Then someone offered ITIL training, and I said yes to everything — and pushed the managers to attend, not the technical staff. Some took offence. A new manager had arrived around that time who understood perfectly well what a CMDB was for, and was diplomatic enough to suggest we might still find a way to live without one.

The trainer had written a book on service management that sold 48,000 copies. So I asked her, in front of everyone: can you do change management without a CMDB? She answered carefully. I asked again, from a different angle. And again. Until careful ran out: "No. Not possible. I have never seen it and I never will. How do you change something if you don't know what you have, and you don't record anything?"

That one sentence moved more than my six years of asking. In a later expert meeting someone even said it out loud: "that's what Marc has been saying for six years now." I resolved never to say it again. I didn't need to.

Then came the part that taught me the most, and it isn't about technology. When ownership of the CMDB was finally on the table, I volunteered — I had implemented them before, more than once. But I wasn't a head of department, so it went to someone who was. Years later, on my last day, she told me what happened after that meeting: she'd gone home and said to her husband, "I have no clue what I've just taken. I don't understand any of this."

I want to be precise about where the failure sits, because it is not with her. Saying yes in that room took nerve, and telling me the truth on my last day took more. The failure is a system that assigns critical work by title instead of competence — and then waits years before hiring, from outside, the CMDB experience it had in the building all along. Which is eventually what happened.

It still took years of presentations after that. And here is the part nobody likes written down: when an institution caps everyone's stay — the nine-year rule is public policy, and I understand why it exists — tool selection quietly becomes CV selection. The push went to ServiceNow, the one CERN runs, because that is the name that travels with you onto your next job. BMC Helix would have given us every licence we needed for the price of ServiceNow's entry tier. Public money doesn't leak in scandals. It leaks in a hundred reasonable-sounding decisions with no feedback loop attached.

And the ending is almost too neat to print. ServiceNow arrived — without the CMDB module, which cost extra. The implementation partner, who happened to be an Atos company, the consultancy where I'd built CMDBs years earlier, told management in one meeting what I had said for six years: you need the CMDB. A few years later they bought the module.

They still haven't implemented it. There's a table now, populated from PuppetDB with whatever fields could be scraped — but nothing relates to anything, and the team holding it hasn't yet grasped that a CMDB starts from the things that don't move (data centre, room, row, rack, unit) and builds up. Buying the module was mistaken for doing the work.

Final score, nine and a half years in: incident management is arriving, change management partially, and the CMDB is a bought licence and an unrelated table. I left behind the roadmap, the pilots, and normalised API scripts across the monitoring and configuration systems — everything needed to finish it. External invoices, it turns out, are easier to approve than internal experience; and a licence is easier to buy than a discipline.

Three things I'd tell any technology leader from this:

• You cannot manage change if you don't know what you have. Not my opinion — the verdict of someone who sold 48,000 books on the subject, under repeated questioning.
• Learn the ladder of no: silence → we're too small → others won't buy in → not in my remaining tenure. None of these is an argument. All of them are answers you'll get instead of one.
• Assign critical work by competence, not title. The title-holder's private "I have no clue what I've just taken" costs you five years. It always comes out eventually — usually on someone's last day.

What's the longest your organisation has argued about something this basic? Am I missing something?

## Sources

- [FitSM, the lightweight ITSM standard](https://www.fitsm.eu/)
- [ISO/IEC 20000](https://en.wikipedia.org/wiki/ISO/IEC_20000)
- [The nine-year rule, in EMBL's own words to the UK Parliament](https://committees.parliament.uk/writtenevidence/111157/pdf/)
- [CERN's service portal (yes, it's ServiceNow)](https://cern.service-now.com/service-portal?id=functional_element&name=service-now)
