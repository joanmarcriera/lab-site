---
title: "\"Inaccessible\", not \"deleted\" — the word that saved 12 petabytes of work"
date: 2026-07-20
tags: [operations]
aliases: ["/war-stories/inaccessible-not-deleted/"]
---

We had to get rid of about 12 petabytes because a contract said so. Most people who hadn't read the contract said "we need to delete the data". The contract didn't say delete. It said we were required to make the data inaccessible. Those are not the same thing, and the difference between them was worth an enormous amount of avoided, pointless work. Reading the exact words is a technical skill — and so is checking your reading with the people who own the contract and the data before you act on it, which we did, in writing.

Start with what "delete" would actually mean on tape. Deleting data from tape isn't a flag — it's physical. To truly erase it you have to load each tape and write over the existing data, zeros and ones on top of the old zeros and ones, exactly as you would to wipe a disk. Otherwise the bits are still there and still readable. Twelve petabytes of tapes, loaded and overwritten one by one, is weeks of drive time and real wear on the media, for no benefit the contract asked for.

Now here's why "inaccessible" was already most of the way done before we started. From day one, the archive never wrote a file to a tape. It wrote erasure-coded fragments across several media, and the map of what lives where lives somewhere else entirely. A tape on its own is noise; the catalogue is what turns it back into data. The data was, by construction, already close to inaccessible the moment the catalogue said so.

So the decommission looked like this:

• We deleted the data from the active storage — the online copy people actually reach through.
• We removed the catalogue entries and flagged the tape fragments as deleted, so nothing could resolve to that data any more.
• We did not go and overwrite 12 petabytes of physical tape with zeros. That would have been damaging to the media and pointless: with the active copy gone and the catalogue entries removed, the data was already inaccessible in the sense the contract required — and the contract owners agreed.
• The physical overwrite is scheduled, not skipped. Those tapes carry fragments flagged for deletion. At the next generation of drives, the tapes are reformatted and reused — at which point, if the tape roadmap holds to the pattern of the last decade, they come back roughly 50% bigger — and the old data is physically overwritten as a side effect of work that was going to happen anyway.

That's the whole trick: we satisfied the contract as written, agreed the interpretation with the people it was written for, and let the expensive physical part ride along, for free, on the next hardware refresh. We didn't manufacture a 12-petabyte project to feel thorough.

But the bigger money I ever saved on this archive wasn't a deletion. It was a thing I stopped us building.

When our active archive started to succeed, someone arrived with the idea of wiring in the beta of a data-discovery service. The design, once I did the arithmetic, was alarming. For every single file added to the archive, we would compute a SHA-1 hash of the file — SHA-1, for some reason, not even MD5 — and then a SHA-1 of every folder that contained it. Not just the immediate folder: the parent, and the parent's parent, all the way up. If a file sat three folders deep, that's four SHA-1 hashes for one file: one for the file and three for the ancestor folders. Add a second file to that same folder and you don't reuse anything — that's four more. Then publish all those hashes out to an external service that was, at that point, still in alpha.

Multiply that by the ingest rate of a fast-growing petabyte archive and you're proposing to hash the same folder trees over and over, forever, and stream the results to an alpha dependency. It was coming on hard precisely because the archive was winning, and I couldn't tell whether it would kill the service by accident. It is easy, from outside an archive, to underestimate what a per-file operation costs at that ingest rate — and my job was to make that cost visible, not to assume bad design.

I didn't win that one with a rant about SHA-1. I won it with sequencing. I said we needed more resources to first finish the archive, retire LSF, and retire everything still pending — because we were carrying the users, the services and the researchers across with us, and that came first. Once that was done, we could sit down and discuss the discovery project on its merits and how it actually served the institution's missions. That was the end of it. The wasteful design never shipped, and the archive kept growing.

Which brings me to the question I actually get asked: at 120 petabytes, what keeps you up at night on cost? On cost — nothing. The unit economics are fine and they get better with every tape generation. What keeps me up is process: the flywheel I tried to build ran on the habits of good people rather than on anything written down. A flywheel made of habits spins beautifully until the people change. Turning habits into a process that survives them is the part of the job I got to too late.

Cost problems, at this scale, mostly solve themselves. Process and culture problems compound in the dark, and no amount of capacity buys you out of them.

When your organisation is told to "delete" something, does anyone go back and read whether that's actually what's required — or do you just do the expensive literal thing to feel safe?

## Sources

- [Erasure coding](https://en.wikipedia.org/wiki/Erasure_code)
- [SHA-1 (and why hashing everything, repeatedly, is a design smell)](https://en.wikipedia.org/wiki/SHA-1)
- [LTO tape and its capacity roadmap](https://en.wikipedia.org/wiki/Linear_Tape-Open)
