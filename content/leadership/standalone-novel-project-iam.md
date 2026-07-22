---
title: "Fifteen years of identity debt, and how we finally paid it down"
date: 2026-07-19T18:30:00+01:00
tags: [leadership, operations]
---

Nobody volunteers to replace an identity management system. When I took on the IAM overhaul at EMBL-EBI, the project had been left unattended for roughly fifteen years. The internal consensus was that it would take ten more to fix, because it could only be done in tiny pieces. Both beliefs were wrong, but understanding *why* they were wrong took a framework I only later found a proper name for.

### Why identity debt is the worst debt

Identity is where technical debt and organisational debt compound each other. Ours had reached an uncomfortable state:

• People had been able to create accounts at will — and they did. No contract signed, no way to contact the owners afterwards. Accounts with data access that no audit could explain.
• The business logic was undocumented, and there were more exceptions than rules. Some rules applied to a pair of two accounts only; even then, the two accounts implemented the exception differently.
• Nobody understood the whole. HR had delegated parts of identity to IT staff with no mandate for it. Every team touched identity; no team owned it.

At the scale of tens of thousands of accounts guarding hundreds of petabytes of research data, "we will get to it someday" stops being an option. It is a security incident waiting for a date. Anyone who wants to see what disciplined identity management looks like can read the [NIST Digital Identity Guidelines](https://pages.nist.gov/800-63-3/); our legacy system predated most of that thinking.

### Naming the beast: a novel project

The project-management literature — [*Managing the Unknown* by Christoph Loch, Arnoud De Meyer and Michael Pich](https://books.google.com/books/about/Managing_the_Unknown.html?id=ILrSioVAB50C) is the book I point people to — distinguishes execution projects (plan is known, discipline wins) from novel projects (uncertainty dominates, learning wins). The IAM replacement was unmistakably novel — not because the technology was exotic, but because the *unknowns outnumbered the knowns*.

When I sat down and mapped the uncertainties honestly, the table was sobering. Would the business logic even be implementable programmatically? Unknown. Would researchers, who had suffered the old system for years, actually want change? Unknown. Would HR embrace becoming the source of truth for identity — or find reasons not to do it "yet"? Risk. Would application owners help, or would helping us consume more of our time than doing it alone? Risk. Would the federation partners react badly? Unknown.

One entry in that table deserves a highlight: "Appetite for change in IT management" was the only item I could mark as *known*. They were afraid and needed reassurance. Knowing that was worth more than any architecture diagram, because fear you can plan for; surprises you cannot.

### What we actually did

The approach was iterative and social far more than it was technical:

• **Secure the cost first.** Once a budget range was accepted and IT management offered air cover, the conversation changed from "should we" to "how".
• **Push in all directions.** We asked every team who would help. From the willing, we documented the business logic. Then we went round again, validating that we had understood it. Each loop produced more logic, more feedback, and — importantly — more allies.
• **Set a date and a rollback.** We told everyone the flip date, built a tested rollback, and asked application owners to validate beforehand.
• **Push responsibility outward when silence answers.** Nobody validated, of course. So we went owner by owner and handed the responsibility back explicitly. That produced the feedback and the validations. The change shipped.

Loch, De Meyer and Pich make an argument that maps exactly onto this: when your management does not understand you are running a novel project, do not ask them to fund the whole journey. Define the budget for the first milestone, aim that budget at answering one question, and let the answer decide the next step. That is how you buy permission to learn.

### The lessons I keep

**The ten-year estimate was a cultural artefact, not an engineering one.** It priced in the toxicity of the topic — the years of "not my problem" — rather than the work. Once someone owned the problem end to end, the work was tractable.

**Undocumented logic is recovered socially, not archaeologically.** We did not reverse-engineer fifteen years of code in isolation. We extracted the rules from people, in rounds, and validated in public. The documentation was a by-product of building consensus.

**Forced validation beats requested validation.** Asking "please validate" produces silence. Naming a date, providing a rollback, and returning the responsibility individually produces answers. People engage when the consequence of not engaging lands on them.

**Success looks anticlimactic.** After the flip, everyone was congratulated and we moved on. No drama is the outcome you are aiming for. If your riskiest project ends with a shrug, you did it right.

**Buy boring where you can.** My conclusion after this project is blunt: IAM should not be an in-house hobby. A standard, widely-used identity platform means future engineers arrive with experience instead of needing a year of onboarding to tinker with a bespoke system. Uniqueness in identity infrastructure is a liability, not a differentiator.

There is a quiet epilogue. The organisation still runs multiple SSO identity providers and more two-factor systems than anyone would design on purpose — an estimated 10% of everyone's time leaks into identity friction. [CHECK — internal estimate from my own notes, not an audited figure.] Paying down one layer of debt exposes the next. That is not failure; that is what progress looks like in infrastructure.

If you listed your scariest project's unknowns in one honest table, would your leadership fund the first milestone — or are they still waiting for a ten-year plan?

## Sources

- [Managing the Unknown (Loch, De Meyer, Pich) — the best treatment of novel projects vs execution projects](https://books.google.com/books/about/Managing_the_Unknown.html?id=ILrSioVAB50C)
- [NIST SP 800-63 Digital Identity Guidelines — the public reference I wish that legacy system had followed](https://pages.nist.gov/800-63-3/)
