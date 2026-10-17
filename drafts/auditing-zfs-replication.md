---
title: "My backup audit said everything was fine. It was only looking at half of it."
date: 2026-10-12
draft: true
tags: [zfs, backup, homelab, reliability]
summary: "A ZFS replication audit that derives its dataset list from the replication tasks themselves, tiers staleness by schedule, and treats a disabled task as a failure."
---

## Problem

My storage box replicates its ZFS datasets every night to a second machine in the house. I
had a script that checked it: for each dataset, find the newest snapshot that exists on both
sides and print how old it is. It printed a tidy table and exited 0.

The list of datasets was an array at the top of the script. I wrote it when there were
eleven. By the time I looked again I was replicating nearly twice that, and the script
was still reporting "all current" about eleven. Nothing in the output said that the other
datasets had never been checked.

An audit that says "fine" about things it never looked at is worse than no audit, because
you stop looking.

## Approach

Three changes, none of them clever:

1. **Derive the list, do not maintain it.** The replication tasks already know what is
   replicated and where to. Ask them.
2. **Judge each dataset by its own schedule.** A dataset replicated monthly is not stale at
   eight days. A dataset replicated daily is.
3. **A disabled task is a failure.** Its last snapshot may match perfectly on both sides. It
   is still a hole, and it will stay one quietly.

## Steps

On TrueNAS SCALE the middleware will hand over every replication task as JSON:

```bash
ssh nas 'sudo -n midclt call replication.query'
```

Each task has `source_datasets`, a `target_dataset`, a `schedule`, and the `auto` and
`enabled` flags. That is enough to build "source : target : tier" for every dataset:

```python
for t in tasks:
    srcs, tgt = t["source_datasets"], t["target_dataset"]
    sched = t.get("schedule") or {}
    if not t.get("auto", True):               tier = "manual"
    elif str(sched.get("dom", "*")) == "1":   tier = "monthly"
    else:                                     tier = "daily"
    if not t.get("enabled", True):            tier = "DISABLED"
    for s in srcs:
        dst = tgt if len(srcs) == 1 else tgt + "/" + s.rsplit("/", 1)[-1]
        print(f"{s}:{dst}:{tier}")
```

The `dst` line matters. A task with several sources points at a *parent* dataset, and each
source lands underneath it by its last path component. Get that wrong and half the pairs
compare a dataset with nothing.

For each pair, list the snapshots on both hosts with their creation time in seconds:

```bash
zfs list -t snapshot -Hp -o name,creation -s creation -d 1 pool/dataset
```

`-H` drops the header, `-p` gives machine-readable numbers, `-d 1` stops at that dataset
without descending into children. The newest name present on both sides is the newest
common snapshot, and its age is the lag:

```bash
common=$(comm -12 <(echo "$src_snaps" | cut -f1 | sort) <(echo "$dst_snaps" | cut -f1 | sort))
newest=$(awk -F'\t' 'NR==FNR{c[$1];next} $1 in c' <(echo "$common") <(echo "$src_snaps") | tail -1)
```

Then the tier sets the limit: 26 hours for daily, 768 for monthly (31 days and some slack),
no limit for manual, and zero for disabled.

## Verify

Run on the evening of 12 October against the real fleet, as the baseline before a round of storage upgrades. Dataset names are changed and the
repeating rows trimmed; the tiers, snapshot names, lags and the summary line are as printed.

```
DATASET                                    TIER      NEWEST COMMON SNAPSHOT       LAG(h)
fast/apps                                  daily     @auto-2026-10-12_02-00           21
fast/applications                          daily     @auto-2026-10-12_02-00           21
tank/photos                                daily     @auto-2026-10-12_02-00           21
tank/timemachine                           daily     @auto-2026-10-12_03-00           20
tank/media                                 monthly   @auto-2026-10-01_02-30          285
tank/videos                                monthly   @auto-2026-10-01_02-30          285
tank/windows                               manual    @manual-copy-2026-07-13        2184  (manual tier — informational)
tank/vm-images                             manual    @manual-copy-2026-07-13        2184  (manual tier — informational)
tank/old-app                               DISABLED  @pre_reinstall_final           3445  <-- TASK DISABLED
tank/isos                                  DISABLED  @pre_reinstall_final           3445  <-- TASK DISABLED

SUMMARY: 26 tracked · 21 current · 2 stale/missing/disabled · 3 manual-tier
Replication NOT fully current — do NOT run risky storage operations.
```

The exit code was 1. Seventeen daily datasets are 20 or 21 hours old, which is that
morning's run. Four monthly ones are 285 hours old and correctly not flagged. And two tasks are disabled, their newest common snapshot a `pre_reinstall_final` from 143 days
ago. An audit working from a hand-kept list only tells you about what is on the list; this
one found them because it asked the tasks.

Whether a set of ISO images needs replicating is a fair question. The point is that I now
have to answer it, by re-enabling the task or deleting it, and not leave it switched off.

## Gotchas

- **Fail loudly when a host is down.** If the target is unreachable, every dataset looks
  like "no snapshots on the other side". Check SSH to both hosts first and exit with a
  different code.
- **Match snapshot names exactly.** A substring match pairs `auto-2026-10-09_02-00` with
  the wrong line sooner or later. Use `comm` on sorted names, or an exact awk lookup.
- **Snapshots made outside the middleware are invisible to it.** One of my datasets is
  snapshotted by a cron script, because the middleware refuses snapshot tasks on its own
  internal apps dataset. The replication task still covers it, so this audit sees it.
- **This answers one question only**: are the replication tasks current? It says nothing
  about datasets that no task covers at all. That needs a second audit that walks every
  filesystem in every pool.
- **The last line is for the reader, not the machine.** "Do NOT run risky storage
  operations" is there because the one time you need to know your second copy is current
  is just before you replace a disk or expand a pool.

## Further reading

- The runbooks around this, written so an AI assistant can execute them:
  [homelab-ai-skills](https://github.com/joanmarcriera/homelab-ai-skills).
- `man zfs-list`, for `-H`, `-p` and `-d`.
- In 2014 I solved the same problem for an Oracle database with rsync and cron:
  [a Data Guard-alike using bash and cron](/archive/2014/dataguard-alike-using-bash-and-cron/).
