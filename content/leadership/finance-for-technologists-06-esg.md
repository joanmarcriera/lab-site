---
title: "ESG without the halo: correlation, causation and why I still picked the boring index"
date: 2026-07-19T19:50:00+01:00
tags: [finance, leadership]
---

ESG is the rare subject where the marketing and the evidence live in different postcodes. Corporate sustainability content almost never treats "does this actually work?" as an open empirical question. It is one, and as someone who spends his professional life distinguishing signal from dashboard decoration, I wanted to answer it for myself.

### The evidence, stated carefully

The headline statistic in ESG marketing comes from [a meta-analysis by Friede, Busch and Bassen](https://doi.org/10.1080/20430795.2015.1118917) aggregating roughly two thousand empirical studies, most of which find a positive relationship between ESG and financial performance. Stated like that, it sounds settled. The right response is what every SRE does to a suspicious graph: ask about causality.

Profitable companies have slack to spend on sustainability, so performance may cause ESG rather than the reverse. Or competent management produces both good returns and good ESG, and the correlation is a shadow of a third variable. Most of those two thousand studies cannot distinguish these stories. Anyone who has "proven" that a dashboard metric drives revenue knows exactly how this works.

Real causal evidence exists, and it is elegant. You cannot randomly assign sustainability policies to companies, but close votes do it for you: a shareholder proposal passing 50.5/49.5 versus failing 49.5/50.5 is as good as a coin flip between otherwise similar firms. [Caroline Flammer's regression discontinuity study](https://doi.org/10.1287/mnsc.2014.2038) finds that narrowly passed sustainability proposals produced genuine abnormal returns, along with gains in labour productivity and sales growth. Modest, real, causal. That is the honest ceiling of what we currently know, and it is worth more than a thousand glossy correlation studies.

### My own analysis: two ESG funds and an uncomfortable conclusion

I ran the comparison myself: two US ESG index funds, one "integration" flavoured (stays close to the broad market while tilting weights by ESG score) and one "screening" flavoured (excludes low scorers outright), against the plain S&P 500, deciding as an investor.

Doing the analysis properly was deflating in the best way. Both ESG funds carry betas within a whisker of 1: they are the market, lightly rearranged. Their long-run performance since 2017 nearly overlaps the plain index, with divergences that appear and then mean-revert; no persistent outperformance in either direction. Which left, as the only durable differentiator, fees. The screened fund charges more, because screening is work.

My conclusion, and I stand by it: at a personal level I liked the screened fund, and I would like to believe rigorous screening earns a premium as the market's ESG baseline rises. But belief is not evidence, and on the evidence I would buy the plain S&P 500 and let the fee difference compound. If my ESG position costs me basis points annually and delivers approximately the market, then what I am buying is the screening itself, avoided harm, not returns, and I should be honest that it is a values purchase, priced in fees. Honest accounting beats comfortable narrative.

### Measurement is the whole game

Underneath every ESG debate sits a measurement problem that should feel familiar to anyone who has operated systems against SLOs:

• Ratings are models. Different agencies weight different factors and routinely disagree about the same company; [Berg, Kölbel and Rigobon documented the divergence](https://doi.org/10.1093/rof/rfac033) under the apt title "Aggregate Confusion". Choosing a rating is choosing a definition.
• Proxies get gamed. The moment a disclosure metric drives capital allocation, optimising the metric decouples from optimising the reality. [Goodhart's law](https://en.wikipedia.org/wiki/Goodhart%27s_law) does not care about your intentions.
• The measurable crowds out the important. Institutional investors concentrate on E and G, emissions and board structure quantify nicely, while S languishes, not because society matters less but because it resists a spreadsheet.

I spent years building monitoring for scientific infrastructure at EMBL-EBI, and the parallel is exact: what you can cheaply measure becomes what you manage, and the gap between metric and mission is where problems hide. ESG is not uniquely broken. It is an early-stage observability stack for corporate behaviour, complete with noisy exporters and disputed dashboards.

### Why engineers should care anyway

It would be easy to read the causation caveats as licence for cynicism. Wrong lesson. Three reasons this subject belongs in a technologist's toolkit:

• Infrastructure owns the E. Datacentre energy is a material ESG line for any serious tech company, and the people who control PUE, workload scheduling, hardware refresh cycles and region selection are not the sustainability team. They are us. When my homelab's electricity bill taught me to consolidate workloads onto fewer, more efficient machines, that was ESG optimisation at rack scale; the same maths runs a thousand times larger in production estates.
• Disclosure is becoming an engineering workload. Emissions reporting needs data pipelines, lineage and auditability. Badly built, it is fiction with a CSV export. This is our kind of problem.
• Capital reads these signals whether or not they are perfect. Part 5 of this series covered how index-scale investors use voice to press companies on governance and climate disclosure. Their pressure shapes budgets that eventually land on engineering roadmaps. Understanding the mechanism beats being surprised by it.

Six parts ago I started this series with the time value of money. The through-line, looking back, is that finance is mostly the discipline of making trade-offs explicit that engineers usually make implicitly: time against money, risk against return, control against accountability, values against fees. The vocabulary was the easy part. The habit of writing the trade-off down before deciding is the part I actually keep.

What would change in your organisation if the sustainability numbers were held to the same standard as the uptime numbers?

## Sources

- [Friede, Busch & Bassen — the ~2,000-study meta-analysis on ESG and financial performance](https://doi.org/10.1080/20430795.2015.1118917)
- [Flammer — the close-vote (regression discontinuity) study on sustainability proposals](https://doi.org/10.1287/mnsc.2014.2038)
- [Berg, Kölbel & Rigobon, "Aggregate Confusion: The Divergence of ESG Ratings"](https://doi.org/10.1093/rof/rfac033)
- [Goodhart's law](https://en.wikipedia.org/wiki/Goodhart%27s_law)
