---
title: "python does not match the python default version"
date: 2009-10-01
post_lang: en
tags: [debian, linux, server, shell]
original_url: http://www.joanmarcriera.es/2009/10/01/python-does-not-match-the-python-default-version/
summary: "Working around a pycentral error when installing mod_python by temporarily repointing the /usr/bin/python symlink."
draft: false
---

Today I had to install mod_python and I've got the following error:

```
The following NEW packages will be installed:

libapache2-mod-python

0 upgraded, 1 newly installed, 0 to remove and 3 not upgraded.

Need to get 0B/134kB of archives.

After this operation, 590kB of additional disk space will be used.

Preconfiguring packages ...

(Reading database ... 38385 files and directories currently installed.)

Unpacking libapache2-mod-python (from .../libapache2-mod-python_3.3.1-2build1_amd64.deb) ...

Traceback (most recent call last):

File "/usr/bin/pycentral", line 1891, in ?

main()

File "/usr/bin/pycentral", line 1885, in main

rv = action.run(global_options)

File "/usr/bin/pycentral", line 1296, in run

runtimes = get_installed_runtimes()

File "/usr/bin/pycentral", line 210, in get_installed_runtimes

default_version = pyversions.default_version(version_only=True)

File "/usr/share/pycentral-data/pyversions.py", line 163, in default_version

raise ValueError, "/usr/bin/python does not match the python default version. It must be reset to point to %s" % debian_default

ValueError: /usr/bin/python does not match the python default version. It must be reset to point to python2.5

dpkg: error processing /var/cache/apt/archives/libapache2-mod-python_3.3.1-2build1_amd64.deb (--unpack):

subprocess pre-installation script returned error exit status 1

Errors were encountered while processing:

/var/cache/apt/archives/libapache2-mod-python_3.3.1-2build1_amd64.deb

E: Sub-process /usr/bin/dpkg returned an error code (1)
```

This is because I have the default python PATH instance linked to the 2.4 python version instead of the actual 2.5 that comes with my distro. So I don't would like to annoy my researchers during the install. The best option is to unlink, link, install, unlink and link again. But it must be as fast as possible....so he it comes:

**Solution:**

```bash
rm /usr/bin/python && ln -s /usr/bin/python2.5 /usr/bin/python && apt-get update && apt-get upgrade && rm /usr/bin/python && ln -s /usr/bin/python2.4 /usr/bin/python
```

Done.

## 2026 note

Python 2.4/2.5, pycentral and mod_python are all long gone from current distributions, so this exact situation no longer arises. In general, do not hand-edit the `/usr/bin/python` symlink on a Debian-based system; use `update-alternatives` or a virtual environment (`python3 -m venv`) for a different interpreter, and use `mod_wsgi` rather than mod_python with Apache.
