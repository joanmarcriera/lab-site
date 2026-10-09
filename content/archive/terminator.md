---
title: "Terminator"
date: 2009-04-17
post_lang: es
tags: [debian, gnome, linux, shell, ubuntu]
original_url: http://www.joanmarcriera.es/2009/04/17/terminator/
summary: "A tip on Terminator, a terminal emulator that tiles several terminals in one window, with its main keyboard shortcuts."
draft: false
---

Aquellos que tengan por costumbre tener un par o tres de terminales a lo mejor encontraran útil distribuirse estas terminales de forma que las puedan ver todas a la vez, como un mosaico. Existe un gestor de terminales llamado [Terminador](http://software.jessies.org/terminator/). Como siempre facilmente instalable con apt, merge, yum, zypper o synaptic. Lo interesante de este gestor es que con los cuatro siguientes comandos puedes apañartelas muy bién, lo comprovareis.

- Ctrl+Shift+O - Divide en horizontal.
- Ctrl+Shift+E - Divide en vertical
- Ctrl+Shift+Right - Desplaza del divisor hacia la derecha.
- Ctrl+Shift+Left - Desplaza el divisor hacia la izquierda.
- Ctrl+Shift+Up - Divisor para arriba.
- Ctrl+Shift+Down - Divisor para abajo
- Ctrl+Shift+N - Next shell
- Ctrl+Shift+P - Previous shell
- Ctrl+Shift+C - Cut
- Ctrl+Shift+V - Paste

Y en Gnome F11 te da un full screen que a mi me es muy útil. Muchas gracias.

## 2026 note

Terminator is still packaged in Debian and Ubuntu (`apt install terminator`), and the split shortcuts above are still its defaults. `tmux` is the common alternative when you want the same tiling inside a terminal and over SSH.
