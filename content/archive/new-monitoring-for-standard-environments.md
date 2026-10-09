---
title: "New monitoring for standard environments"
date: 2014-08-19
post_lang: en
tags: [divertimento]
original_url: http://www.joanmarcriera.es/2014/08/19/new-monitoring-for-standard-environments/
summary: "Installing the Open Monitoring Distribution (OMD, built around Check_MK) on a RHEL 6 style server."
draft: false
---

From some time now we have started using a "monitoring distribution". It uses passive monitoring where it can be used, and has lots of plugins for standard services. It gives you a nice output, check it out:

*(screenshot withheld)*

Credit has to be given to <http://mathias-kettner.de/>

All you need to know is here => <http://omdistro.org/>

To install the FULL pack you just need to do the following:

```bash
# where to start => http://omdistro.org/

wget http://ftp.cica.es/epel/6/x86_64/epel-release-6-8.noarch.rpm
rpm -ivh epel-release-6-8.noarch.rpm
rpm -Uvh "https://labs.consol.de/repo/stable/rhel6/x86_64/labs-consol-stable.rhel6.noarch.rpm"
yum update
yum install omd-1.10
omd create monit
yum install check-mk-agent
omd create lab
```

After this, you can go to your server http://server/monit/ with user omdadmin and the default password, and you will find yourself adding machines to the monitoring. The agents can be found on the server itself, at the /opt/omd/sites/monit/share/agents/ directory (I may misspell but is arround that )

## 2026 note

The repositories and packages in this recipe (RHEL/CentOS 6, EPEL 6, omd-1.10) are long end-of-life and should not be used. OMD lives on as the base of Checkmk, whose free edition is open source and installs from the vendor's packages for supported distributions. Change the default `omdadmin` password straight after the first login.
