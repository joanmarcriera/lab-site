---
title: "Risk, return and the hurdle rate: what engineers get wrong about 'safe' choices"
date: 2026-07-19T20:30:00+01:00
series: "Finance for technologists · 2/6"
---

Reliability engineering and finance are the same discipline wearing different clothes. Both estimate the gap between expected and actual outcomes, both price that gap, and both fail in the same way: by assuming failures are independent when they are not. Once I started reading corporate finance seriously, the parallel became impossible to unsee.

### Risk is variance, and variance has a price

Finance defines risk as dispersion: how far actual returns wander from expected returns, measured as variance or standard deviation. An asset returning a steady 3% is low risk. An asset averaging 10% but swinging between -40% and +47% in successive years, as some large tech stocks have, is high risk even though its average looks glorious.

The historical record is striking: over the twentieth century, riskier asset classes (small-cap stocks) massively outgrew safer ones (government bills), but with drawdowns brutal enough to ruin anyone forced to sell at the wrong moment. The premium exists because investors demand compensation for stomaching the swings; quite how large that compensation has been is itself a long-running debate known as the [equity premium puzzle](https://en.wikipedia.org/wiki/Equity_premium_puzzle). No swings, no premium.

Engineers make an equivalent trade daily and rarely name it. The "safe" choice, the incumbent vendor, the frozen dependency, the change freeze, is the Treasury bill of technology strategy. It minimises variance and quietly guarantees underperformance. I have watched platform teams congratulate themselves on stability while the organisation around them paid the opportunity cost. Low risk is not free; it is priced in foregone return. Finance just writes the price down.

### The two kinds of risk, and why only one earns a premium

The most transferable idea in the whole subject is the split between idiosyncratic and [systematic risk](https://en.wikipedia.org/wiki/Systematic_risk).

• Idiosyncratic risk is specific: one company's product flops, one disk dies, one engineer resigns. Hold many uncorrelated assets and these wash out. Because it can be diversified away for free, the market pays nobody for carrying it.
• Systematic risk is shared: recessions, rate rises, pandemics. It survives diversification. This is the risk that commands a premium.

In infrastructure terms: nobody should reward you for running a service that dies with one disk, because replication is cheap. Surviving correlated failure, a region outage, a supply chain shock, a cloud provider incident, is the expensive capability, and it should be justified the way an investor justifies systematic risk exposure: with an explicit view on likelihood, cost and compensation. At EMBL-EBI we ran services where the honest answer to "what happens if the site loses power?" had a price tag attached. Deciding not to pay it is a legitimate decision. Not knowing the price is negligence.

[Diversification](https://en.wikipedia.org/wiki/Diversification_(finance))'s fine print matters too: it only works while assets are uncorrelated. Portfolios that looked diversified in 2007 turned out to share one giant hidden dependency. Every SRE has seen the same postmortem: two "independent" replicas, one shared switch. Correlation is where diversification goes to die, in portfolios and in racks.

### CAPM, beta, and a healthy dose of scepticism

The [capital asset pricing model](https://en.wikipedia.org/wiki/Capital_asset_pricing_model) says an asset's expected return is the risk-free rate plus a premium proportional to its beta, its sensitivity to the whole market. High beta, high expected return. It is the standard machinery behind the cost of equity.

What I appreciate about honest practitioners is that they do not oversell it. Markets sit out of CAPM equilibrium often enough for entire industries, algorithmic trading, factor investing, momentum strategies, to exist by harvesting the gap. Beta is hard to measure, alpha is fleeting, and the "market portfolio" of theory is not something you can buy. As with any model I have run in production: wrong in the details, indispensable as a first approximation.

### The hurdle rate: your project's real competitor

Here is the sentence that most changed how I frame proposals. Your project does not compete against doing nothing; it competes against the return the company earns deploying the same money elsewhere at similar risk. That alternative return is the cost of capital, and it sets the discount rate from part 1 of this series.

Practical consequences for technical leaders:

• A platform investment promising 6% efficiency gains at a company whose cost of capital is 10% destroys value, however elegant the architecture.
• Riskier projects deserve higher hurdle rates. A speculative ML platform and a routine hardware refresh should not be discounted at the same rate, and pretending otherwise flatters the speculative one.
• "We saved headcount" claims should survive the question: saved relative to what alternative use of the spend?

At one point I pulled [Robert Shiller's public historical market data](http://www.econ.yale.edu/~shiller/data.htm) and estimated risk premia myself, spreadsheet and all. Recommended exercise: nothing builds respect for the equity risk premium like computing how noisy it is.

One caveat I will stand behind: numerical risk premia give false comfort when the underlying distribution is fat-tailed, and both markets and outages are fat-tailed. The variance number is a summary, not the story. Use it to rank options, not to feel safe.

The discipline I have kept: for any significant technical decision, write down expected return, expected variance, and correlation with what we already run. Three lines. It is astonishing how many architecture debates dissolve once those three lines exist.

What hurdle rate do your internal projects actually have to clear, and does anyone know the number?

## Sources

- [Capital asset pricing model](https://en.wikipedia.org/wiki/Capital_asset_pricing_model)
- [Systematic vs diversifiable risk](https://en.wikipedia.org/wiki/Systematic_risk)
- [Diversification and correlation](https://en.wikipedia.org/wiki/Diversification_(finance))
- [Robert Shiller's public historical market dataset](http://www.econ.yale.edu/~shiller/data.htm)
- [The equity premium puzzle](https://en.wikipedia.org/wiki/Equity_premium_puzzle)
