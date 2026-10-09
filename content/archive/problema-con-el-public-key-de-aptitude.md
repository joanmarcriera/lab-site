---
title: "Problema con el Public key de aptitude"
date: 2009-04-01
post_lang: es
tags: [debian, shell, ubuntu]
original_url: http://www.joanmarcriera.es/2009/04/01/problema-con-el-public-key-de-aptitude/
summary: "Fixing the apt 'no public key available' error by fetching the missing key from a keyserver and adding it to apt."
draft: false
---

Un server que estuvo en su momento un poco en desuso ha sido recuperado para nuevas funciones y debe ser actualizado pero no se deja por un tema de llaves. La solución es sencilla, ya que la llave no esta donde debería se le manda buscarla.

```
# apt-get update
Get: 1 http://ftp.fr.debian.org stable Release.gpg [386B]
...
Hit http://ftp.fr.debian.org stable/main Sources
Fetched 3B in 1s (2B/s)
Reading package lists... Done
W: There is no public key available for the following key IDs:
4D270D06F42584E6
W: You may want to run apt-get update to correct these problems
#
```

Si alguien se ha encontrado con algo asi alguna otra vez lo encontrará una chorrada, pero en mi caso he estado buscando la forma de saltarme la validación de llaves y me he encontrado con la solución. Aquí va.

Primera acción:

```bash
#> apt-key update
```

Segunda acción:

```bash
# gpg --keyserver subkeys.pgp.net --recv-keys 4D270D06F42584E6
```

Ya tenemos la nueva key.

```bash
# gpg --export --armor 4D270D06F42584E6| apt-key add -
OK
```

Ya la tenemos en la DDBB de aptitude. Y como comprovación que ya tenemos la llave:

```bash
# apt-get update
Get: 1 http://ftp.fr.debian.org stable Release.gpg [386B]
.....
Reading package lists... Done
#
```

Acepto que a lo mejor este no es un post muy lucido, pero para mi, la próxima vez que me encuentre con esto, va a ser practico que no veas, :) .

## 2026 note

`apt-key` is deprecated and removed from recent Debian and Ubuntu releases, and the `subkeys.pgp.net` keyserver pool no longer exists. Today the key is downloaded (for example from `keyserver.ubuntu.com` or the repository's own site), stored under `/etc/apt/keyrings/` or `/usr/share/keyrings/`, and referenced from the source entry with `signed-by=`.
