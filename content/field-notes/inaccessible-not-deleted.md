---
title: "\"Inaccessible\", not \"deleted\" — the word that saved 12 petabytes of work"
date: 2026-07-20
tags: [operations]
aliases: ["/war-stories/inaccessible-not-deleted/"]
---

We had to get rid of about 12 petabytes because a contract said so. Most people who hadn't read the contract said "we need to delete the data". The contract didn't say delete. It said we were required to make the data inaccessible. Those are not the same thing, and the difference between them was worth an enormous amount of avoided, pointless work. Reading the exact words is a technical skill.

Start with what "delete" would actually mean on tape. Deleting data from tape isn't a flag — it's physical. To truly erase it you have to load each tape and write over the existing data, zeros and ones on top of the old zeros and ones, exactly as you would to wipe a disk. Otherwise the bits are still there and still readable. Twelve petabytes of tapes, loaded and overwritten one by one, is weeks of drive time and real wear on the media, for no benefit the contract asked for.

Now here's why "inaccessible" was already most of the way done before we started. From day one, the way we wrote data was this: anything bigger than about half a megabyte gets striped — with erasure coding and checksum bits — across six different tapes. So to reconstruct a single file, you need those six specific tapes, and you need to know the order to read them in. The map of which content lives on which tapes, in which order, is held in a database that is not on the tapes themselves. Worst case for an attacker: you'd need the order of all the tapes, the tool that wrote them, and knowledge of how they were written. If somebody simply found a petabyte of our tapes in a skip, they would get nothing out of them. The data was, by construction, already close to inaccessible.

So the decommission looked like this:

• We deleted the data from the active storage — the online copy people actually reach through.
• We flagged, in the database, that the data was deleted from tape.
• We did not go and overwrite 12 petabytes of physical tape with zeros. That would have been damaging to the media and pointless: with the active copy gone and the database flag set, the data was already inaccessible in the sense the contract required.
• The physical overwrite is deferred, not skipped. Those tapes now carry files flagged for deletion. When we next move to a new generation of drives, we load the tapes, reformat them — at which point, if IBM holds to the pattern of the last decade, they come back roughly 50% bigger in capacity — and reuse them. New data is written on top, and the old data is genuinely overwritten as a side effect of work we were going to do anyway.

That's the whole trick: we satisfied the contract with a database flag, and let the expensive physical part ride along, for free, on the next hardware refresh. We didn't manufacture a 12-petabyte project to feel thorough.

But the bigger money I ever saved on this archive wasn't a deletion. It was a thing I stopped us building.

When FIRE, our active archive, started to succeed, someone arrived with the idea of wiring in the beta of a data-discovery service. The design, once I did the arithmetic, was alarming. For every single file added to FIRE, we would compute a SHA-1 hash of the file — SHA-1, for some reason, not even MD5 — and then a SHA-1 of every folder that contained it. Not just the immediate folder: the parent, and the parent's parent, all the way up. If a file sat three folders deep, that's four SHA-1 hashes for one file: one for the file and three for the ancestor folders. Add a second file to that same folder and you don't reuse anything — that's four more. Then publish all those hashes out to an external service that was, at that point, still in alpha.

Multiply that by the ingest rate of a fast-growing petabyte archive and you're proposing to hash the same folder trees over and over, forever, and stream the results to an alpha dependency. It was coming on hard precisely because FIRE was winning, and I genuinely couldn't tell whether it would kill the service by accident. I don't think the people pushing it fully understood what they were asking the archive to do at scale.

I didn't win that one with a rant about SHA-1. I won it with sequencing. I said we needed more resources to first finish FIRE, retire LSF, and retire everything still pending — because we were carrying the users, the services and the researchers across with us, and that came first. Once that was done, we could sit down and discuss the discovery project on its merits and how it actually served the institution's missions. That was the end of it. The wasteful design never shipped, and the archive kept growing.

Which brings me to the question I actually get asked: at 120 petabytes, what keeps you up at night on cost? On cost — nothing. The unit economics are fine and they get better with every tape generation. What keeps me up is the lack of process, and the fact that the flywheel I tried to build runs on the culture of the place rather than on anything durable. A flywheel made of habits and good people spins beautifully until the right people leave. Culture requires certain personalities, and I'm not sure we always hired the ones that keep it spinning.

Cost problems, at this scale, mostly solve themselves. Process and culture problems compound in the dark, and no amount of capacity buys you out of them.

When your organisation is told to "delete" something, does anyone go back and read whether that's actually what's required — or do you just do the expensive literal thing to feel safe?

## Sources

- [Erasure coding](https://en.wikipedia.org/wiki/Erasure_code)
- [SHA-1 (and why hashing everything, repeatedly, is a design smell)](https://en.wikipedia.org/wiki/SHA-1)
- [LTO tape and its capacity roadmap](https://en.wikipedia.org/wiki/Linear_Tape-Open)
- [EMBL-EBI FIRE archive / data resources](https://www.ebi.ac.uk/)
