---
title: "Pressing the button on your last Friday"
date: 2026-07-20
tags: [leadership, operations]
aliases: ["/war-stories/the-last-friday-button/"]
---

A departing engineer offered to upgrade our single-sign-on on their last Friday. I advised against it. The upgrade went ahead, and on Monday nothing worked. I still think the advice was right — and the story is about the organisation, me included, not the engineer.

Here is the situation. They owned the SAML single-sign-on — the thing that stands between a user and every internal service they log into. Time had been set aside, explicitly, for the upgrade to happen before they left. It hadn't. Then, on their last morning, hours before walking out of the door for good, they came to me with a choice: "push the button" and upgrade it now, or leave it exactly as it was.

I didn't take the decision. It wasn't mine to take, and I said so: that one belonged with their line management. What I did set out plainly was the condition, because I was the one who'd be left holding it.

• If you upgrade it and it still works on Monday, I'll take it on. I'll own it from there.
• If you upgrade it and it doesn't work on Monday, there is nobody to hand it back to. You're gone. There's no handover. There's a button.

The decision was taken to upgrade. Friday afternoon, the button was pressed, and everyone went home for the weekend.

Monday morning, nothing that used SSO worked. Not one service. A queue of tickets that grew every time another person tried to log in and couldn't. Every application that trusted the identity provider was now locked out, which — the whole point of single sign-on being single — was most of them.

Here is the part I'm quietly proud of, because it's the part that isn't luck. I had already lined up two external support quotes, and I already had management approval to spend against them. Not on Monday in a panic — before. So I didn't spend Monday finding help. I spent Monday using it. I brought in an SSO specialist that day.

What the specialist found is the real lesson, and it's got nothing to do with pressing buttons. The development, test and production environments had nothing in common. Not "some drift." Nothing. Different configurations, different assumptions, and — this is the one that tells you everything — one of them was running on a different operating system altogether. So whatever the departing engineer had validated somewhere was never going to survive contact with production, because production wasn't a bigger version of the thing they'd tested. It was a different thing wearing the same name.

Three things I took from it:

• Knowledge transfer is not a button pressed on the last day. It's the months set aside and not used. A handover is a person who can answer a question on Tuesday, not a final commit on Friday. If the plan is "they'll do it before they leave," you don't have a plan, you have a countdown.
• Never run an upgrade you can't support into a weekend. The question is never just "will it work when I press it." The question is "who is awake, paid, and competent to fix it when it doesn't — and are they reachable before Monday." If the honest answer is no one, the upgrade doesn't ship. It waits for a morning with a support rota behind it.
• Environments that drift apart guarantee this outcome. Dev, test and prod that share nothing aren't three environments, they're three separate systems and one dangerous assumption. You cannot rehearse a change you can only perform live. The rot was invisible right up until it was a wall of tickets.

I don't tell this as a story about one engineer. They were allowed to be in that position — allowed to hold a critical system alone, allowed to let the set-aside time run down, allowed to press a button into a weekend with no one behind them. That's not a personal failing. That's an organisation — and I was part of it, with a seat close enough to have pushed harder — that treated a single point of human knowledge as if it were a documented service. The button was always going to get pressed by someone. The only question was whether anyone had built the thing that catches it.

The good ending isn't that Monday went smoothly. It didn't. It's that the fallout was contained by decisions made before the fallout: a condition set out loud on Friday, two quotes and an approval already in hand, a specialist in the room by Monday afternoon. Preparation isn't what you do in the incident. It's what makes the incident boring.

All of this was some years ago. The environments were brought back into line at the time, and that estate has moved on since under people doing good work; I have no current access to it, and no knowledge of how it looks today.

What's the critical system in your estate that exactly one person understands — and what happens the Friday they leave?

## Sources

- [SAML](https://en.wikipedia.org/wiki/Security_Assertion_Markup_Language)
- [Bus factor — the risk of knowledge held by one person](https://en.wikipedia.org/wiki/Bus_factor)
