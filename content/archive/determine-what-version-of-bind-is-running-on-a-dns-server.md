---
title: "Determine what version of bind is running on a dns server."
date: 2009-07-31
post_lang: en
tags: [linux, server, shell]
original_url: http://blog.joanmarcriera.es/determine-what-version-of-bind-is-running-on-a-dns-server/
source: wayback
summary: "A one-line dig query that asks a DNS server which BIND version it reports, to check whether it is exposed to a known BIND 9 bug."
draft: false
---

There is a bug on bind9, like [this one](http://www.cyberciti.biz/tips/bind-dynamic-update-dos.html).

So, how to know if you can exploit it?

```
dig -t txt -c chaos VERSION.BIND @<SERVER_IP>
```

It's possible to hide the bind version, so do not expect to get it from all of them.

## 2026 note

The query still works: `dig +short CH TXT version.bind @server` asks for the same CHAOS-class record. Administrators can hide or replace the answer with the `version` option in the `options` block of `named.conf`, so the reply is only what the server chooses to report, and a missing version does not mean the server is patched. The bug linked above was a BIND 9 dynamic-update denial of service from 2009; BIND 9.16 and later are long past it, and current releases are tracked by ISC security advisories.
