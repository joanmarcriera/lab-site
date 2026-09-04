---
title: "What nine and a half years of arguing for a CMDB taught me"
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

Meanwhile a lightweight standard was adopted instead: FitSM. Colleagues were disappointed I wasn't studying for the exams; I passed them anyway. It is a subset of ISO 20000 — if you know the parent, you know the child.

And I stopped quietly absorbing the chaos. Every time a change broke something, I asked the same questions, in public: was this change recorded anywhere? Was it done in order? Did two people just change the same thing in two different ways? The answers were no, no, and yes.

The questions were heard. The argument, in the form I was making it, was not — and I had not yet found the form that would turn it into a decision.

Then someone offered ITIL training, and I said yes to everything — and pushed the managers to attend, not the technical staff. Some took offence.

The trainer had written a widely read book on service management. So I asked, in front of everyone: can you do change management without a CMDB? She answered carefully. I asked again, from a different angle. And again. Until careful ran out: "No. Not possible. I have never seen it and I never will. How do you change something if you don't know what you have, and you don't record anything?"

That one sentence moved more than my six years of asking. In a later expert meeting someone even said it out loud: "that's what Marc has been saying for six years now." I resolved never to say it again. I didn't need to.

Then came the part that taught me the most, and it isn't about technology. When ownership of the CMDB was finally on the table, I volunteered — I had implemented them before, more than once. It went, reasonably enough on paper, to a more senior colleague, because that is how ownership of cross-cutting work usually gets assigned: by seniority. Nobody in that room, me included, made the case that it should be assigned by who had done it before.

I want to be precise about where the failure sits, because it is not with any one person. The lesson is about the system, and I was part of it: when critical work is assigned by title rather than by who has done it before, you lose years.

It still took years of presentations after that. And here is the part nobody likes written down: when an institution caps everyone's stay with a fixed-term staff rule — and I understand why such rules exist — tool selection acquires a quiet pull towards CV selection: the platform whose name travels best onto a next job. I felt that pull myself. The only defence I know is to write the whole-life cost next to every option before the shortlist exists, because money rarely leaks in scandals — it leaks in a hundred reasonable-sounding decisions with no feedback loop attached.

And the ending is almost too neat to print. The platform arrived — without the CMDB module, which cost extra. The implementation partner said in one meeting what I had been saying for six years: you need the CMDB. A few years later the module was bought. External voices carry further than internal ones; I should have borrowed one sooner.

When I left, it was a licence and a table populated from the configuration system with whatever fields could be scraped — nothing yet relating to anything. Whether that has changed since, I don't know; I no longer have any visibility, and the people there now are doing good work. The general lesson stands on its own: a CMDB starts from the things that don't move (data centre, room, row, rack, unit) and builds up, and buying the module is not the same as doing the work.

Final score when I left, nine and a half years in: incident management arriving, change management partially, and the CMDB a bought licence and an unrelated table. I left behind the roadmap, the pilots, and normalised API scripts across the monitoring and configuration systems — everything needed to finish it. A licence, it turns out, is easier to buy than a discipline.

Three things I'd tell any technology leader from this:

• You cannot manage change if you don't know what you have. Not my opinion — the verdict of someone who literally wrote the book on the subject, under repeated questioning.
• Learn the ladder of no: silence → we're too small → others won't buy in → not in my remaining tenure. None of these is an argument. All of them are answers you'll get instead of one.
• Assign critical work by competence, not title. Seniority is a fine default for accountability and a poor one for expertise; confusing the two costs you years.

What's the longest your organisation has argued about something this basic? Am I missing something?

## Sources

- [FitSM, the lightweight ITSM standard](https://www.fitsm.eu/)
- [ISO/IEC 20000](https://en.wikipedia.org/wiki/ISO/IEC_20000)
