---
title: "Sun Grid Engine"
date: 2010-03-11
post_lang: ca
tags: [divertimento, linux, server]
original_url: http://www.joanmarcriera.es/2010/03/11/sun-grid-engine/
summary: "Installation notes for Sun Grid Engine 6.2u5 on Debian/Ubuntu: NFS share, sgeadmin user, master install and autostart."
draft: false
---

My SGE installation process.      

#### Links basics

- <http://wikis.sun.com/display/gridengine62u5/Home> -- SGE Home
- [JMX](http://publib.boulder.ibm.com/infocenter/wasinfo/v6r0/index.jsp?topic=/com.ibm.websphere.express.doc/info/exp/ae/cxml_javamanagementx.html)
- [NFS](http://howtoforge.com/setting-up-an-nfs-server-and-client-on-debian-lenny)

#### Com funciona

##### User level

- <http://wikis.sun.com/display/gridengine62u5/How+the+System+Operates> -- Funcionament del sistema
- <http://wikis.sun.com/display/gridengine62u5/How+Resources+Are+Matched+to+Requests> -- Distribució de recursos
- <http://wikis.sun.com/display/gridengine62u5/Choosing+a+User+Interface> -- GUI
- <http://wikis.sun.com/display/gridengine62u5/Users+and+User+Categories> -- Categories d'usuari

##### Admnistració

- [Hosts](http://wikis.sun.com/display/gridengine62u5/Configuring+Hosts)
- [cues](http://wikis.sun.com/display/gridengine62u5/Configuring+Queues)
- [usuaris](http://wikis.sun.com/display/gridengine62u5/Managing+User+Access)
- [qconf](http://wikis.sun.com/display/gridengine62u5/Using+qconf)
  - [cheat sheet](http://wikis.sun.com/display/gridengine62u5/qconf+Cheat+Sheet)
- [sistemes paralels](http://wikis.sun.com/display/gridengine62u5/Managing+Parallel+Environments)
- [monitorització](http://wikis.sun.com/display/gridengine62u5/Monitoring+and+Controlling+SMF+Services)
- [estadistiques](http://wikis.sun.com/display/gridengine62u5/Generating+Accounting+Statistics)
- [backup i restore](http://wikis.sun.com/display/gridengine62u5/Backing+Up+and+Restoring+System+Configuration)
- [tuning](http://wikis.sun.com/display/gridengine62u5/Fine-Tuning+Your+Environment)
- [tuning amb dtrace](http://wikis.sun.com/display/gridengine62u5/Using+DTrace+for+Performance+Tuning)

##### Instalació

- [Planificació](http://wikis.sun.com/display/gridengine62u5/Planning+the+Installation)
  - [System requirements](http://wikis.sun.com/display/gridengine62u5/System+Requirements)
  - [checklist](http://wikis.sun.com/display/gridengine62u5/Planning+Checklist)
  - [Descarregar SGE](http://www.sun.com/download/index.jsp?cat=Grid%20%26%20Provisioning&tab=3)
- [Metodes d'instalació](http://wikis.sun.com/display/gridengine62u5/Installation+Methods)

#### Hands on

##### Install

###### checklist

*(screenshot lost)*

###### User accounts

*(This section and "Network services" below are quoted from Sun's Grid Engine 6.2u5 documentation.)*

**Note** To use SMF on Solaris 10 or later hosts and run the Grid Engine software as an unprivileged user, perform the following additional steps as root user (or user with appropriate permissions): **For a local user**:

1.  Create the new role `sgeadmin`:

    ```
    roleadd -c "Grid Engine SMF Administrator" -g <group> -d <home_dir> -u <UID> -s <profile_shell> -P "solaris.smf.manage.sge" "sgeadmin"
    ```

1.  Assign the just-created role sgeadmin to the user:

    ```
    usermod -R "sgeadmin" <login>
    ```

**For a distributed name service, such as NIS, NIS+, or LDAP**:

- Create the new role `sgeadmin` and assign it to the user:

  ```
  /usr/sadm/bin/smrole add -D <domain_name> - -n "sgeadmin" -a "normal_user" -d <home_dir> -c "Grid Engine SMF Administrator" -p "solaris.smf.manage.sge"
  ```

###### Network services

Determine whether your site's network services are defined in an NIS database or in an `/etc/services` file that is local to each workstation. If your site uses NIS, determine the host name of your NIS server so that you can add entries to the NIS services map. The Grid Engine system services are `sge_execd` and `sge_qmaster`. To add the services to your NIS map, choose reserved, unused port numbers. The following examples show `sge_qmaster` and `sge_execd` entries.

```
sge_qmaster 6444/tcp
sge_execd 6445/tcp
```

###### Installation

###### Master host

- <http://wikis.sun.com/display/gridengine62u5/Installing+the+Software+With+the+GUI+Installer>

- <http://wikis.sun.com/display/gridengine62u5/Installing+the+Software+From+the+Command+Line>

###### Execution hosts

- <http://wikis.sun.com/display/gridengine62u5/Installing+the+Software+With+the+GUI+Installer>

- <http://wikis.sun.com/display/gridengine62u5/Installing+the+Software+From+the+Command+Line>

- automated installation, using the `inst_sge` script and a configuration file. See [Using the inst_sge Utility and a Configuration Template](http://wikis.sun.com/display/gridengine62u5/Automating+the+Installation+Process#AutomatingtheInstallationProcess-autocfg).

###### NFS

- server

  ```
  apt-get -y install nfs-kernel-server nfs-common portmap
  echo "/var/nfs        10.0.0.0/24(rw,sync,no_subtree_check)" >> /etc/exports
  exportsfs -a
  ```

- client

  ```
  apt-get -y install nfs-common portmap
  echo "10.0.0.21:/var/nfs /mnt/nfs/var/nfs  nfs     rw,sync,hard,intr       0      0" >> /etc/fstab
  mkdir -p /mnt/nfs/var/nfs ; mount -a
  ```

- permisions

  ```
  addgroup sgeadmin
  adduser -c "Grid Engine SMF Administrator" --home /home/sgeadmin -g sgeadmin  sgeadmin
  chown -R sgeadmin.sgeadmin /var/nfs/sgeroot
  ```

\*\* Tots els nodes i/o masters han de tenir l'usuari sgeadmin

###### Edició de hostnames

```
HOSTNAME=%NOMMAQUINA% ; export HOSTNAME
```

```
 sudo sed -i "s/kickseed/$HOSTNAME/g" /etc/hosts
 sudo sed -i "s/kickseed/$HOSTNAME/g" /etc/hostname
 sudo hostname -v $HOSTNAME
```

###### Instalació del Master

- Entorn: \*\* Variables entorn

  ```
  echo "
  SGE_ROOT=/mnt/nfs/var/nfs/sgeroot
  export SGE_ROOT" >> /home/sgeadmin/.bashrc
  ```

  \*\* hostname

  ```
  sed -i "/`hostname`/s/127.0.1.1/`ifconfig | awk '/Bcast/ {print $2}'|cut -d: -f2`/g" /etc/hosts
  ```

- Descomprimir:

  ```
  gzip -dc ../sge/ge-6.2u5-common.tar.gz | tar xvpf -
  gzip -dc ../sge/ge-6.2u5-bin-lx24-amd64.tar.gz |tar xvpf -
  gzip -dc ../sge/ge-6.2u5-bin-lx24-x86.tar.gz |tar xvpf -
  gzip -dc ../sge/ge-6.2u5-bin-lx24-ia64.tar.gz |tar xvpf -
  ```

- Software necessari per a la intalació

  ```
  apt-get install binutils sun-java6-jre
  ```

- Iniciar la instalació (as root)

  ```
  cd $SGE_ROOT
  ./inst_sge -m
  ```

- JMX MBean server config

  ```
  Using the following JMX MBean server settings.
     libjvm_path              >/usr/lib/jvm/java-6-openjdk/jre/lib/amd64/server/libjvm.so<
     Additional JVM arguments >-Xmx256m<
     JMX port                 >6446<
     JMX ssl                  >true<
     JMX client ssl           >true<
     JMX server keystore      >/var/sgeCA/sge_qmaster/default/private/keystore<
     JMX server keystore pw   >*********< ;)   .
  ```

- Berkeley Database spooling parameters

  ```
  Berkeley Database spooling parameters
  -------------------------------------

  You are going to install a RPC Client/Server mechanism!
  In this case, qmaster will
  contact a RPC server running on a separate server machine.
  If you want to use the SGE shadowd, you have to use the
  RPC Client/Server mechanism.

  Enter database server name or
  hit RETURN to use default [host01] >>

  Enter the database directory
  or hit RETURN to use default [/mnt/nfs/var/nfs/sgeroot/default/spooldb] >>
  creating directory: /mnt/nfs/var/nfs/sgeroot/default/spooldb
  Please remember these values, during Qmaster installation
  you will be asked for! Hit RETURN to continue!

  The Berkeley DB installation is completed now!
  If you are using a Berkely DB Server, please add the bdb_checkpoint.sh
  script to your crontab. This script is used for transaction
  checkpointing and cleanup in SGE installations with a
  Berkeley DB RPC Server. You will find this script in:
  /mnt/nfs/var/nfs/sgeroot/util/

  It must be added to the crontab of the user (sgeadmin), who runs the
  berkeley_db_svc on the server host.

  e.g. * * * * * <full path to scripts> <sge-root dir> <sge-cell> <bdb-dir>
  ```

- Sgeadmin Keystore =\> minim 6 lletres =\> CHANGE_ME ;)

- Using Grid Engine

  ```
  Using Grid Engine
  -----------------

  You should now enter the command:

     source /mnt/nfs/var/nfs/sgeroot/default/common/settings.csh

  if you are a csh/tcsh user or

     # . /mnt/nfs/var/nfs/sgeroot/default/common/settings.sh

  if you are a sh/ksh user.

  This will set or expand the following environment variables:

     - $SGE_ROOT         (always necessary)
     - $SGE_CELL         (if you are using a cell other than >default<)
     - $SGE_CLUSTER_NAME (always necessary)
     - $SGE_QMASTER_PORT (if you haven't added the service >sge_qmaster<)
     - $SGE_EXECD_PORT   (if you haven't added the service >sge_execd<)
     - $PATH/$path       (to find the Grid Engine binaries)
     - $MANPATH          (to access the manual pages)
  ```

- autostart qmaster y bdb on boot as sgeadmin (dona un warning pero no passa res perque només ens interessa el runlevel 2 i en un futur potser el 5)

  ```
  echo "sudo -u sgemaster /etc/init.d/sgemaster.MYCLUSTER " >> /etc/rc.local
  echo "sudo -u sgemaster /etc/init.d/sgebdb start " >> /etc/rc.local
  sed -i "s/exit 0//g" /etc/rc.local
  echo "exit 0" >> /etc/rc.local
  cat /etc/rc.local
  ```

**qmon** no funcionava i he hagut d’executar el  següent: source /mnt/nfs/var/nfs/sgeroot/default/common/settings.sh I ara comença lo divertit, afegir nodes respectant permisos i que funcionin. Despres les cues. Enjoy.  

## 2026 note

Sun Grid Engine 6.2u5 and the Sun/Oracle wiki pages linked here are long gone. The project lives on as community forks (Open Grid Scheduler, Son of Grid Engine) but for new clusters Slurm is the common batch scheduler. The NFS and `portmap` steps are also dated: current systems use `rpcbind`, and the exports command is `exportfs -a` (the post has a typo).
