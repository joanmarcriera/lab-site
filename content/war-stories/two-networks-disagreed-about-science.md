---
title: "The ports wouldn't open because two networks disagreed about what \"science\" was"
date: 2026-07-20
series: "War stories"
---

Some data transfers just wouldn't go through, and the fix wasn't on our side at all. It was two networks on two continents that had never compared notes. Once I got them in the same conversation, the problem dissolved — and not just for us. It unblocked institutions we'd never even talked to.

Here's the mechanism, because it's simpler than it sounds. Research-and-education networks classify traffic. Ranges of IP addresses get tagged as "science" — legitimate research data movement — and that classification is what decides whether certain ports open for a high-throughput transfer. If your address range is on the science list, the door opens and the data flows. If it isn't, the transfer quietly refuses to complete and you're left staring at a connection that should work and doesn't.

Our data was going between the UK and the United States. On the US side — I believe it was ESnet, the American research network — some of the JISC ranges on the UK side simply weren't declared as science. Not blocked, not blacklisted. Just missing from the list. An omission, not a decision. And an omission is the worst kind of fault to chase, because everyone's own configuration looks correct. JISC looked right to JISC. ESnet looked right to ESnet. Nobody had a bug. The gap only existed in the space between them, where neither could see it.

I could have burned weeks poking at our end — checking firewalls, retrying transfers, opening tickets that went nowhere — because from where I stood everything on our side was fine. It was fine. The missing piece was a reconciliation that only two other organisations could do, and neither of them knew it needed doing.

So I did the one useful thing available to me: I connected the two parties who each held half the answer. I got the right people from JISC and the right people from ESnet talking directly, and asked them to reconcile the subnets between themselves — to work out exactly which JISC ranges were missing from the US science classification. Ranges that, as it happened, we were part of. I couldn't fix it. They could, together, in a conversation that took minutes once it was actually happening.

When they added the missing subnets, the data started flowing. And here's the part I didn't expect: it flowed for far more than us. We were just one institution inside those JISC ranges. The moment the ranges were correctly classified, every institution sitting in them was unblocked too. I'd gone in trying to fix one lab's transfers and came out having quietly fixed the pipe for a whole set of organisations who never knew there'd been a problem, or that it was solved.

That's the lesson I keep from this one, and it's short:

• **When something's broken in the space between two systems, your job isn't to fix it — it's to get the two owners into the same room.** Neither JISC nor ESnet could see the gap alone. Both could close it in minutes together.
• **A missing entry is not a bug on anyone's side.** Everyone's config was internally correct. Stop hunting for the culprit and start hunting for the seam.
• **Fixing the shared layer fixes it for everyone on it.** A per-institution workaround would have helped one lab. Correcting the classification helped every institution in the range.

Most of my hardest problems haven't been technical. They've been two competent teams, each holding half the picture, who'd never been introduced. The whole intervention was a phone call and an email. No code, no clever architecture — just noticing that the fault lived in the gap, and that the people who could close it didn't know the other existed.

When something on your estate is broken and your own side checks out clean: are you still debugging your half — or have you found the two people who each hold half the answer and put them in touch?

## Sources

- [JISC](https://www.jisc.ac.uk/)
- [ESnet (Energy Sciences Network)](https://www.es.net/)
- [EMBL-EBI](https://www.ebi.ac.uk/)
