---
title: "Fuse and sshfs"
date: 2009-10-06
post_lang: en
tags: [debian, linux, server, shell]
original_url: http://www.joanmarcriera.es/2009/10/06/fuse-and-sshfs/
summary: "How to build FUSE and sshfs from source to mount remote directories over SSH, with fixes for two common errors."
draft: false
---

Ok, you want to mount some remote stuff with sshfs. Download fuse and sshfs from [here](http://fuse.sourceforge.net/). (Stable release.)

Now we have two files :

- fuse-2.8.1.tar.gz
- sshfs-fuse-2.2.tar.gz

With our regular user we do the following .

```bash
$ tar -zxvf *.tar.gz
$ cd fuse-2.8.1
$ ./configure ; make
```

We go to root and install it.

```bash
# make install
```

Then the sshfs

```bash
$ cd sshfs-fuse-2.2
$ ./configure; make
# make install
```

Then, here comes the interesting part of the post, my usual errors and my tips.

Error on fuse: "fuse: failed to open /dev/fuse: Permission denied"

Solution:

```bash
# chmod o+rw /dev/fuse
```

You can also add you user to the new fuse group, but I always pretend to install it for the other users, and I don't will remember (do not want to..) to add new users to this group. So others is helpful.

Error on sshfs: "error while loading shared libraries: libfuse.so.2"

Solution:

32bits)

```bash
# ln -s /usr/local/lib/libfuse.so.2 /lib64/
```

64bits)

```bash
# ln -s /usr/local/lib/libfuse.so.2 /lib/
```

I guess this last one is a bug, but may be a feature, you know.

## 2026 note

There is no need to compile FUSE and sshfs by hand any more: `sshfs` is packaged on Debian, Ubuntu and Fedora (`apt install sshfs`), and the `fuse`/`fuse3` package sets up `/dev/fuse` permissions and the `fuse` group correctly. Usage is `sshfs user@host:/path /mnt/point`, unmounted with `fusermount -u /mnt/point` (or `fusermount3 -u`). The original `sshfs` project is now in maintenance-only mode, but it still works for everyday use. The two symlink lines in the post look swapped: the one labelled 32 bits points at `/lib64/` and the 64-bit one at `/lib/`.
