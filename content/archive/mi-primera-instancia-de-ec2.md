---
title: "Mi primera instancia de EC2"
date: 2010-11-20
post_lang: es
tags: [divertimento]
original_url: http://blog.joanmarcriera.es/mi-primera-instancia-de-ec2/
source: wayback
summary: "A short Spanish diary of launching a first Amazon EC2 instance, prompted by an article on cracking passwords with EC2 GPU instances."
draft: false
---

Hace unos dias me leí la siguiente documentación y me picó la curiosidad.

[Cracking Passwords In The Cloud: Amazon's New EC2 GPU Instances](http://stacksmashing.net/2010/11/15/cracking-in-the-cloud-amazons-new-ec2-gpu-instances/).

Así que hoy he conseguido lo siguiente:

- flipar con la validación telefonica de amazon.
- autenticarme unas 200 veces en sus servicios, parece que tengo las cookies hechas polvo.
- quemar un par de neuronas por sobrecarga de acronimos.
- crear mi primera instancia y loggearme por ssh.
- flipar con la cantidad de sistemas operativos disponibles. Incluso windows y uno propio de amazon. he elegido fedora.
- instalar htop y httpd en una fedora
- matar la maquina
- y ver que todo esto me ha costado 0 euros.

## 2026 note

The free tier that made this cost nothing in 2010 (a small free instance for the first year) has since been reworked, and AWS now offers new accounts a credit-based free plan instead, so check the current terms before assuming a test costs nothing. The "Amazon's own OS" is now Amazon Linux 2023, and the GPU instance families are much newer (the G and P series). Phone verification at sign-up and a long list of overlapping service names are still part of getting started.
