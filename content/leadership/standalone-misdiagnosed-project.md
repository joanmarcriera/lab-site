---
title: "The most expensive project mistake is made on day one"
date: 2026-07-19T18:40:00+01:00
tags: [leadership]
---

Projects fail at diagnosis, not at delivery. That is the single most useful idea I have about running projects, and it matches everything I have seen in twenty years of running infrastructure.

The framing is simple. A project is a weapon of organisational change: it exists to turn strategy into something concrete. But not all projects are the same animal, and the management system that makes one type succeed will quietly kill another. (If you want a more playful version of the same insight, [Eddie Obeng's four project types](https://business.adobe.com/uk/blog/basics/4-types-of-projects-which-kind-are-you-leading) — painting by numbers, going on a quest, making a movie, walking in the fog — carve up the same space.)

### Three types, three playbooks

• **Execution projects.** Most of the plan is knowable up front. Think a data-centre migration with a fixed inventory. Success is measured against schedule, budget and predefined targets. Discipline wins.
• **Novel projects.** Significant uncertainty or genuine innovation. You cannot plan your way through the unknown; you experiment, learn and pivot. Success is judged on outcomes *and* on the quality of the process that got you there.
• **Change projects.** The deliverable is people doing things differently. New processes, new systems, new behaviour. Success is stakeholder buy-in and adoption rates — not the go-live date.

Reading that list, most technology leaders nod along. Then they go back to the office and run everything with the execution playbook, because that is the one with the comfortable Gantt chart.

### What misdiagnosis looks like from the inside

Asked once to describe a misdiagnosed project I had lived through, I did not have to think hard.

I have watched an ITIL tooling implementation at a research organisation run for years past its intended timeline. The pattern was textbook. The product was selected partly because comparable institutions had it — if a bigger lab uses it, it must be good. The project was managed on schedule alone, so quality questions had nowhere to land. Concerns from the IT teams who would live with the result were noted and dismissed. And when licensing reality collided with budget reality, the answer was to drop the capability rather than reconsider the tool.

The outcome? The legacy system it was meant to replace kept running in parallel, because not every client of the old system made it into the migration plan. Milestones were celebrated — an MVP that could receive tickets, then a "minimal usable product" that could route them, mostly. The schedule was defensible at every step. The adoption never came.

None of the people involved were incompetent. The project was simply diagnosed as an execution project — buy tool, configure, deploy — when it was a change project wearing an execution project's clothes. Every IT team was being asked to change how they worked and what they measured. Nobody managed that part, because the plan had no line for it.

### The signs to watch for

There is a short list of misdiagnosis symptoms I now use as a checklist:

• People miss deadlines or budgets and it is clearly not their fault — a rigid plan was imposed on work with high uncertainty.
• An execution team is given the freedom of a novel project — no discipline, scope creep everywhere, "agile" used as an excuse.
• A business-process project fails because nobody recognised it as a change project — the technology landed, the behaviour did not.

There is a fourth sign I will add from experience: **success theatre**. When a struggling project keeps producing celebrations, ask what type of project the celebrations are measuring. A ticket system that receives tickets is an execution milestone. A ticket system that teams *choose* to use is a change milestone. They are not the same thing, and only one of them pays the bills.

### The sunk cost trap

Misdiagnosed projects rarely get re-diagnosed, and the reason is human, not technical. Once a project has consumed years and budget, a new project manager inherits a Catch-22: changing direction means owning the admission that the direction was wrong. So investment continues on sunk-cost momentum. I have asked a version of this question aloud — can one person turn such a project around, or is it wiser to let it run its course? The honest answer is that some cultural corrections need critical mass before they can even be discussed. If you are the only person in the room saying "change management without a CMDB is not change management", you are probably early, not wrong.

### What I do differently now

• At intake, I ask one question before any planning: what type of project is this? If the honest answer is "change", the stakeholder map gets built before the technical plan.
• I define success per type. Execution: schedule and spec. Novel: validated learning per pound spent. Change: adoption, measured monthly, reported to the sponsor.
• I hunt for the misdiagnosis symptoms in quarterly reviews, not just at kick-off. Projects drift between types; a novel project becomes an execution project once the unknowns resolve, and the management style should follow.

Diagnosis is free. Misdiagnosis is the most expensive line item you will never see on a budget.

What would change in your portfolio if every project had to declare its type — and its real definition of done — before funding?

## Sources

- [Eddie Obeng's four types of projects (a well-known public project-typology framework)](https://business.adobe.com/uk/blog/basics/4-types-of-projects-which-kind-are-you-leading)
- [More on how I think about diagnosing IT projects](https://blog.riera.co.uk)
