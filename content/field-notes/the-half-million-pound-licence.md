---
title: "The £500,000 licence I didn't buy"
date: 2026-07-20
tags: [finance]
aliases: ["/war-stories/the-half-million-pound-licence/"]
---

The cheapest data transfer is the licence you never renew. We were about to be asked for half a million pounds, and we didn't pay it.

At EBI, moving and archiving research data is not a side task — it is the mission. So the money we spend on data transfer is not overhead, it is the job. Which is exactly why the pricing model matters more than the software.

We had two products doing broadly the same thing. Globus, built by researchers for researchers, on a flat licence: £20,000 a year, move as much data as you like. And IBM Aspera, on the opposite model: the more data you move, the more you pay. For most companies that per-volume model is fine, because moving data is a cost they want to keep down. For an institution whose whole purpose is to move and archive ever-growing volumes of research data, it is structurally wrong. You are penalised for succeeding at your mission.

The trigger was simple. We were paying £20,000 a year for Globus and £40,000 a year for Aspera. Aspera was maxed out. To keep going, IBM wanted around £500,000 for a new licence — and then we would have been renting more capacity on top of that. The story people told afterwards was "the £140K swap". It was never a swap. The real number was the £500,000 new licence we avoided.

The first time I said we should move off Aspera, the answer was, "To what?" To Globus. "But we don't have Globus." Yes we do. We had forty servers of Globus already — forty badly-installed, underused virtual machines. I just needed to do it properly.

Here is how it went:

• **Used the vendor as free consultancy.** I asked Globus directly what a proper deployment should look like. They advised on sizing. We consolidated forty badly-installed VMs down to three physical servers — properly built this time. It took a year just to get the hardware.

• **Capped Aspera so it couldn't run away.** Aspera was a virtual machine. I moved it onto a hypervisor with a deliberately bandwidth-limited link, so usage physically could not exceed the licence we already had. That froze the problem while everyone migrated. No surprise overage, no £500K trigger.

• **Ran both in parallel and pointed everyone at the fast path.** With Globus live alongside Aspera, migrating became the obvious choice, so people moved themselves.

• **Turned parallel-running into leverage.** With a working alternative already carrying traffic, I told IBM plainly: if you want to keep the contract, Aspera has to perform better — fewer reconnects, fewer errors — and we want managed services for the same price. We got it, delivered through a third party doing business with IBM. That only worked because we weren't bluffing; the replacement was already running.

• **Won the users with arithmetic, not opinions.** Aspera is genuinely well-loved in genomics, and those users trusted it. I didn't argue about software. I showed them the numbers. Half a million pounds is a lot of money for researchers — money that buys sequencing, not licences. They were happy to start moving.

The lesson I keep from this one isn't "Globus good, Aspera bad". Aspera is a fine product and its model suits plenty of organisations. The lesson is that you have to match the pricing model to your mission before you match the features. If your reason to exist is moving more data every year, a contract that charges you more for moving more data will eventually corner you. It doesn't matter how good the transfers are.

And the tactics compound. The bandwidth cap bought time. The time let us build the three servers properly. The properly-built servers gave us a credible parallel service. The parallel service gave us leverage over IBM. The leverage plus the raw numbers won the users. Pull any one of those out and it's just a migration that drags on for three years while the old bill keeps climbing.

We ended up paying less, moving more, and with a better-managed Aspera contract for the users who still wanted it — instead of writing a cheque for £500,000 to keep doing exactly what we were already doing.

If your infrastructure's core purpose is to do more of something every year, is your biggest vendor contract priced to reward that — or to tax it?

## Sources

- [Globus](https://www.globus.org/)
- [IBM Aspera](https://www.ibm.com/products/aspera)
- [EMBL-EBI](https://www.ebi.ac.uk/)
