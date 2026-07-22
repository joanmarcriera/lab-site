---
title: "Six Sigma thinking for infrastructure teams (no belts required)"
date: 2026-07-19T17:40:00+01:00
tags: [leadership, operations]
---

Infrastructure teams already do Six Sigma. Badly, informally, and under different names — but we do it. So I decided to learn it properly.

My study pile was the Lean Six Sigma certification track: the White Belt handbook and course pack, a set of certification manuals, and the full sequence of DMAIC training units, up through the Green Belt syllabus. This is the methodology born at Motorola and industrialised by GE: [reduce variation, eliminate waste, improve processes with data](https://asq.org/quality-resources/six-sigma). I approached it the way an SRE approaches any legacy system — expecting some rust, hoping for good bones.

The bones are excellent. Here is what transfers to running technology platforms, and what does not.

### DMAIC is a postmortem loop with better discipline

The core framework is [DMAIC: Define, Measure, Analyse, Improve, Control](https://asq.org/quality-resources/dmaic). Walking through it, anyone who has run a serious incident review will feel déjà vu.

Define the problem from the customer's perspective, not the system's. Measure the current state before touching anything. Analyse for root cause rather than symptoms. Improve by addressing that root cause. Then — and this is the phase that earns its keep — Control: monitor to make sure the gains survive contact with next quarter.

Tech is decent at the middle three and terrible at the bookends. We define problems from the infrastructure's point of view ("the cluster is slow") rather than the user's ("submissions take four hours to appear"). And we almost never close the loop with a control plan. We ship the fix, write the postmortem, and move on; six months later the same class of failure returns wearing a different hat. The Six Sigma answer is unglamorous: every improvement gets a metric, a threshold, an owner and an alert. If you cannot say how you would know the problem came back, you have not finished fixing it.

At EMBL-EBI, the improvements that stuck — in archive operations, in identity management across thousands of users — were precisely the ones where we had built the "did it stay fixed" instrumentation. The ones that regressed were the ones we celebrated and abandoned.

### DOWNTIME is the best description of toil I have read

Lean's eight wastes come with a mnemonic that could have been invented for operations teams: DOWNTIME — Defects, Overproduction, Waiting, Non-utilised talent, Transportation, Inventory, Motion, Extra-processing.

Translate each into infrastructure and the list turns into an audit checklist:

• Defects — rework: failed changes, rollbacks, tickets reopened.
• Overproduction — environments, replicas and reports nobody consumes.
• Waiting — the big one. Approval queues, CAB meetings, "waiting on the other team". Usually the largest waste and the least visible, because everyone is individually busy while the work sits still.
• Non-utilised talent — senior engineers performing manual restarts a script should own. This waste line item is why toil-reduction budgets exist.
• Transportation and Motion — data copied between systems that could share a source; humans swivel-chairing between consoles.
• Inventory — work in progress: the half-finished migrations accumulating risk in every backlog.
• Extra-processing — the manufacturing name for gold-plating. Building five nines for a service whose users need three. I have committed this one personally and can confirm the diagnosis.

The insight is not that waste exists; every engineer feels it. The insight is that naming waste categories makes it discussable without blame — the training is explicit that waste conversations are about the process, never about an individual's performance. That framing predates blameless postmortems by decades.

### Leadership owns the system

The materials lean heavily on the quality gurus, and the [Deming line](https://deming.org/a-bad-system-will-beat-a-good-person-every-time/) is the one worth framing: "A bad system will beat a good person every time."

The White Belt handbook makes the same point structurally — it starts with leadership: mission, modelled behaviour, systems thinking applied to key processes. Continuous improvement is not a grassroots hobby; it survives only where leaders treat the operating process itself as a product they own. As Deputy Head of Operations, my job on my best days was exactly that — not fixing the incident, but fixing the system that produced incidents, and protecting the time my team needed to do the same.

### What I would not import

Honesty section. First, belt ceremony: the hierarchy of White, Yellow, Green, Black and Master Black Belt maps how much statistics you have learned, and in weak organisations it becomes a caste system that gatekeeps common sense. Second, full statistical process control — control charts, capability indices, hypothesis-testing decision trees — is built for high-volume repeatable processes. Manufacturing runs thousands of identical units a day; most infrastructure work is lower-volume and higher-variance, and pretending otherwise produces impressive charts about nothing. Deployment pipelines and ticket queues are the exceptions where the statistics genuinely apply.

And a candid note on levels: the White Belt is vocabulary, not mastery — the handbook itself says as much. It is the entry point of a deep body of knowledge. Anyone presenting a White Belt as a quality credential has misread the belt; its value is that the vocabulary turns vague frustration about "process" into specific, fixable waste.

Fifty years of manufacturing improvement, free for the borrowing. We renamed half of it DevOps and pretended it was new; the other half is still sitting there, useful and unclaimed.

If you audited one week of your team's work against the eight wastes, which category do you suspect would win?

## Sources

- [DMAIC, explained by the American Society for Quality](https://asq.org/quality-resources/dmaic)
- [Six Sigma overview (ASQ)](https://asq.org/quality-resources/six-sigma)
- [The Deming Institute on "a bad system will beat a good person every time"](https://deming.org/a-bad-system-will-beat-a-good-person-every-time/)
