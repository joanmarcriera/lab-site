---
title: "1,000 machines in a day, or 3,000 unfinished a month later"
date: 2026-07-20
series: "War stories"
---

After the incident, we had to get an endpoint agent onto every machine we ran. CrowdStrike, on everything, quickly. That job became the cleanest measurement I've ever seen of the difference between automating work and doing it by hand. Same task, same deadline, same organisation. Two completely different outcomes.

My side automated it. We rolled CrowdStrike to 1,000 machines in a single day. Some were test boxes, some development, then the full thousand — and it was one day, not one heroic week. That number isn't a boast about effort. It's the opposite. It's what happens when the effort went in earlier, into the tooling, so that the rollout itself is almost boring. You describe the desired state once and let the machines converge on it. A thousand or ten thousand, the human effort is roughly the same.

The other side did it by hand. A month later, 3,000 of their machines still didn't have it installed. Not because the task was harder on their estate — it was the same agent, the same operating systems, the same instructions. It wasn't installed because a person was logging into a box, running the steps, moving to the next box, and repeating. At that rate a month isn't slow. A month is exactly what manual work at that scale costs. The scandal isn't that they were behind. The scandal is that "behind" was the predictable, arithmetic result of the method they chose.

And when I raised it, the answer I got was the line that stays with me: their manager says they cannot do it better.

Sit with that for a second, because it's the whole post.

• **"We can't do it faster" is almost never true.** What's true is "we haven't built the thing that would let us go faster." Those are different sentences with different owners. The first blames the work. The second is a decision a manager made, or failed to make, months ago.

• **The gap was never about talent or hours.** Both teams had capable engineers working hard. One team had spent its earlier time building the machinery to move at scale; the other had spent that same time doing today's tickets by hand, which guarantees you'll be doing tomorrow's by hand too. Manual work doesn't just cost you today. It borrows against every future day.

• **A crisis doesn't create the gap. It reveals it.** On a calm Tuesday, "we install things by hand" and "we install things with automation" look like style preferences. Then you're told to touch 4,000 machines this week, and one approach finishes and the other is still going a month later. The incident didn't make one team slow. It made an existing slowness impossible to hide.

That's the real lesson, and it isn't really about CrowdStrike, or even about automation as a tool. It's about what a team's response to scale tells you about the team. When you ask an organisation to do something large and fast, you find out instantly which parts built for scale before they needed it and which parts were quietly relying on there never being a bad week. The bad week always comes.

"Their manager says they cannot do it better" is the sentence I'd frame and hang on a wall, because it's where the whole thing goes wrong. It treats a capability gap as a fact of nature instead of a backlog item. Nobody is born unable to automate a software install. You're only unable to do it faster today because nobody was given the time, or the mandate, to build the capability yesterday. That's not the engineers' failing. That's a leadership choice about what you invest in when there is no fire — and the entire point of investing then is that you can't build the fire engine while the building is burning.

So when I see 1,000 in a day next to 3,000 in a month, I don't read it as one team being better than another. I read it as a report card on decisions made long before the incident. One team had been told to build for the day it would need to move fast. The other had been allowed to believe that day would never come.

When the next thing has to touch every machine you run, do you already know whether you'd finish in a day or still be going in a month — and if it's the second, whose decision made it so?

## Sources

- [CrowdStrike Falcon](https://www.crowdstrike.com/)
- [Ansible (configuration automation)](https://www.ansible.com/)
- [Puppet (configuration automation)](https://www.puppet.com/)
