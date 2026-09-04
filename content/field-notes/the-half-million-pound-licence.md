---
title: "The six-figure licence I didn't buy"
date: 2026-07-20
tags: [finance]
aliases: ["/war-stories/the-half-million-pound-licence/"]
---

The cheapest data transfer is the licence you never renew. We were about to be asked for a very large sum of money, and we didn't pay it.

At the institute, moving and archiving research data is not a side task — it is the mission. So the money we spend on data transfer is not overhead, it is the job. Which is exactly why the pricing model matters more than the software.

We had two products doing broadly the same thing. One, built by the research community for the research community, on a flat licence: pay once a year, move as much data as you like. The other, a commercial product on the opposite model: the more data you move, the more you pay. For most companies that per-volume model is fine, because moving data is a cost they want to keep down. For an institution whose whole purpose is to move and archive ever-growing volumes of research data, it is structurally wrong. You are penalised for succeeding at your mission.

The trigger was simple. The per-volume product was maxed out. To keep going, we were looking at a new licence costing roughly eight times what we were paying for both products combined — and then renting more capacity on top of that. The real number in this story was never the annual fees. It was the new licence we avoided.

The first time I said we should move off the per-volume product, the fair question came back: "To what?" To the flat-licence one. "But we don't have it." We did — sort of. We had forty servers of it already: forty scattered, underused virtual machines that nobody, me included, had ever treated as a service. I needed to build it properly.

Here is how it went:

- **Used the vendor as free consultancy.** I asked the flat-licence vendor directly what a proper deployment should look like. They advised on sizing. We consolidated forty scattered VMs down to three physical servers, built to that sizing. It took a year just to get the hardware.

- **Kept the per-volume product inside its licence.** It ran as a virtual machine. I moved it onto a hypervisor with a link capped at the throughput we had actually licensed, so usage stayed within the contract we already had while everyone migrated. No surprise overage, no trigger for the new licence.

- **Ran both in parallel and pointed everyone at the fast path.** With the flat-licence service live alongside, migrating became the obvious choice, so people moved themselves.

- **Turned parallel-running into leverage.** With a working alternative already carrying traffic, I told the commercial vendor plainly: if you want to keep the contract, the product has to perform better — fewer reconnects, fewer errors — and we want managed services for the same price. We got it, delivered through a partner. That only worked because we weren't bluffing; the replacement was already running.

- **Won the users with arithmetic, not opinions.** The per-volume product is well-loved in the research community, and those users trusted it. I didn't argue about software. I showed them the numbers. That much money is a lot for researchers — money that buys science, not licences. They were happy to start moving.

The lesson I keep from this one isn't "one product good, the other bad". Both are fine products and the per-volume model suits plenty of organisations. The lesson is that you have to match the pricing model to your mission before you match the features. If your reason to exist is moving more data every year, a contract that charges you more for moving more data will eventually corner you. It doesn't matter how good the transfers are.

And the tactics compound. Staying inside the licence bought time. The time let us build the three servers properly. The properly-built servers gave us a credible parallel service. The parallel service gave us leverage with the vendor. The leverage plus the raw numbers won the users. Pull any one of those out and it's just a migration that drags on for three years while the old bill keeps climbing.

We ended up paying less, moving more, and with a better-managed commercial contract for the users who still wanted it — instead of writing a very large cheque to keep doing exactly what we were already doing.

If your infrastructure's core purpose is to do more of something every year, is your biggest vendor contract priced to reward that — or to tax it?

## Sources

- [Software licensing models — an overview](https://en.wikipedia.org/wiki/Software_license)
- [Science DMZ and data transfer nodes (ESnet)](https://fasterdata.es.net/science-dmz/)
