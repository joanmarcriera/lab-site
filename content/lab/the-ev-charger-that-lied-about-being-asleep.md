---
title: "The EV charger that lied about being asleep"
date: 2026-08-26
tags: [home-automation, reliability]
draft: false
---

We got back from holiday to find the car hadn't charged overnight, and the charger's status
screen said the thing it always says when this happens: the car is asleep, go and unplug it and
plug it back in. I've fixed that exact fault before, so I did the obvious thing. It didn't work.
That was the first sign this wasn't the fault I thought it was.

There turned out to be two separate root causes, and only finding both of them actually fixed the
night.

**The first was a ten-day blackout in the car's cloud integration.** It had gone unreachable while
we were away and reconnected with two schedule settings flipped backwards from correct — no
restart, no edit, just a bad state on reconnect. One of those settings is the only thing that
makes the car wake itself up and start charging every night; the other blocks daytime charging
entirely when it's set wrong. Together they silently combined into "never charges, ever," and nothing
about the car's own dashboard flagged it as wrong — it just looked like a car with charging turned
off, which is indistinguishable from a car someone had deliberately configured that way.

**The second cause is the one that actually mattered, and I missed it on the first pass.** The
charger's resting mode only draws from solar surplus, which is zero at midnight by definition. A
manual "boost" overrides that — but a boost is a timer, not a setting. It runs for a few minutes,
expires, and the charger falls straight back to surplus-only. Watching the logs afterwards, the
sequence was almost funny: real power flowing at full rate for about four minutes, then the mode
quietly reverting and the charge dying at zero watts. Nothing alerted on that, because nothing had
told the automation that a boost needs a chaperone to keep it alive past its own timer.

I'd also, a few nights earlier, half-diagnosed a similar-looking failure and filed it away as
"boosting delivers nothing when the car's asleep" — evidence that turned out to be simply a car
that wasn't plugged in that night. I'd carried that wrong conclusion into this diagnosis and it
sent me down the wrong path before the timer explanation clicked. Discarding a plausible-looking
but wrong data point turned out to matter as much as finding the right one.

The fixes, once both causes were clear, were straightforward: a drift guard that now self-heals a
flipped schedule setting instead of just alerting on it, in two stages — flip the specific switch
first, and if that hasn't taken effect shortly after, fall back to resending the car's entire
configuration from scratch; a nightly watchdog that notices if the car should be charging and
isn't, and retries before waking me up about it; and an automation that re-asserts the fast-charge
mode every few minutes through the overnight window, so a boost's timer expiring is no longer a
single point of failure. All of it is gated on the same "the smart tariff isn't managing this
right now" condition, so none of these safety nets can fight each other, or fight the actual
tariff-driven charging schedule on the nights it's working properly.

**What I'd do differently:** I'd have treated "status says asleep" as a hypothesis to check, not a
diagnosis to act on. The lesson that actually generalises here is that mode and status labels are
not ground truth — only the power reading is. A device can report exactly the state that matches a
familiar fault while the real cause is somewhere else entirely, and the fastest way to lose an
evening is to pattern-match the symptom instead of reading the number underneath it.

## Sources

- [Home Assistant](https://www.home-assistant.io/)
