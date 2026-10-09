---
title: "Puntos de montaje via ssh"
date: 2009-03-24
post_lang: es
tags: [linux, shell, ubuntu]
original_url: http://www.joanmarcriera.es/2009/03/24/puntos-de-montage-via-ssh/
summary: "Mounting a remote directory read-only over SSH with sshfs so a development machine can use real data without copying it."
draft: false
---

Hay quien a veces tiene instalado un programa en cierta máquina y no en otra, a eso se le llama distribución de recursos. ;) Esta configuración implica ventajas e inconvenientes, resulta que uno de los inconvenientes se puede solucionar. Veamos.

La primera ventaja es que en dos maquinas distintas se pueden tener versiones distintas de programas, una maquina con programas en producción y otra maquina con programas en desarollo, con sus fallos y sus downtimes.

El primer inconveniente es que tienes dos maquinas, una de las cuales no quieres tocar, pero que resulta que es la que tiene los datos, y por lo tanto necesitas replicar los datos. Que pasaria si esos datos fueran muchos gigas, incluso Teras?, o sencillamente fueran demasiados como para duplicarlos? Hacer pruebas con un muestreo reducido podria ser una solución, pero hay otra forma de sortear el problema.

SSHFS , o dicho de otra manera : tener dentro de una carpeta todo lo que otro usuario puede acceder en otra maquina. Si señor, montar una particion remota com si realmente ese disco remoto fuera el nuestro propio. (se aconseja montar readonly para no romper nada.;) )

Como lo hacemos? Vamos a interpretar que queremos jugar con unos ficheros que estan en A desde el pc B(nuestro desktop)

En A no hacemos nada. ;) (Es de producción y ese era el plan.)

En B: Instalamos sshfs des de la linea de comandos

```bash
$>sudo apt-get update && sudo apt-get install sshfs
```

O bién haceis click aqui : Install sshfs (`apt:sshfs`)

Para usar el disco remoto como si fuera nuestro es tan sencillo como hacer lo siguiente:

```bash
$>sshfs nuestrousuario@ipDelHostDondeEstanLosDatos:/directorio/que/queremos nuestro/directorio -o ro
```

Tachan, ya podemos trabajar con nuestas aplicaciones en desarrollo leyendo datos reales.

Para desmontar el punto de montaje:

```bash
$>fusermount -u nuestro/directorio
```

EDIT Notes: Me he encontrado que en algunos caso es necessario agregar usuarios al grupo fuse para que estos puedan hacer las conexiones y asi olvidarse de los problemas de permisos.

## 2026 note

sshfs still works as described, and `-o ro` for a read-only mount is still good practice. On current systems it uses FUSE 3, so unmounting is normally `fusermount3 -u`, and the `fuse` group is usually no longer needed on Debian and Ubuntu.
