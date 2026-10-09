---
title: "Testear la conectividad entre dos maquinas con NC"
date: 2009-03-22
post_lang: es
tags: [linux, shell]
original_url: http://www.joanmarcriera.es/2009/03/22/testejar-ports-amb-nc/
summary: "How to check that a TCP port is reachable between two machines by listening with nc on one and connecting with telnet from the other."
draft: false
---

Hay muchas maneras de saber si un puerto esta activo o no, una de las más clasicas es 'lsof', en el ejemplo siguiente nos darà que aplicación esta usando el puerto 80.

```bash
$> lsof -i:80
```

Pero hay algunas veces que eso no sirve, lo que queremos es saber si realmente se puede llegar de una maquina al puerto de otra. Para llevar a cabo esto necesitamos dos maquinas, A y B , la primera haremos que escuche en el puerto 54321 y la seguna comprovará que se puede llegar.

A (escucha)

```bash
$>nc -l -p 54321
```

B (conecta)

```bash
$> telnet A 54321
```

Si obtenemos un error es que algo interfiere la comunicación, posiblemente un firewall. Si no hay un mensaje de error significa que hemos abierto un canal de comunicación entre las dos maquinas, y es un canal de ida y vuelta por lo tanto podriamos chatear entre ellas sin problemas. Espero que os sea útil.

**Update:**

**Por otro lado ...** en algunos sistemas lo suficientemente viejos nos encontraremos que 'nc' es un "Client program for NEdit text editor" , en este caso puede ser practico copiar el binario desde otro sistema.

## 2026 note

The idea still works. `telnet` is rarely installed now, so `nc -zv A 54321` from machine B is the usual test, and OpenBSD netcat (the default on Debian and Ubuntu) listens with `nc -l 54321`, without `-p`. `ss -ltnp` replaces `lsof -i` for seeing what listens on a port.
