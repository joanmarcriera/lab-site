---
title: "The first 15 petabytes took ten years. The next 110 took eight."
date: 2026-07-20
series: "War stories"
---

When I took over FIRE, the archive, at the end of 2017, it held 15 petabytes — the accumulation of ten years. When I handed it on in 2025 it held 125, and in one month it had grown by three petabytes on its own.

What I inherited was a design from another era: an IBM batch system underneath, archiver processes writing directly into the databases, and everything literally in fives. Five user groups, and for each one its own API implementation, its own database, its own staging area, its own queue, and its own poller. Some of the databases were MySQL, some Oracle; two of the MySQL ones were even on different versions with different schemas. A poller would find a row where an archiver had dropped a file path and an MD5, go to that user's staging area, fetch the file, write it to two locations, and report back. Five times over, five different ways. That's not redundancy, it's five single points of failure wearing a trench coat.

The fixes that mattered were never about disks:

• Access layer first. Nobody touches the databases directly, ever again. The archive and the transfer services that export its data are deeply interlinked, so cleaning the boundary came before growing anything.
• Teams of one are not teams. I inherited several "teams" consisting of exactly one person — an SRE here, a DevOps there. I merged them into the development team and made everything everyone's job. Developers who wanted to do SRE did SRE. Everybody grew. Eight people ran an eight-fold growth not because they were heroes, but because the structure stopped wasting them.
• Buy for the curve, not the quarter. The old process was "buy a petabyte, install it next month." At this growth rate that's a permanent emergency. The argument that took real pushing: buy 50 petabytes at a time and migrate data live. Growth doesn't just need more hardware; it needs different processes.
• Decide your consistency model out loud. My first design documents said it plainly: we will not write twice synchronously; we go eventually consistent. People didn't believe the volumes — they kept assuming data has a short lifespan. It doesn't. An institution that intends to outlive me has to be engineered on that timeline. I've always designed for the archive still working when I'm dead.
• Keep logic out of the database. From year one we pulled code out of Oracle procedures and refused to recreate it in Postgres procedures. No business logic hiding in SQL, no batch-system scripts welded into the platform. As native and as boring as possible.

Two war stories inside the war story. When IBM acquired Aspera, our transfer vendor, they wanted £500,000 for a new licence. Instead of buying it, we rented — for the same money we got the licence and managed services, which freed my people from having to be specialists in one proprietary transfer technology. And where the licence tied cost to transfer speed but a bug made the cap unenforceable, we virtualised the Aspera nodes and pinned them to deliberately bandwidth-limited hardware, so the chassis honoured the limit the software couldn't. Compliance by hardware — buying the right amount of restraint on purpose.

And the Postgres migration: we tested heavily, put it in production, and it worked — it just needed a different indexing approach. Then we migrated back. Not because the technology failed, but because the database team that would support it wasn't ready to support it. Running an unsupported database under 100+ petabytes is not bravery, it's debt. We kept the tested migration path in the drawer instead. Engineering maturity is sometimes measured in retreats.

The lesson under all of it: past a certain scale, the work stops being about the thing and becomes about the shape of the organisation around the thing. The petabytes were the easy part.

What's the "team of one" in your organisation that everyone pretends is a team?

## Sources

- [Eventual consistency](https://en.wikipedia.org/wiki/Eventual_consistency)
- [IBM Aspera](https://en.wikipedia.org/wiki/Aspera_(company))
- [Platform LSF, the batch system era](https://en.wikipedia.org/wiki/Platform_LSF)
- [More stories](https://blog.riera.co.uk)
