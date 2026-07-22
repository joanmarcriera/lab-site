---
title: "Your internal platform is a product. Your users just can't churn."
date: 2026-07-19T20:55:00+01:00
---

Infrastructure people are trained to think in systems. Product people are trained to think in problems. After years of running services, I decided to borrow the second group's habits wholesale — by taking the least glamorous system I own through a full product cycle, exactly as a product manager would run it.

The cycle has four steps, each producing a working document: identify and define the challenge; ideate and design solutions; shape the proposition and user experience; then run agile experimentation and implementation. Four documents with my name on them later, I had accidentally become the product manager of the least glamorous product I know.

### Choosing a challenge without rushing to a solution

The discipline of the first step is refusing to solve anything. Pick an unmet problem, investigate its root cause, ask why it has not already been fixed — too expensive? too political? previous attempts failed, and why? — quantify roughly what fixing it is worth, and identify the most senior person who benefits, because that person is your sponsor. I covered the misdiagnosis trap earlier in this series; this was the systematic antidote.

My challenge: identity and access management across [EMBL](https://www.embl.org/). Behind the acronym sits a genuinely tangled system — HR records feeding LDAP schemas, business logic deciding group memberships, and a fan-out into everything from the HPC cluster and storage to email, wikis, cloud accounts and chat. Every new joiner at any of six European sites flows through it. So does every leaver, every role change, every permission grant. It is the circulatory system of the organisation, and like most circulatory systems it was noticed mainly when blocked.

### The persona that changed the argument

Product people insist you build a [persona](https://www.nngroup.com/articles/persona/) — a fictitious person who benefits most from a solution, carried through the whole process as a lens. Engineers roll their eyes at this. I did too, briefly.

Mine was a PhD student joining EMBL. Walk through their expectations for a moment. They chose a world-leading European laboratory. Transparency and knowledge-sharing are not perks to them; they are the ethics of their profession. They expect cross-site collaboration because their science demands it. And their very first structured experience of this organisation — before any science happens — is our onboarding: accounts, access, tools.

That reframing did more for the project's priority than any architecture diagram I have ever drawn. A slow, inconsistent onboarding is not an IT inconvenience. It is the organisation's first and loudest statement of its culture, delivered to exactly the people whose expectations are highest. First impressions are a product surface. Ours happened to be a login flow.

### Stakeholders: map the detractors, then recruit them

Step one also demands a stakeholder map — everyone affected or invested, plotted as supporter or detractor against their influence. The uncomfortable rule: detractors get an action plan. Not avoidance, not resentment; a plan to win their support or at least neutralise the blocking power, ideally by drawing on their actual expertise so they own part of the outcome.

For IAM the map wrote itself: HR owns the start of the joiner journey and the expectations set there; the Service Desk feels every pain point because users phone them, not me; the operations team are — as I put it in my deck to leadership — the Geppettos of the system, pulling strings nobody else can see. None of these groups reported to the same place. All of them could kill the project by lukewarm compliance alone. The map made that visible before it became fatal.

### Shipping it agile-style, in public

The implementation proposal borrowed the [lean startup playbook](https://theleanstartup.com/principles) — build-measure-learn, pivot when the evidence says so — but the parts I actually operationalised were humbler:

- A genuinely cross-functional team: HR, operations, helpdesk and Service Desk represented, not consulted-after-the-fact.
- Weekly objectives small enough to be tested, with the full picture drawn before implementation starts.
- An information radiator — a public Kanban board on tools we already owned — so progress and priorities are visible without asking.
- A monthly IAM users group open to anyone, where we report progress, take feedback, and reorder priorities in the open.

And the cost case, which is where product thinking earns its keep with a chief executive: no new posts. Existing tooling. Roughly ten extra licences. The project was already a commitment under a broader one-organisation initiative; the proposal simply argued that doing it collaboratively would deliver three things for the price of one — the IAM system, a measurable step in innovation culture, and the integration of teams that had never shipped anything together.

### What product marketing taught an infrastructure engineer

The other habit worth stealing is proposition design and positioning — the discipline of stating, in the user's language, what the offering does for them and why it beats the alternatives. Internal teams skip this because the users are captive. That is exactly backwards. Captive users cannot leave, but they can work around you, and [shadow IT](https://en.wikipedia.org/wiki/Shadow_IT) is what churn looks like when the exit is blocked. If you cannot write the one-paragraph proposition for your platform, your users are already writing it for you, less kindly.

My honest caveat: product frameworks assume more freedom than an internal platform owner usually has. I could not pivot away from federation constraints or pick my customer segment. But constraints make the product habits more valuable, not less — when you cannot change what you build, changing how it feels to use is the entire game.

### What I took away

• Define the challenge as a problem someone has, investigated to root cause, before proposing anything.
• Build the persona. Feel silly. Use it anyway — it will win arguments your diagrams cannot.
• Map stakeholders honestly and give every detractor an action plan.
• Ship in public: visible board, open feedback loop, short cycles.
• Write the proposition for your internal platform as if users could leave. Functionally, via workarounds, they can.

Next and last in this series: the one-page exercise I now ask every technology leader to do — the whole job on a single sheet of paper.

## Sources

- [Personas in UX — why the fictional user wins real arguments (Nielsen Norman Group)](https://www.nngroup.com/articles/persona/)
- [The lean startup principles: build-measure-learn](https://theleanstartup.com/principles)
- [Shadow IT — what churn looks like when the exit is blocked](https://en.wikipedia.org/wiki/Shadow_IT)
- [EMBL — the six-site European laboratory behind the example](https://www.embl.org/)
