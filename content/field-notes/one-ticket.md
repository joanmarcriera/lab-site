---
title: "An important GitHub org had no reachable admin. I opened one ticket."
date: 2026-07-20
tags: [operations]
aliases: ["/war-stories/one-ticket/"]
---

Here is a story with no dramatic recovery in it, and that's the whole point.

About a year in, a question surfaced that should never have to be asked: who actually owns our GitHub organisation? An important one. Real repositories, real people depending on it. And nobody could tell me. There was no reachable admin. The account that controlled it belonged to someone none of us could name or contact.

You can imagine the exciting version of this story. Some clever recovery. Some clever escalation. Some clever hack to prove I could take it back. That version would get more attention on the internet than the one that actually happened.

The one that actually happened is this. I opened a support ticket with GitHub. In a couple of emails they told me they couldn't disclose who owned the organisation — which is correct, they shouldn't. So I asked them a different question: can you pass a message to whoever does own it? They said yes. They relayed it. The unknown owner read it, contacted me back, and made me an admin.

And then I did the one thing that mattered more than getting in. I immediately added a second admin. So that this exact situation — an important org with a single, unreachable owner — could never happen again.

That's it. That's the story. A ticket, a relayed message, one admin grant, and a second admin grant. No drama. I believe in simple things.

I keep coming back to this one because it's a small, honest example of a rule I'd argue for anywhere:

• The boring correct move beats the clever one. Opening a ticket is not impressive. It worked in days, disclosed nothing it shouldn't, and left the platform's trust model intact. A clever workaround would have been a better anecdote and a worse outcome.
• A single point of human failure is exactly as real as a single point of machine failure. We build redundancy into disks, power supplies, network paths, availability zones — and then we let one unreachable person be the only human who can administer a critical account. That's a single point of failure wearing a lanyard. The fix is the same as it is for hardware: add a second one.

The reason I added the second admin in the same breath as accepting the first is that fixing the incident and fixing the cause are two different jobs, and most people stop after the first. Getting access solved my Tuesday. Adding a second admin solved every future Tuesday. If I'd walked away the moment I was in, I'd have simply moved the single point of failure from a stranger to me — and one day I'd be the unreachable name, and someone else would be opening the ticket.

None of this required cleverness. It required doing the plain, correct thing and then doing the second plain, correct thing that stops it recurring. That combination is undervalued precisely because it's undramatic. Nobody tells war stories about the ticket that worked.

So here's my question. What critical thing in your organisation has exactly one administrator right now — and how long would it take you to find out their name?

## Sources

- [GitHub organizations](https://docs.github.com/en/organizations)
- [GitHub Support](https://support.github.com/)
