---
title: "Watch mysql processlist"
date: 2010-01-18
post_lang: en
tags: [linux, minicommands, server, shell]
original_url: http://www.joanmarcriera.es/2010/01/18/watch-mysql-processlist/
summary: "Two ways to watch the MySQL process list live: watch with mysqladmin, or the mytop tool."
draft: false
---

Option a)

```bash
$ watch -n 1 mysqladmin --user=<user> --password=<password> processlist
```

Option b) Install [mytop](http://jeremy.zawodny.com/mysql/mytop/)

Enjoy.

## 2026 note

Both still work, but a password on the command line is visible in `ps` output, so put the credentials in the `[client]` section of `~/.my.cnf` and drop the `--password` option. `mytop` has largely been replaced by `innotop` and `mariadb-admin`/`mysqladmin` with `SHOW FULL PROCESSLIST`.
