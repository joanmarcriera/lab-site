---
title: "Debt, equity and the 3% rule: why software companies borrow almost nothing"
date: 2026-07-19T20:20:00+01:00
series: "Finance for technologists · 3/6"
---

I used to think capital structure was the one finance topic an engineer could safely ignore. A single contrast convinced me otherwise: software companies typically run on about 3% debt, automotive manufacturers on about 60%. The explanation turns out to be about engineers.

### Start from the theorem that says nothing matters

The [Modigliani–Miller theorem](https://en.wikipedia.org/wiki/Modigliani%E2%80%93Miller_theorem) states that in a perfect market, no taxes, no bankruptcy, no transaction costs, a company's value does not depend on its mix of debt and equity. This sounds useless. It is the opposite. It is a null hypothesis: since capital structure clearly does matter in the real world, every real effect must come from a named market imperfection. Find the friction, and you have found the reason. I rate this as one of the best pieces of intellectual hygiene in all of finance, and it generalises: my null for architecture reviews is now "in a world of free bandwidth and perfect reliability this choice would not matter, so which constraint are we actually arguing about?"

### Friction one: tax makes debt cheap

Interest payments are deducted before tax; dividends are not. So every pound of interest shields a slice of profit from taxation. This [interest tax shield](https://en.wikipedia.org/wiki/Tax_shield) is real value: a leveraged firm hands more total cash to its investors (debt holders plus shareholders) than the identical unleveraged firm, and the difference is exactly the tax saved.

The [adjusted present value](https://en.wikipedia.org/wiki/Adjusted_present_value) method puts numbers on this: value the project as if all-equity financed, then add the present value of the tax shield. A project that is NPV-negative when financed purely with equity can turn positive once the shield is counted. As someone who builds cost models for a living, I found this genuinely clarifying: financing structure is an input to project value, not an afterthought. For fixed debt, discount the shield at the cost of debt; for a stable debt-to-equity policy, fold it into the tax-adjusted [WACC](https://en.wikipedia.org/wiki/Weighted_average_cost_of_capital). I rebuilt the shield maths in my own spreadsheet because I did not believe it until I had computed it myself. Old habit.

### Friction two: distress makes debt expensive

If tax were the only friction, firms would leverage to the hilt. They do not, because debt raises the probability of financial distress, and distress destroys value in ways that are mostly indirect:

• Fire sales: needing cash and being known to need it means selling assets below their worth.
• Incentive rot: management with limited downside starts gambling; or disengages and job-hunts.
• Stakeholder flight: customers doubt your continuity, suppliers tighten terms, and employees, the mobile ones first, leave.

[Andrade and Kaplan's study of highly leveraged firms in trouble](https://doi.org/10.1111/0022-1082.00062) puts combined distress costs at roughly 10 to 20% of firm value. The striking part is that the process itself, lawyers and courts, is the minor cost. The major cost is the ecosystem quietly pricing in your possible death long before it happens. Anyone who has run a service through a vendor's public near-collapse has watched this dynamic from the outside: the technical product still worked; the trust did not.

### Why 3% versus 60%

Now the punchline. [Trade-off theory](https://en.wikipedia.org/wiki/Trade-off_theory_of_capital_structure) says each firm balances tax benefits against expected distress costs, and expected distress cost depends on what the assets are.

An automotive manufacturer owns plant, land and machines: stable cash flows, and assets that keep their value in a sale. Distress is painful but survivable, so carrying heavy debt to harvest the tax shield makes sense. A software firm's asset base is human capital plus reputation. In distress, both walk. The engineers leave, the customers churn, and there is nothing left to auction. So software firms rationally forgo most of the tax shield and run near debt-free.

For technology leaders this lands close to home in three ways:

• Retention risk is a balance sheet quantity. When your CFO resists leverage, they are pricing the fact that the company's value commutes home every evening.
• Funding structure is context for engineering strategy. A debt-heavy employer has covenant obligations and cash flow commitments that shape how it treats platform investment in a downturn. Read the balance sheet before the roadmap.
• Open source projects run the same trade-off without money. A project "financed" by a single maintainer's goodwill is leveraged to the hilt against distress: one burnout event and contributors, like customers of a distressed firm, quietly migrate. Foundations, co-maintainers and boring governance are the equity cushion. I fund my homelab projects the same way: spare capacity everywhere, obligations nowhere.

Interestingly, the evidence suggests real firms borrow less than pure tax optimisation would recommend. Executives are more frightened of distress than the spreadsheet says they should be. Having watched engineers over-provision for the failure modes they have personally lived through, I recognise the psychology, and I am not sure it is wrong.

One caveat: textbook treatments work with clean examples in which tax rates hold still and debt behaves. Real capital raising happens under time pressure with markets slamming shut; ask anyone who watched a struggling firm try to refinance into a closing window. The framework tells you the trade-offs; it does not promise the window stays open.

Next in this series: what happens when the company itself becomes the product, IPOs and acquisitions.

If your company's funding dried up tomorrow, which would go first: the assets or the people?

## Sources

- [Modigliani–Miller theorem](https://en.wikipedia.org/wiki/Modigliani%E2%80%93Miller_theorem)
- [Trade-off theory of capital structure](https://en.wikipedia.org/wiki/Trade-off_theory_of_capital_structure)
- [The interest tax shield](https://en.wikipedia.org/wiki/Tax_shield)
- [Andrade & Kaplan, "How Costly is Financial (Not Economic) Distress?" (Journal of Finance)](https://doi.org/10.1111/0022-1082.00062)
