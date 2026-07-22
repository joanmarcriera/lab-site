---
title: "The negotiation I lost was my own promotion"
date: 2026-07-20
tags: [leadership]
aliases: ["/war-stories/the-negotiation-i-lost/"]
---

Two quick negotiations went well, and the one that mattered most to me personally, I lost. I lost it on purpose, more or less, and I want to be honest about how that happens — because it's rarely one dramatic decision. It's a hundred small ones, all pointing the same way.

First, the two that went well, because they set the scene.

We stopped renewing PagerDuty and moved our on-call and operational automation onto open-source Rundeck. It did what we needed, we already had the skills, and it took a recurring licence off the books. Not a heroic call — just the sort of unglamorous substitution that quietly frees up budget every year if you're willing to do the work.

Then the cloud maths. There was a serious pull towards putting our data in the public cloud, and the ingress story always sounds wonderful — getting data *in* is cheap or free. It's getting it back out that ends you. We ran the egress numbers for restoring at our scale, and even at a 66% discount, pulling 100 petabytes back out of the cloud in 2030 would need an insurance company to underwrite it, not a budget line. That single figure reframed the whole conversation. Cheap to enter, ruinous to leave, is not a home for a hundred-petabyte archive that has to outlive all of us.

So I could read a contract and I could read a bill. The negotiation I couldn't win was the one about my own career.

I was Deputy Head of Operations. The step up was Head of Operations, and I didn't get it. I stayed deputy. And the honest reason is not a conspiracy — it's a trade I kept making with my eyes open. Over years, I consistently chose the work over the politics. I pushed hard on what I believed the infrastructure needed. I antagonised people I'd have been wiser to bring slowly onside. Every time there was a choice between being right about the technology and being smooth about the room, I picked the technology. That is a real choice with a real price, and the price turned out to be the title.

I want to be careful here, because this is the part people get wrong when they tell these stories. Nobody wronged me. Leadership above me had every right to weigh things the way they did. Some leaders reward the person who fights for the work; some reward the person who manages the room; most quietly need both, and I turned up strong on one side of that and thin on the other. That's not a villain. That's a gap in me, and I own it.

Here's what I'd genuinely weigh differently, and what I wouldn't.

• **I'd invest earlier in the relationships, not later.** I treated politics as overhead — a tax on real work. It isn't. It's how the real work gets funded, staffed, and defended when you're not in the room. I learned that too late to spend it on myself.
• **I'd separate "being right" from "needing to be seen to be right."** I was often right. I didn't always need to win the argument in public to get the outcome. Some of my antagonising bought me nothing but the satisfaction of the antagonising.
• **I would not trade the outcomes back.** The systems I fought for are better for the fight. The retirements happened, the isolation happened, the cloud trap got avoided. If the cost of all that was a title I didn't get, that is a price I can look at squarely and still pay.

That last point is the one I hold onto. Because the tempting version of this story is the bitter one — the one where you were robbed, where the political operator won and the honest engineer lost. That story is a comfort and it's a lie. The truer, less flattering version is that I optimised for the thing I cared about most, and got exactly what that optimisation pays out. More impact, less title. I knew the shape of the trade. I just didn't fully feel the cost until it landed.

Would I choose the same again? Mostly, yes — with one edit. I'd keep fighting for the work. I'd just stop treating the people around it as an obstacle to route around, and start treating them as part of the system I was responsible for. You can be principled and still be politically literate. I proved you can be principled without it. I don't recommend the second one.

Ambition costs something either way. Chase the title and you can end up defending decisions you don't believe in. Chase the work and you can end up doing your best years one rung below where your name says you should be. There's no free version. There's only the question of which regret you can live with.

Mine's the deputy's chair, and a decade of infrastructure I'm proud of. I can live with that one.

If your promotion depended on being smoother about the politics than about the work — would you take the title, or keep the fight?

## Sources

- [Rundeck](https://www.rundeck.com/)
- [PagerDuty](https://www.pagerduty.com/)
- [Google Cloud Storage pricing (egress)](https://cloud.google.com/storage/pricing)
- [EMBL-EBI](https://www.ebi.ac.uk/)
