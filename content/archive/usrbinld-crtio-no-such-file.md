---
title: "Varnish is complaining"
date: 2010-10-04
post_lang: en
tags: [linux, shell]
original_url: http://www.joanmarcriera.es/2010/10/04/usrbinld-crtio-no-such-file/
summary: "Varnish failed to start after a Debian etch to lenny upgrade because crti.o was missing; installing libc6-dev fixed it."
draft: false
---

I've just upgraded a development server and I've found myself with this issue: Starting Varnish

```
Internal error: cc(1) complained:

/usr/bin/ld: crti.o: No such file: No such file or directory

collect2: ld returned 1 exit status
```

Yes, this is a plone-farm using varnish, and I've just upgraded from etch to lenny. So theoretically should not be a big deal. Thinking a bit I just remembered that 15 minutes ago I've also upgraded the kernel, so, my be the headers.... no they are ok. So I google a bit , and [voila](http://ubuntuforums.org/showthread.php?t=670930).

```bash
apt-get install libc6-dev
```

And that's all folks, just a group of libraries changing it's version.

```
libc6-dev linux-libc-dev
```

Hope you find it useful.

## 2026 note

Varnish 2.x compiled its VCL to C at start-up, which is why it needed a C compiler and the libc development files; current Varnish versions still compile VCL through the system C compiler, so a missing `libc6-dev` (or `build-essential`) produces the same kind of error. The fix is the same on current Debian and Ubuntu.
