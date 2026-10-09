---
title: "Last.fm desde shell"
date: 2009-04-18
post_lang: es
tags: [divertimento, linux, shell]
original_url: http://www.joanmarcriera.es/2009/04/18/lastfm-desde-shell/
summary: "Listening to Last.fm radio from the command line with shell-fm on a low-memory machine."
draft: false
---

[Last.fm](http://last.fm) se tiene intención de hacer pagar ciertos servicios a alguna gente. [link](http://blog.wired.com/business/2009/03/lastfm-radio-to.html). De momento lo han pospuesto. Aún así esto es útil cuando estas algo justito de ram y lanzar firefox relentiza todo el sistema.

Para aquellos que quieran probarlo hay programita usar [last.fm](http://www.last.fm/) desde shell.

Para instalarlo es muy sencillo:

```bash
apt-get -y install shell-fm
```

No he encontrado demasiados comandos, el que uso por el momento es el siguiente:

```bash
shell-fm  lastfm://artist/${artist}/similarartists
```

Donde la variable artist es la que sustituimos por lo que queremos escuchar.

Muchas gracias.

## 2026 note

shell-fm is a small client for the old Last.fm radio protocol, which Last.fm has since retired, so I would not expect this to work today. For music in a terminal, tools such as `mpd` with `ncmpcpp`, `cmus` or `mpv` are the usual current options, and scrobbling to Last.fm is still possible through their separate scrobbler plugins or helpers.
