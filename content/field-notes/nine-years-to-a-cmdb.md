---
title: "Nine and a half years to a CMDB we still didn't have"
date: 2026-07-22
tags: [leadership]
aliases: ["/war-stories/nine-years-to-a-cmdb/"]
---

I have implemented CMDBs before — at Barcelona Media, at the Sant Feliu town council, at the insurer ARAG, at Bull, at Atos. So when I joined a petabyte-scale scientific institution with a large IT function and found no CMDB and no change management, I said so.

I got four answers, in sequence, over years. Learn this ladder — you will meet it too:

• First answer: silence. Nothing. The proposal simply did not exist.
• Second, when I pushed a week later and asked why nobody was responding: "We're not big enough. We don't do change management." Dozens of IT professionals, petabytes of data — not big enough.
• Third: "The others won't buy in. It will be very difficult." Note the shift — no longer wrong, merely hard.
• Fourth, and my favourite: impossible within the horizon of whoever was answering. Not wrong, not hard: inconvenient for one person's calendar.

At no point did anyone say the CMDB was a bad idea. The ladder never does.

Meanwhile a lightweight standard appeared instead: FitSM. Nobody could quite say where it came from. Colleagues were disappointed I wasn't studying for the exams; I passed them anyway. It is a subset of ISO 20000 — if you know the parent, you know the child.

And I stopped quietly absorbing the chaos. Every time a change broke something, I asked the same questions, in public: was this change recorded anywhere? Was it done in order? Did two people just change the same thing in two different ways? The answers were no, no, and yes.

The questions were heard. The argument, in the form I was making it, was not — and I had not yet found the form that would turn it into a decision.

Then someone offered ITIL training, and I said yes to everything — and pushed the managers to attend, not the technical staff. Some took offence.

The trainer had written a widely read book on service management. So I asked, in front of everyone: can you do change management without a CMDB? She answered carefully. I asked again, from a different angle. And again. Until careful ran out: "No. Not possible. I have never seen it and I never will. How do you change something if you don't know what you have, and you don't record anything?"

That one sentence moved more than my six years of asking. In a later expert meeting someone even said it out loud: "that's what Marc has been saying for six years now." I resolved never to say it again. I didn't need to.

Then came the part that taught me the most, and it isn't about technology. When ownership of the CMDB was finally on the table, I volunteered — I had implemented them before, more than once. But I wasn't a head of department, so it went to someone who was — someone who, I learned much later, had taken it on out of duty rather than expertise, and knew it.

I want to be precise about where the failure sits, because it is not with that person. Saying yes in that room took nerve, and being honest about it afterwards took more. The failure is a system that assigns critical work by title instead of competence — and then waits years before hiring, from outside, the CMDB experience it had in the building all along.

It still took years of presentations after that. And here is the part nobody likes written down: when an institution caps everyone's stay with a fixed-term staff rule — and I understand why such rules exist — tool selection quietly becomes CV selection. The push went to the platform whose name travels best onto a next job, at a multiple of what a less fashionable product would have cost for the same licences. Public money doesn't leak in scandals. It leaks in a hundred reasonable-sounding decisions with no feedback loop attached.

And the ending is almost too neat to print. The platform arrived — without the CMDB module, which cost extra. The implementation partner told management in one meeting what I had said for six years: you need the CMDB. A few years later the module was bought.

When I left, it was a licence and a table populated from the configuration system with whatever fields could be scraped — nothing yet relating to anything. Whether that has changed since, I don't know; I no longer have any visibility, and the people there now are doing good work. The general lesson stands on its own: a CMDB starts from the things that don't move (data centre, room, row, rack, unit) and builds up, and buying the module is not the same as doing the work.

Final score, nine and a half years in: incident management is arriving, change management partially, and the CMDB is a bought licence and an unrelated table. I left behind the roadmap, the pilots, and normalised API scripts across the monitoring and configuration systems — everything needed to finish it. External invoices, it turns out, are easier to approve than internal experience; and a licence is easier to buy than a discipline.

Three things I'd tell any technology leader from this:

• You cannot manage change if you don't know what you have. Not my opinion — the verdict of someone who literally wrote the book on the subject, under repeated questioning.
• Learn the ladder of no: silence → we're too small → others won't buy in → not in my remaining tenure. None of these is an argument. All of them are answers you'll get instead of one.
• Assign critical work by competence, not title. A title-holder who privately knows they are out of their depth costs you years. It always comes out eventually.

What's the longest your organisation has argued about something this basic? Am I missing something?

## Sources

- [FitSM, the lightweight ITSM standard](https://www.fitsm.eu/)
- [ISO/IEC 20000](https://en.wikipedia.org/wiki/ISO/IEC_20000)
