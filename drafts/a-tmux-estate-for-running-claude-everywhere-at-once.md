---
title: "A tmux estate for running Claude everywhere at once"
date: 2026-09-05
tags: [engineering, ai-tooling]
draft: true
---

I run one Claude Code session per active project, and lately that's meant five or six terminal
windows open at once, each doing something different, each occasionally needing me right now and
otherwise needing to be left completely alone. Plain terminal tabs don't scale to that. You lose
track of which tab is which, the system clipboard doesn't reliably follow you between panes, and
if the machine restarts you're rebuilding your whole working set from memory.

So the actual problem wasn't "I need a terminal multiplexer" — I'd had tmux installed for years
and never configured it properly. The problem was "I need to know, at a glance, which of six
unattended agents just finished and is waiting on me," and a stock tmux config doesn't tell you
that.

What I built is a single `tmux.conf`, symlinked from the dotfile location into a versioned config
repo so it travels with the rest of my setup. A few choices did the actual work:

- **Session-per-project, window-per-task.** The session name is the project; a window's status
  flips to reverse video the moment it produces new output it thinks I haven't seen. For a Claude
  window, "new output" effectively means "it finished and wants my attention" — so the status bar
  becomes a passive todo list of which agents are done, without me polling anything.
- **Clipboard that actually works.** OSC 52 gets tmux selections onto the system clipboard
  directly, but it depends on a terminal preference being enabled, and I didn't want a workflow
  that silently breaks if that setting ever reverts. So `pbcopy` bindings sit underneath it as a
  fallback that works regardless — copy in tmux, paste anywhere on the Mac, no exceptions.
- **Sessions that survive a reboot, sort of.** `tmux-resurrect` restores the layout and working
  directory of every pane, and — because Claude Code sessions are the whole point — I told it to
  relaunch the `claude` process specifically wherever it was running. It deliberately does *not*
  restore pane contents; scrollback across a dozen panes is mostly noise, and it's cheaper to
  `claude --resume` into the actual conversation than to reconstruct a wall of stale terminal
  output.

I shipped the first version with the status bar pinned to the top, because that's where I'd seen
it done elsewhere. Within a day of actually living in it, I moved it to the bottom — it's where my
eyes already go for terminal chrome, and the reason for the "top" default turned out to be no
reason at all, just a starting point I hadn't questioned.

**What I'd do differently:** I'd have put the config in front of my own daily use before calling
it finished, rather than after. The status-bar position was a one-line fix, but it's the kind of
thing that only shows up when you actually sit with a tool for a working day instead of reading the
diff and moving on — and I nearly skipped that step because the config "looked right" on paper.

## Sources

- [tmux](https://github.com/tmux/tmux)
- [tmux-resurrect](https://github.com/tmux-plugins/tmux-resurrect)
- [TPM — Tmux Plugin Manager](https://github.com/tmux-plugins/tpm)
