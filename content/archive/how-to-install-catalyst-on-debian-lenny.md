---
title: "How to install Catalyst on debian lenny"
date: 2010-03-24
post_lang: en
tags: [debian, linux]
original_url: http://www.joanmarcriera.es/2010/03/24/how-to-install-catalyst-on-debian-lenny/
summary: "Installing the Catalyst Perl web framework and its common modules on Debian Lenny by pulling packages from the unstable repository."
draft: false
---

I’ve readed [this](http://search.cpan.org/dist/Catalyst-Manual/lib/Catalyst/Manual/Tutorial/01_Intro.pod) and made some minor modifications.

```bash
$sudo su

#echo "# repo for catalyst" >> /etc/apt/sources.list

#echo "deb http://ftp.us.debian.org/debian/ unstable main" >> /etc/apt/sources.list

#apt-get clean && apt-get update

#apt-get install sqlite3 libdbd-sqlite3-perl libcatalyst-perl \
libcatalyst-modules-perl libdbix-class-timestamp-perl \
libdatetime-format-sqlite-perl libconfig-general-perl libhtml-formfu-model-dbic-perl libterm-readline-perl-perl \
libdbix-class-encodedcolumn-perl libperl6-junction-perl \
libtest-pod-perl gcc make libc6-dev
```

That’s all.

## 2026 note

Debian Lenny is long end-of-life, and mixing the unstable repository into a stable system like this is something I would avoid today. Current Debian ships `libcatalyst-perl` and the related modules in its normal repositories, so a plain `apt install` works; alternatively `cpanm Catalyst::Runtime` into a local perlbrew or `local::lib` install keeps it away from the system packages.
