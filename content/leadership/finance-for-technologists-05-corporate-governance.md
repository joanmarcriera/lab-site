---
title: "Agency costs in the machine room: governance lessons from boardrooms, open source and my homelab"
date: 2026-07-19T20:00:00+01:00
series: "Finance for technologists · 5/6"
---

Corporate governance was the finance topic I expected to skim and ended up rereading. It is nominally about boards and shareholders. It is actually about a problem every engineering leader owns: what happens when the people controlling a system are not the people who suffer its failures.

### Agency costs, in native engineering units

Public companies separate ownership from control. Shareholders own; managers run. The separation is productive, it lets specialists manage and lets owners diversify, but it opens a gap: managers can pursue empire-building, perks and comfort at the owners' expense. Finance calls the leakage agency cost, a concept formalised in [Jensen and Meckling's 1976 paper](https://doi.org/10.1016/0304-405X(76)90026-X), and governance is the tooling built to contain it.

Engineers meet this daily without the vocabulary. The team that owns deployment risk is rarely the team demanding the risky feature date. The architect who mandates the framework does not carry the pager for it. Vendor lock-in is an agency problem: the person signing the contract has a three-year horizon; the systems inheriting it have a fifteen-year one. Once you have the concept, you see it everywhere, which is precisely what makes it useful.

### What boards teach us about review processes

The study of boards is a catalogue of oversight failure modes, every one of which has a direct software analogue.

• Monitoring is a public good, so it is underprovided. No single small shareholder will pay to watch management closely, since all shareholders share the benefit. Hence boards: delegated, concentrated scrutiny. This is why "everyone can review the change" reliably means nobody reviews the change, and why explicit code ownership beats diffuse goodwill.
• Independence works, capture kills it. The empirical evidence points one way: independent-majority boards are likelier to remove underperforming CEOs and less likely to wave through value-destroying acquisitions. But directors socially entangled with the CEO stop functioning as monitors, and firms with such connected boards lose value. The reviewer who reports to the author is not a reviewer.
• Prestige is not expertise. [Theranos](https://en.wikipedia.org/wiki/Theranos) assembled the most decorated board money could buy, statesmen, generals, zero biotech depth, and it oversaw nothing; John Carreyrou's [Bad Blood](https://en.wikipedia.org/wiki/Bad_Blood:_Secrets_and_Lies_in_a_Silicon_Valley_Startup) is the definitive account. Investors outsourced diligence to a famous letterhead. I have seen architecture review boards fail identically: seniority in the room, no one who has operated the class of system under review.
• Small groups decide better. [Yermack's research](https://doi.org/10.1016/0304-405X(95)00844-5) links smaller boards with higher firm value. My experience with change advisory boards matches: past a certain size they stop catching risks and start performing risk theatre.
• Busy monitors monitor nothing. Directors stacking six board seats give each a day or two a month. The engineering mirror is the principal engineer allocated 10% to ten projects, accountable for the health of none.

### Voice, exit, and the index fund problem

The corner of governance I find most personally relevant is shareholder activism, and at one point I sat down and analysed how BlackRock and Vanguard, the giant index managers, govern the companies they hold. My conclusion, in my own words: exit is not a credible tool for them. An index fund cannot sell the misbehaving company; it holds the market by construction. So influence flows through voice, in [Hirschman's classic framing](https://en.wikipedia.org/wiki/Exit,_Voice,_and_Loyalty): voting, engagement, persistent pressure on boards, pay and disclosure. Their sheer size means management usually moves before any vote is tallied.

Open source runs on the same physics. If your platform depends on a critical library, "exit", migrating off, is theoretically possible and practically ruinous, exactly like an index fund "selling the market". Which leaves voice: turning up in the issue tracker, funding maintainers, joining the foundation, doing the unglamorous governance work. Companies that consume critical dependencies while contributing nothing are shareholders who never vote and then act surprised by the AGM outcome. I have maintained open source projects for years; the users with governance standing when a hard decision arrives are the ones who invested voice early.

There is a darker reading of common ownership too: [Azar, Schmalz and Tecu](https://doi.org/10.1111/jofi.12698) argue that when the same few funds own every competitor in an industry, the incentive to compete softens. The evidence is contested, but the structural point stands: concentration of quiet influence deserves scrutiny, in capital markets and in software foundations dominated by one vendor's employees.

### Governance scales down: the homelab test

The claim I will defend over a beer: governance is not bureaucracy, it is the stuff that keeps working when enthusiasm and memory fail. So I applied the idea to the smallest organisation I run, my homelab.

I am simultaneously shareholder, board and management of that rack, which is precisely the governance nightmare the theory warns about: no separation, no monitoring, unlimited agency slack. My fixes were miniature corporate governance: every change to storage or backups gets written down before execution (disclosure); anything touching the backup chain waits a day and gets re-read cold (an independence hack, since I cannot hire a non-executive director for my ZFS pool); and quarterly I audit what I actually run against what I documented (audit committee, population: one). Ridiculous? Slightly. But the failure statistics of my own infrastructure since adopting it argue otherwise. Discipline is a substitute for supervision when supervision is unavailable.

One honest caveat: the research struggles to tie board structure directly to share price performance. Governance quality shows up mainly when things go wrong, which makes it, like backups and disaster recovery, chronically undervalued in good times. That parallel is the whole reason I take it seriously.

Where in your organisation does the person holding the risk lack the power to say no?

## Sources

- [Jensen & Meckling, "Theory of the Firm" — the original agency-cost paper](https://doi.org/10.1016/0304-405X(76)90026-X)
- [The Theranos story — https://en.wikipedia.org/wiki/Theranos — and John Carreyrou's book Bad Blood](https://en.wikipedia.org/wiki/Bad_Blood:_Secrets_and_Lies_in_a_Silicon_Valley_Startup)
- [Yermack, smaller boards and higher firm value](https://doi.org/10.1016/0304-405X(95)00844-5)
- [Hirschman's Exit, Voice, and Loyalty](https://en.wikipedia.org/wiki/Exit,_Voice,_and_Loyalty)
- [Azar, Schmalz & Tecu on common ownership](https://doi.org/10.1111/jofi.12698)
