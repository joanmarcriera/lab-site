---
title: "How I came to own identity — by dumping every password hash in week one"
date: 2026-07-20
tags: [operations]
aliases: ["/war-stories/the-art-of-switching-things-off/"]
---

The oldest thing I ever switched off was ypcat.

First week into the institution. Before I'd found the good coffee, I found the oldest machine on the network. And I tried something I hadn't tried in twenty years — a bug we'd spotted back in my university days, aimed at NIS, the old Network Information Service that ypcat talks to. It worked. Within an afternoon I was holding the hash of every password in the institution.

I took it to the security lead and said: this is a problem.

He said, "Yes, I know."

That is how I came to own the identity process. Not through a reorg or a job description — through a twenty-year-old bug and a man who already knew. ypcat was the first thing I retired, because nobody needed it in the year 2000, and you certainly don't need it in 2025. The point of the story isn't the hack. The hack was trivial. The point is that switching that machine off was the most useful thing anyone had done to it in a decade, and it had been sitting there the whole time because retiring things is nobody's job until someone decides it's their job.

I decided it was mine.

Decommissioning is real engineering. This is the part people miss. We celebrate the launch, the migration, the shiny new platform — and we treat switching off the old thing as tidying up, something you get to eventually, an intern's ticket. It isn't. Turning a system off safely is often harder than turning a new one on, because the old thing has roots you can't see, and every one of those roots is someone's undocumented dependency. Done properly, retirement is where you actually pay down the debt instead of just refinancing it.

So over the years I retired a roster of things, on purpose:

• **ypcat / NIS** — the password-hash machine. Twenty-five years past its use-by date.
• **Abacus** — an in-house configuration-management system, a pile of Bash scripts for provisioning machines. Puppet, Ansible, Chef and CFEngine have existed for over twenty years. There is no reason to keep a homegrown thing made of Bash managing your fleet.
• **An XMPP server** — quietly serving a chat protocol almost nobody used any more.
• **LSF fronting transfer services** — IBM's batch scheduler, doing a job it was never meant to do.
• **Kubernetes in front of FTP** — this one still makes me smile. FTP is sticky: when a client reconnects it needs to land on the same container. Putting sticky-session FTP on Kubernetes is fighting the entire design of the platform to recreate a single old server. So we stopped.
• **Redis caching** — and this is the one I'm proudest of, because of how we killed it.

The Redis retirement was honest. We had a team of three developers, and with three people we could not keep that cache healthy. So we didn't quietly let it rot and we didn't pretend it was fine. We gave ourselves a timeline — as a team — to make it healthy. When the deadline came and we hadn't managed it, and we had other, more valuable things to build, we retired it. It was heartfelt. Nobody enjoys switching off something they built. But it was a decision made *with* the team, out loud, against a date we'd set ourselves — not one I imposed from above. That's the difference between an engineering decision and a management edict.

Now the failures, because the failures are where the real lessons live.

I once retired an rsync-over-SSH server. Textbook: found it, understood it, provided the alternative, switched it off. One week later, another IT person — same department, different team — recreated it. Not out of malice; they had a need and rsync-over-SSH was the tool they reached for. So I had to start the whole retirement process again, from zero, and the second time it took an extra year. What made it stick was that this time I had a section head from research backing me. **The lesson: a retirement isn't finished when you switch the thing off. It's finished when the alternative is genuinely real and someone senior enough is standing behind the decision.** Turn something off without both of those and it grows back.

The second failure is the one I think about most. We built an S3-write service in Java. It worked. It was tested. We were ready to release it. And then we unpublished it — deleted working software we'd finished — and we did it deliberately. Because we knew shipping it meant maintaining S3-write *alongside* the HTTP upload path that had existed since 2017, for the length of a long transition. And around that time it became clear management weren't going to renew the contract of one of the pivotal engineers on the team. Ship S3-write into that, and midway through the transition we'd be trying to hire a replacement — if we even had the headcount — while the rest of the team absorbed the gap and possibly walked because of it. So we retired working code before it ever ran in anger. Killing software that works can be the mature call. Sometimes the responsible thing is to not add the thing you spent months building.

And one more, smaller and more personal. Before we settled on Elastic APM for monitoring the Java processes, I wanted visibility fast, so I asked the team to stand up Spring Actuator endpoints. It went badly — and it was my fault. At that point the team didn't yet trust me enough to tell me *no*. So instead of pushing back, they wrote actuators to make me happy. All of it was wasted effort, and we retired the lot, because the goal was never to make me happy — it was to make the infrastructure easy to maintain, and those turned out to be two different things. **A team that can't say no to you costs you far more than a team that can.**

That's the through-line of every one of these. ypcat, Abacus, XMPP, LSF, Kubernetes-over-FTP, Redis, rsync twice, the S3-write we buried, the actuators I asked for and shouldn't have. Building is easy to be proud of. Switching things off — deciding, with your team and your evidence, what the world is better without — is the harder and quieter half of the job.

So here's my question: what's the oldest thing still running in your estate that everyone knows should be gone — and whose job is it to switch it off?

## Sources

- [NIS / ypcat (Network Information Service)](https://en.wikipedia.org/wiki/Network_Information_Service)
- [Puppet](https://www.puppet.com/)
- [Redis](https://redis.io/)
- [Kubernetes](https://kubernetes.io/)
- [Spring Boot Actuator](https://docs.spring.io/spring-boot/docs/current/reference/html/actuator.html)
- [Elastic APM](https://www.elastic.co/observability/application-performance-monitoring)
