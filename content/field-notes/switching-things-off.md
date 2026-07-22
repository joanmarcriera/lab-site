---
title: "Why I spent my last three years switching things off"
date: 2026-07-20
tags: [operations]
aliases: ["/war-stories/switching-things-off/"]
---

I spent my last years at EMBL-EBI retiring things. Decommissioning endpoints, killing protocols, switching services off. Nobody throws a party when you turn something off. There's no demo, no launch, no screenshot for the all-hands. I did it anyway, and I'd do every hour of it again.

The reason is the only reason that ever mattered here, and it isn't a technical one. This is not a normal company. It's research infrastructure for the human genome — the data plumbing underneath people studying cancer in children, people working on rare diseases. Important things that, if nobody takes care of them, simply do not get done. So none of this was ambition. I wasn't fighting for anything for myself. I was fighting for work that would quietly stop existing if I didn't do it, and that nobody outside would ever see.

There's a strange tax on doing this near the end. When you announce you're leaving, your proposals are taken *less* seriously, not more. The unspoken read is: you don't care any more, you're on your way out, you should already have your feet up. I heard the same thing pointed at others — someone would say "I've only got three years left here," as if three years were a rounding error. Three years is a massive amount of time. You can build or break an enormous amount in three years. I still don't understand not doing. And there's a hard fact underneath it: I knew, better than someone who'd joined a few months earlier, exactly what needed doing and in what order. Leaving didn't erase that. If anything it made it more urgent to write it all down.

Some of it was fighting inertia I couldn't wait out. One deliverable — turning our ITSM tool into the web front end for identity management — was promised to me five years running by a team that had a long history of missed deadlines and blocked projects. By the third year I stopped waiting and built the capability another way, with open-source Rundeck. What made me smile, grimly, is that the promise stayed on the roadmap for a fourth year and a fifth, long after we'd already worked around it. You don't need to deliver something the rest of us stopped needing two years ago. That's the cost of a project that's held up for years: eventually the world routes around it, and the only person who hasn't noticed is the one still promising it.

Here are the retirements I'm proudest of landing.

• **Thirty different endpoints in transfer services, gone.** Every one is a door that no longer needs guarding, patching, or explaining.
• **rsync over SSH — retired twice.** A whole protocol that can't really be secured, kept alive for exactly one service and one remaining client. The hard part wasn't the switch, it was convincing people that Globus isn't a giant torrent because it happens to be peer-to-peer. Patient explanation did more than any config change.
• **The old archive, put behind a clean API.** Users no longer reach into the database. They get an interface with a clear boundary — they can't touch what they shouldn't, and I can change what's behind it without breaking them.
• **Transfer services isolated onto their own storage.** At the start we had machines carrying 46 mount points, wired into essentially all the institute's storage. Picture one of those mounts shared with a 500-node cluster: the cluster hammers it, someone on the FTP side can't read or write, they raise a ticket — and by the time I look, twelve hours later, the system is perfectly healthy, because the cluster moved on. A ghost fault that heals itself before you can catch it. One dedicated transfer store made those ghosts disappear.

The thing I genuinely fear will die quietly after me is the least visible of the lot: virtual accounts. Replacing password-bearing transfer accounts, which belong to the outside world, with passwordless accounts that internal people sudo into — so that when someone leaves, their replacement can sudo in, read the Linux history, and inherit the actual knowledge instead of a mystery. On my last day I was still explaining it. If people understand it, it survives. If they just create accounts for the sake of it, it becomes another mess with my name faintly on it.

So what did I put in the handover that most handovers miss? Videos. A large pile of short ones. Not "click here, then here" — the manual already does that badly. My videos explain the *why*. Why this service exists, why it's shaped the way it is, why we retired the thing next to it. Documentation tells you which button to press. It almost never tells you why the button is there, and the why is the only part that stops the next person from cheerfully rebuilding the mess you spent three years removing.

None of this will ever look impressive on a roadmap. That was never the point. The point was that the science underneath keeps running whether or not anyone's watching the plumbing.

If you left your job in three months, would your best work be the shiny thing you shipped — or the quiet, unglamorous mess you finally cleared so nobody has to inherit it?

## Sources

- [Globus](https://www.globus.org/)
- [rsync](https://rsync.samba.org/)
- [Rundeck](https://www.rundeck.com/)
- [EMBL-EBI](https://www.ebi.ac.uk/)
