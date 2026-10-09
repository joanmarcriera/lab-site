---
title: "Clean RAM and swap"
date: 2011-04-19
post_lang: en
tags: [linux, server, shell]
original_url: http://www.joanmarcriera.es/2011/04/19/clean-ram-and-swap/
summary: "How to drop the Linux page cache, dentries and inodes with /proc/sys/vm/drop_caches."
draft: false
---

Clean the linux ram and swap it's easy.

```bash
# sync; echo 3 > /proc/sys/vm/drop_caches
```

Why this? sync writes all possible changes to HD. and drop_caches have this possible values:

- To free pagecache: `echo 1 > /proc/sys/vm/drop_caches`
- To free dentries and inodes: `echo 2 > /proc/sys/vm/drop_caches`
- To free pagecache, dentries and inodes: `echo 3 > /proc/sys/vm/drop_caches`

^_^

## 2026 note

The drop_caches interface is unchanged and still needs root (for example `sync; echo 3 | sudo tee /proc/sys/vm/drop_caches`). It only releases clean cache, not swap: to empty swap you would run `swapoff -a && swapon -a`, as long as there is enough free RAM to hold what is swapped out. On a normal system the kernel reclaims cache by itself when memory is needed, so dropping caches is mostly useful for benchmarking.
