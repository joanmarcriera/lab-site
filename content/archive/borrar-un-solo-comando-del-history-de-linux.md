---
title: "Borrar un solo comando del history de linux"
date: 2009-05-11
post_lang: es
tags: [debian, linux, server, shell, ubuntu]
original_url: http://www.joanmarcriera.es/2009/05/11/borrar-un-solo-comando-del-history-de-linux/
summary: "How to delete a single entry from the bash history, for example after typing a password on the command line."
draft: false
---

Puede pasar que nos distraigamos y pongamos un password en la linea de comandos, por lo que este queda en el history. Es importante borrarlo, y se pude hacer de la siguiente manera:

```bash
# history -d 5
```

Donde 5 es el numero de linea donde se encuentra nuestro comando. Esperemos que no sea necesario hacerlo muy a menudo.

## 2026 note

`history -d N` still works in bash; the entry is removed from the in-memory list and the history file is rewritten when the shell exits (or after `history -w`). Better still is to avoid the problem: with `HISTCONTROL=ignorespace` any command typed with a leading space is never recorded, and secrets are best read from a prompt or a file instead of being passed as command-line arguments, since those are also visible in `ps`.
