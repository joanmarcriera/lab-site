---
title: "The tender clause nobody had used before"
date: 2026-07-22
series: "War stories"
---

I put a clause in a storage tender that made vendors read twice: if the delivered system cannot write one petabyte in a week and read one petabyte back in a week, you take it home and refund us.

Nobody had put an acceptance test in one of our tenders before. It paid for itself almost immediately — during acceptance, the system returned a cheerful S3 "200 OK" for a full petabyte of writes, and only 700 terabytes were actually readable. Silent data loss, caught by contract instead of by disaster. The vendor, to their credit, was deeply invested — it was the first time they'd sold this solution standalone — and fixed it fast. But without that clause, we'd have found out the day we needed the data.

What the tender replaced deserves its own museum plaque. The disaster-recovery copy lived on Isilon NFS at £113,000 per petabyte. The tape layer behind it: files bundled into full-tape tar archives via half a petabyte of Seagate ClusterStor Lustre, orchestrated by two Oracle databases, written to LTO-6 in a Spectra Logic library — and the restore path was not even documented. Restoring one file meant reading and unpacking an entire tape. Tapes only get bigger; a design that must read a whole tape to return one file gets worse every year on its own. That's what lack of vision looks like in infrastructure: not a bad day, a bad slope.

What we built with the £250,000 tender:

• Replica A on a geo-dispersed, erasure-coded object store across three data centres — lose an entire centre, every file still reconstructable.
• Replica B on tape, written as individual files behind a regular S3 interface. Restoring one file reads one file. And when vendor and client disagree about S3 semantics, you point at Amazon's documentation and the discussion is over. A neutral referee is worth a protocol.
• Two commodity servers with 250GB of RAM replaced: two Oracles, the Lustre, the load-balancer VMs, an in-house API, one entire library brand (Spectra Logic out, IBM kept — the vendor's choice, and they threw in the Jaguar drive upgrade to win), and four tape formats retired in one move.
• Result: about £7,000 per petabyte. Against £113,000 for what it replaced.

The politics, as always, were the hard part. The storage team stepped back until the tender was fully written; my section head funded it from his own budget. I was asked to delay the award so "someone from storage" could review it — the someone was a new joiner whose background was Windows. A thoroughly nice person, and it didn't matter: the system was keys-in-hand, the operating system was irrelevant. The winning bid, by the way, was the shortest one — and the clearest about value delivered per box. Read into that what you will about tender-writing.

And we used it in anger from week one: a full year copying everything off the old LTO-6/7/8 stock. Since then, the drill is periodic — restore half a petabyte, verify, delete it again. One honest caveat I always attach: the hard part of a large restore isn't tape bandwidth, it's finding twenty petabytes of empty disk to land it on. Your DR plan has a real-estate problem before it has a speed problem.

If your backup contract has no acceptance test, you don't have a backup contract. You have an invoice and a hope.

When did you last restore something big — not because you had to, but to prove you could?

## Sources

- [Erasure coding](https://en.wikipedia.org/wiki/Erasure_code)
- [Linear Tape-Open, the open tape lineage](https://en.wikipedia.org/wiki/Linear_Tape-Open)
- [More war stories](https://blog.riera.co.uk)
