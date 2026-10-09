---
title: "wrong ELF class: ELFCLASS64, o la importancia de las librerias dinamicas."
date: 2009-05-08
post_lang: es
tags: [linux, server]
original_url: http://www.joanmarcriera.es/2009/05/08/wrong-elf-class-elfclass64-o-la-importancia-de-las-librerias-dinamicas/
summary: "Why 32-bit binaries copied between servers fail with missing libstdc++ or wrong ELF class, and how to fix it with ld.so.conf, ldconfig and ia32-libs."
draft: false
---

Hemos cambiado unos ejecutables de un server a otro y ahora no quieren funcionar, no tenemos opción de recompilar por algun motivo que no viene al caso. Un problema que debemos solucionar, eso esta claro. Primer diagnostico:


```
server# ldd -d /home/user/tools/symmetrize
undefined symbol: _ZSt4cout, version GLIBCPP_3.2 (/home/user/tools/symmetrize)
undefined symbol: _ZSt4cerr, version GLIBCPP_3.2 (/home/user/tools/symmetrize)
undefined symbol: _ZNSs20_S_empty_rep_storageE, version GLIBCPP_3.2 (/home/user/tools/symmetrize)
linux-gate.so.1 => (0xffffe000)
librt.so.1 => /lib32/librt.so.1 (0xf7fc1000)
libstdc++.so.5 => not found
libm.so.6 => /lib32/libm.so.6 (0xf7f9b000)
libgcc_s.so.1 => not found
libpthread.so.0 => /lib32/libpthread.so.0 (0xf7f83000)
libc.so.6 => /lib32/libc.so.6 (0xf7e34000)
/lib/ld-linux.so.2 (0xf7fd2000)
```


Hay librerias que el programa necesita y no sabe donde encontrarlas. Pero las buscamos, y tenemos la primera sorpresa, estan ahí!!!


```
server# locate ibstdc++.so.5
/opt/vendor/lib64/support/libstdc++.so.5
/opt/vendor/lib64/support/libstdc++.so.5.0.3
/usr/lib/libstdc++.so.5
/usr/lib/libstdc++.so.5.0.7
/usr/lib32/libstdc++.so.5 
```


Que sucede entonces? Deberiamos recompilar la aplicación agregando las librerias de /usr/lib, o como minimo el path, en el compilado resultante. Pero ya habiamos descartado eso, no podemos hacerlo. La segunda opción es poner las librerias directamente en el path, y es que los ejecutables van a un sitio concreto ha buscar ciertas librerias mientras se ejecutan. Ponemos los path de las liberias en /etc/ld.so.conf, a mi me quedan de la siguiente manera:


```
server# cat /etc/ld.so.conf.d/*
# libc default configuration
/usr/local/lib
#luser libraries
/usr/lib
/usr/lib32
# Multiarch support
/lib/x86_64-linux-gnu
/usr/lib/x86_64-linux-gnu
```


Y ejecutamos:

```bash
# ldconfig
```

Con eso deberiamos haber conseguido que nuestro ejecutable encuentre las librerias. Si ese no fuera el caso es que nos faltan las ia32-libs, que son para usar binarios de 32 bits en arquitecturas de 64 bits. O dicho de otra manera, las librerias que acabamos de agregar con ldconfig son de 64 y nuestro ejecutable de 32, por lo tanto debemos instalar las ia32-libs para que en ese mismo path esten las librerias de 32.

## 2026 note

`ldd` and `ldconfig` work as described, but `ia32-libs` no longer exists. On current Debian and Ubuntu you enable multiarch with `dpkg --add-architecture i386` and install the `:i386` packages, and `libstdc++.so.5` comes from a legacy compatibility package. For one-off binaries, `LD_LIBRARY_PATH` or `patchelf --set-rpath` avoids touching system-wide configuration. Note that `ldd` can execute the binary it inspects, so do not run it on files you do not trust.
