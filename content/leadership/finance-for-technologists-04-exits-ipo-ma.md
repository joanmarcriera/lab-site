---
title: "The IPO pop and the poison pill: exit mechanics every senior engineer should know"
date: 2026-07-19T20:10:00+01:00
series: "Finance for technologists · 4/6"
---

Engineers learn exit mechanics the expensive way: on the day their employer announces one. I took the calmer route and studied the machinery before I needed it, and I wish this material were standard onboarding for anyone paid partly in equity.

### An IPO is a surprisingly bad deal, entered rationally

Going public is the classic exit, and it is startlingly expensive. The direct costs stack up: underwriting fees of several percent of the raise (often the single largest line), plus accountants quarterising years of financials, lawyers running due diligence, exchange listing fees, and the roadshow circus. All of that is visible and budgetable.

The larger cost is not. Underpricing, the gap between the offer price and the first day's closing price, has averaged mid-teens percentages in the US over decades, per [Jay Ritter's long-running data](https://site.warrington.ufl.edu/ritter/ipo-data/). The 2020 [DoorDash float](https://www.cnbc.com/2020/12/09/doordash-ipo-dash-trading-nyse.html) was the pantomime version: priced at $102, it opened at $182 and closed its first day up around 86%. Headlines called it a triumph. Viewed from the company's side, it was capital handed away: shares sold far below what buyers proved willing to pay hours later.

Why does everyone tolerate this? The standard theories are worth knowing because they are all about information:

• Information asymmetry: insiders know more than incoming investors, so newcomers demand a discount as insurance.
• Book-building: the bank assembles investor demand before pricing, and investors who reveal useful price information (limit orders rather than blank cheques) get rewarded with allocations. Underpriced allocations are, functionally, payment for information.
• Underwriter conflicts: the bank profits from happy allocated clients and a liquid aftermarket, both of which argue for pricing low. The issuer wants the opposite. Guess who sets the range.

For engineers, the practical reading is this. Your option strike and your lock-up period interact with a pricing process that is structurally tilted toward a first-day pop. Neither celebrating the pop nor raging at it is useful; understanding whose pocket it comes from is.

Then there are [SPACs](https://en.wikipedia.org/wiki/Special-purpose_acquisition_company), the shell-company shortcut that boomed and then deflated. A SPAC let a company reach public markets without traditional IPO diligence and disclosure, while handing the SPAC founders a hefty equity cut. Rising rates and regulatory tightening ended the party. My takeaway is general-purpose: any mechanism whose main feature is skipping scrutiny is borrowing risk, not removing it. We have this pattern in software too; we call it "temporarily" disabling the test suite.

Spotify's [direct listing](https://en.wikipedia.org/wiki/Direct_listing) showed the other escape route: skip underwriters entirely if your brand can carry its own demand. Most companies cannot, and pay the fee as a toll for access to institutional investors.

### M&A: the other exit, and its medieval siege weapons

The acquisition side reads like siege warfare. Most bids start friendly. When a target board refuses, the acquirer can go hostile: a tender offer straight to shareholders, over management's heads. Managers resist for reasons ranging from honest valuation disagreement to naked job preservation, and the [defences](https://en.wikipedia.org/wiki/Shareholder_rights_plan) they prepare in advance are wonderfully named:

• Flip-in pills: existing shareholders (except the acquirer) get discounted shares, diluting the raider mid-bid.
• Flip-over pills: target shareholders get rights to discounted shares of the acquirer post-deal.
• Golden parachutes: change-of-control payouts that inflate the price of victory.
• Staggered boards: even a successful acquirer waits years to replace directors.

I went in expecting to find these absurd. I came out more ambivalent: they are rational deterrents against coercive bids, and simultaneously excellent tools for entrenching mediocre management. Governance, as the next part of this series argues, is about exactly this tension.

The payment currency matters more than most employees realise. Cash deals transfer risk instantly: sellers are paid, done. Stock deals make target shareholders, including staff whose equity converts, co-owners of the combined company's synergy story. If the projected cost savings and revenue gains are real, you share the upside; if they are slideware, you share that too. Having watched acquisitions from inside the machine room, I can report that synergy estimates involving "consolidating infrastructure" deserve particular scepticism: nobody who wrote the deal model has ever migrated a datacentre.

### Where engineers fit

Three habits worth building before you need them:

• Read the deal structure, not the press release. Cash or stock, friendly or hostile, lock-ups and parachutes: these determine what actually happens to people like us.
• Price technical due diligence properly. In M&A the target has limited obligation to expose its internals, especially in hostile deals. Acquirers routinely buy systems sight unseen. If you are the engineer asked to assess a target's stack in three days, your report is load-bearing; write it like one.
• Treat integration as the project. The blunt framing of M&A value: the price you pay is set on deal day, but the value you get is built over the following two years, mostly by engineers and middle managers merging systems nobody documented.

I have worked through merger-synergy valuation models myself, and it is a humbling exercise in how few assumptions separate "accretive deal" from "value destruction".

If an acquirer offered your company stock instead of cash tomorrow, would you know what question to ask first?

## Sources

- [Jay Ritter's IPO data (underpricing statistics)](https://site.warrington.ufl.edu/ritter/ipo-data/)
- [DoorDash's first-day pop, CNBC](https://www.cnbc.com/2020/12/09/doordash-ipo-dash-trading-nyse.html)
- [Poison pills (shareholder rights plans)](https://en.wikipedia.org/wiki/Shareholder_rights_plan)
- [SPACs](https://en.wikipedia.org/wiki/Special-purpose_acquisition_company)
- [Direct listings](https://en.wikipedia.org/wiki/Direct_listing)
