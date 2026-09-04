---
title: "The tender clause nobody had used before"
date: 2026-07-22
tags: [finance, operations]
aliases: ["/war-stories/the-tender-refund-clause/"]
---

I put a clause in a storage tender that made vendors read twice: if the delivered system cannot write one petabyte in a week and read one petabyte back in a week, you take it home and refund us.

Nobody had put an acceptance test in one of our tenders before. It paid for itself almost immediately — during acceptance, the system returned a cheerful S3 "200 OK" for a full petabyte of writes, and only 700 terabytes were actually readable. Silent data loss, caught by contract instead of by disaster. The vendor, to their credit, was deeply invested — it was the first time they'd sold this solution standalone — and fixed it fast. But without that clause, we'd have found out the day we needed the data.

What the tender replaced deserves its own museum plaque. The disaster-recovery copy lived on enterprise NAS at a cost per petabyte that belonged to a different decade. The tape layer behind it: files bundled into full-tape tar archives via a parallel-filesystem staging area, orchestrated by two relational databases, written to tape — and the restore path was not even documented. Restoring one file meant reading and unpacking an entire tape. Tapes only get bigger; a design that must read a whole tape to return one file gets worse every year on its own. That's what an unexamined design looks like in infrastructure: not a bad day, a bad slope.

What we built with the tender:

• Replica A on a geo-dispersed, erasure-coded object store across three data centres — lose an entire centre, every file still reconstructable.
• Replica B on tape, written as individual files behind a regular S3 interface. Restoring one file reads one file. And when vendor and client disagree about S3 semantics, you point at Amazon's documentation and the discussion is over. A neutral referee is worth a protocol.
• Two commodity servers replaced: two databases, the staging filesystem, the load-balancer VMs, an in-house API, one entire tape-library brand, and four tape formats retired in one move.
• Result: the cost per petabyte fell by more than an order of magnitude — roughly one-sixteenth of what it replaced.

The politics, as always, were the hard part. A tender that replaces this much at once crosses several teams' territory, and it needs a sponsor with budget and patience for the review rounds; I was lucky to have one. The late requests for extra review felt, at the time, like delay. In hindsight they were the organisation doing exactly what it should with a design that touched so many things — and because the system was keys-in-hand, none of them changed the outcome. The winning bid, by the way, was the shortest one — and the clearest about value delivered per box. Read into that what you will about tender-writing.

And we used it in anger from week one: a full year copying everything off the old tape stock. Since then, the drill is periodic — restore half a petabyte, verify, delete it again. One honest caveat I always attach: the hard part of a large restore isn't tape bandwidth, it's finding twenty petabytes of empty disk to land it on. Your DR plan has a real-estate problem before it has a speed problem.

If your backup contract has no acceptance test, you don't have a backup contract. You have an invoice and a hope.

When did you last restore something big — not because you had to, but to prove you could?

## Sources

- [Erasure coding](https://en.wikipedia.org/wiki/Erasure_code)
- [Linear Tape-Open, the open tape lineage](https://en.wikipedia.org/wiki/Linear_Tape-Open)
- [More field notes](https://blog.riera.co.uk/field-notes/)
