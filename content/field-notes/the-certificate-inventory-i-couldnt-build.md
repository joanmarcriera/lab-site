---
title: "A certificate inventory I couldn't get built"
date: 2026-07-20
tags: [operations]
aliases: ["/war-stories/the-certificate-inventory-i-couldnt-build/"]
---

This one is a failure, and I'll tell it as one. Not a technical failure — the fix was trivial and I designed it twice. It failed because the organisation would rather wait for a vendor to solve a problem someday than solve it itself this year. Certificates kept expiring in production. Every time, they were renewed after they had already failed, and every time by a different person.

The setup, if you want to reproduce the failure yourself: two different teams bought certificates. One team bought them from JISC. The other team bought them from GoDaddy. Neither team monitored them. JISC does at least email you when a certificate is due for renewal — except the email went to a mailbox nobody watched. GoDaddy doesn't tell you at all. So the only signal that a certificate needed renewing was the certificate failing. The service goes down, someone scrambles, someone renews it, and because there's no owner and no record, next time it's a different someone scrambling. There is no learning curve when nobody's on the same curve twice.

The certificate itself carries the one piece of information you need: its expiry date. That's the whole hook. You don't need a vendor, a product, or a platform to read an expiry date. So I proposed something small.

• Find every certificate we have, regardless of which team bought it or from which supplier.
• Monitor each one against its own expiry date.
• When a certificate hits 30 days remaining, the service desk raises it and asks the two purchasing teams: is this yours, and does it need renewing or not?
• Do that for a year. At the end of the year you've touched every certificate at least once, and you have an inventory — who owns what, which team, live or retired.

That inventory is the thing I actually wanted. It's a CMDB without calling it a CMDB — because the moment you call it a CMDB in some organisations, you trigger a two-year argument about whether you're big enough to have one. So I didn't call it that. I called it a list of certificates with dates next to them.

I was told it was too big a job, and that I'd need someone from the project office to help me structure it. Fine — a colleague from the project office did help, and she was good. I drew the whole thing as one picture: a classic workflow, who does which step, where the service desk sits, how an item enters the inventory. It wasn't complicated. She agreed with it, tidied it, and presented it to management — to the Head of IT and Services.

And that's where it stopped. The plan was easy and it went nowhere, because the head wanted to wait for Google to manage the certificates for us. Like they always wait. There's a pattern in some organisations where any internal improvement can be deferred indefinitely by pointing at a future vendor capability: don't build the inventory, because one day a platform will make inventories unnecessary. Don't fix the process, because a someday-migration will make the process moot. The someday never arrives on a schedule you can plan around, and in the meantime the certificates keep expiring in production, renewed only after they fail, each time by whoever happens to be nearest.

Here's what I'd want any technology leader to take from a boring outage like this one:

• Monitoring is not the same as owning. The certificates were technically "monitored" — JISC emailed a mailbox. Nobody read the mailbox. A monitor that nobody is accountable for is a decoration.
• An inventory is a control, not paperwork. If you can't produce a list of the things that can expire, revoke, or lapse — certificates, licences, domains, secrets — you don't have a risk you're managing, you have a risk that's managing you.
• The service desk is the right home for this. It's routine, it's repeatable, it doesn't need a senior engineer, and it's exactly the kind of low-glamour, high-value work a service desk exists to own. Renewals done "by different people each time" is the smell of work that has no home.
• "Let's wait for the vendor" is a decision, and it has a cost. Deferring to a someday-platform feels prudent and free. It is neither. Every deferral is paid for in the outages that happen between now and the day the platform arrives — if it arrives.

The frustrating thing is that none of this was hard. The design fit on one page. The tooling was "read the expiry date and set an alert at 30 days". The only expensive part was the one part I couldn't supply: a management culture that values people's time enough to fix a recurring, embarrassing, entirely preventable failure instead of waiting for someone else to fix it later. That's not a PKI problem. That's a culture problem, and culture is the one thing you can't buy a licence for.

I left the drawing behind. As far as I know the certificates are still managed by nobody in particular, and still renewed the same way — after they break.

What's the smallest, most preventable failure your organisation keeps having, purely because everyone's waiting for a vendor to make it someone else's job?

## Sources

- [Jisc (UK research & education, certificate service)](https://www.jisc.ac.uk/)
- [GoDaddy](https://www.godaddy.com/)
- [X.509 / TLS certificates](https://en.wikipedia.org/wiki/X.509)
- [Google Trust Services (the "let Google manage certs" direction)](https://pki.goog/)
