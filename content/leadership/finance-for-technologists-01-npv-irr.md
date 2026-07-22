---
title: "NPV for engineers: why your build-vs-buy gut feeling needs a discount rate"
date: 2026-07-19T20:40:00+01:00
series: "Finance for technologists · 1/6"
---

Engineers argue about build-vs-buy with spreadsheets that have no concept of time. I did it for years. A licence costs £40k a year; building takes six months of one engineer; therefore building "pays for itself" in under two years. Case closed.

It took an executive finance programme I took at Oxford's Saïd Business School to take that reasoning apart properly. The core concept is the [time value of money](https://en.wikipedia.org/wiki/Time_value_of_money): a pound today is worth more than a pound next year, because today's pound can be invested, because inflation erodes buying power, and because future money carries risk that it never arrives. None of this is exotic. But almost no engineering business case I have reviewed in my career actually applied it.

### The tool: net present value

[Net present value](https://en.wikipedia.org/wiki/Net_present_value) is the discipline of putting every cash flow on a timeline and discounting each one back to today using a rate that reflects what the money could earn elsewhere. Sum the discounted flows. Positive means do it; negative means do not. That is the whole rule.

The part that changes engineering conversations is the discount rate. Say your company's cost of capital is 10%. A saving of £100k arriving in year four is worth roughly £68k today. Suddenly the self-built tool that "saves £400k over four years" against £300k of upfront engineering time is a much closer call, and that is before you price the maintenance tail, which in my experience nobody prices honestly.

I ran infrastructure at EMBL-EBI, where compute and storage decisions routinely spanned five-year horizons. We were disciplined about capacity models and refresh cycles. We were far less disciplined about the fact that money spent in procurement year one and money saved in operations year five are different currencies. NPV gives you the exchange rate.

### Where IRR bites back

The [internal rate of return](https://en.wikipedia.org/wiki/Internal_rate_of_return) is the discount rate at which a project's NPV lands exactly at zero. It is popular because it produces a single seductive percentage: "this project returns 23%". Its failure modes are well documented, and they map beautifully onto infrastructure work:

• Cash flows that change sign more than once can produce multiple IRRs. A platform migration often looks like this: outflow now, savings for years, then a decommissioning or contract-exit cost at the end. Two valid IRRs, no valid decision.
• Projects where the money arrives before the costs (vendor credits, prepaid commitments) can produce an IRR that points the wrong way entirely.
• Some perfectly good projects have no IRR at all, because the NPV is positive at every discount rate.

The practical rule I follow: compute NPV first, always. Use IRR as a communication device when the cash flow pattern is simple, and never let it overrule NPV when the two disagree.

### Payback period, the engineer's comfort blanket

[Payback period](https://en.wikipedia.org/wiki/Payback_period) is how most infrastructure refreshes get justified: "the new hardware pays for itself in 30 months." I have written that sentence myself. The problem is that payback ignores the time value of money and, worse, ignores everything that happens after the payback point. A project that repays in year three and then compounds savings for a decade loses to a project that repays in year two and then flatlines. That ranking is wrong, and payback cannot see it.

Payback still has a use: it is a crude liquidity check. If your budget genuinely cannot survive a long repayment window, that constraint is real. But it is a constraint, not a valuation.

### What this changes in practice

Three habits I have adopted:

• Every proposal above a threshold gets a cash flow timeline, not a totals table. Costs and savings by year, discounted. The discipline of drawing the timeline exposes wishful thinking faster than any review meeting.
• I ask finance for the discount rate before building the case, not after. It reframes the conversation from "is this cheap?" to "does this beat what the company earns on its money?"
• Perpetuity maths for steady-state costs. A recurring £20k annual SaaS bill at a 10% discount rate is a £200k liability in present value terms. Saying "we carry a £200k liability for this tool" lands very differently in a budget discussion than "it's only £20k a year".

One honest caveat. The precision of NPV is theatre if your inputs are fiction, and engineering estimates usually are. The model does not rescue bad estimates; it makes their consequences visible. I treat the NPV number as a structured argument, not an oracle. That, I think, is the right level of respect for it.

The homelab version of this lesson: I stopped "saving money" by buying second-hand servers whose electricity cost, discounted over five years, exceeded the cloud bill they replaced. The maths did not care about my feelings on owning hardware. It rarely does.

## Sources

- [Time value of money](https://en.wikipedia.org/wiki/Time_value_of_money)
- [Net present value](https://en.wikipedia.org/wiki/Net_present_value)
- [Internal rate of return (and its failure modes)](https://en.wikipedia.org/wiki/Internal_rate_of_return)
- [Payback period](https://en.wikipedia.org/wiki/Payback_period)
