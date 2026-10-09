---
title: "Link Unix machines to AD using Quest Autentication Services.  Install it using expect."
date: 2014-08-19
post_lang: en
tags: [divertimento]
original_url: http://www.joanmarcriera.es/2014/08/19/link-unix-machines-to-ad-using-quest-autentication-services-install-it-using-expect/
summary: "Joining Linux or Mac machines to Active Directory with Quest Authentication Services, using a bash script plus an expect script to automate the interactive installer."
draft: false
---

This next script uses the library introduced on a previous post => [The scripts that become functions, and the functions that belong to a library](/archive/2014/the-scripts-that-become-functions-and-the-functions-that-belong-to-a-library/). This script was launched at the end of the installation of all the workstations. It configures the linux, or MAC , to be part of an Active Directory, which allows the administrator to manage the root passwords, what runs at boot, and even the desktop background. <http://www.quest.com/authentication-services/> However, the installation and configuration was slow and wanted to be interactive, so in this case we used [expect](http://www.admin-magazine.com/Articles/Automating-with-Expect-Scripts) to automate the human interaction. The first script is the bash that was launched after the pre-seed job, then comes the expect (which is launched from inside the bash).

```bash
#!/bin/bash -x

# Script de instalacion de QAS en un desktop
# El script llama a qas_install.expect, donde se ejecutan instrucciones expect. 

# Las salidas por pantalla, se redirigen al fichero output.expect.o
# Los errores se redirigen al fichero output.expect.e # :TODO:01/14/2011 10:32:18 AM CET:: unificar output
exec 1>./output.expect.o
exec 2>./output.expect.e

# Definicion de variables.
USERNAME="username_only_allowed_to_add_machines_to_AD"
PASS="CHANGE_ME"
SERVERIP="192.0.2.10"   # ip of our repository with all the scripts , also the library.
SERVERPATH="scripts"
MASTERURL="http://$SERVERIP/$SERVERPATH"

# Funcion para instalar paquete 'smbfs'.
installsmbfs(){
	 echo "Installing smbfs"
	 apt-get update
	 apt-get -y upgrade
	 apt-get -y autoremove
	 apt-get -y install smbfs 
}

 # :TODO:01/14/2011 10:32:34 AM CET:: smbfs is not necessary 
# Comprueba si el paquete 'smbfs' esta instalado en el sistema. Si no lo esta, ejecuta la funcion 
# llamada 'installsmbfs'.
dpkg-query -l 'smbfs'
[ "$?" -eq  "0" ] && echo "smfs is already installded. Keep going" || installsmbfs

 # :TODO:01/14/2011 10:32:34 AM CET:: smbfs is not necessary 
# Comprueba si el paquete 'smbfs' esta instalado en el sistema. Si lo esta, no hace nada.
dpkg-query -l 'smbfs'
[ "$?" -eq  "0" ] && echo "smfs has been installed. Keep going" || die " smfs can not be installed " 

# Modifica un parametro del fichero /etc/ssh/sshd_config y reinicia el servicio sshd
sed -i 's/ChallengeResponseAuthentication no/ChallengeResponseAuthentication yes/g' /etc/ssh/sshd_config
/etc/init.d/ssh reload
 # :TODO:01/14/2011 10:32:58 AM CET:: check if directory already existes , also check if files already exist
# Descarga ficheros vas.conf y vgp.conf en sus rutas correspondientes
mkdir -p /etc/opt/quest/vas
mkdir -p /etc/opt/quest/vgp
wget $MASTERURL/etc/opt/quest/vas/vas.conf  -O /etc/opt/quest/vas/vas.conf
wget $MASTERURL/etc/opt/quest/vgp/vgp.conf  -O /etc/opt/quest/vgp/vgp.conf

# Modifica el template vas.conf. Escribe el nombre del PC
sed  -i "s/%%HOSTNAME%%/`hostname`/g" /etc/opt/quest/vas/vas.conf

[ -d /home/sysop/fs ] && echo "fs exists" || echo "fs does not exist"
[ -d /home/sysop/fs/QAS_4_0_1_22 ] && echo "QAS dir  exists" || echo "QAS dir  does not exist"

cd /home/sysop
 # :TODO:01/14/2011 10:33:33 AM CET:: this should be done on /tmp
wget $MASTERURL/src/QAS_4.tgz
tar xvzf QAS_4.tgz

cd /home/sysop/QAS_4_0_1_22
./install.sh -q vasclnt
./install.sh -q vasgp
/opt/quest/bin/vastool configure pam common-password

apt-get -y install expect
############################# install qas
tempscript="qas_install.expect"
if [ ! -f ./$tempscript ]
then
        wget $MASTERURL/bin/$tempscript
fi
chmod +x $tempscript
./$tempscript $USERNAME $PASS

exit 0
```



```tcl
#!/usr/bin/expect -f

# Script de expect. Script pide pasar parametros en la instalacion de l aaplicacion QAS
# Con expect, esos parametros se pasan de forma automatica.
#echo "dentro expect"


# Se definen la svariables USERNAME y PASS con el valor de los parametros que recibe el script.
set USERNAME [lindex $argv 0]
set PASS [lindex $argv 1]

# ejecutar el fichero ./install.sh del instalador de QAS
spawn /opt/quest/bin/vastool -u $USERNAME join corp.example.com
# contestar las preguntas de la instalacion de QAS de forma desatendida
sleep 1
expect "CORP.ACTIVEDIRECTORYDOMAIN.ORG:*" 
sleep 1
send "$PASS\r"
sleep 60
```

## 2026 note

Quest Authentication Services is now sold as One Identity Authentication Services, and for most Linux machines the free `realmd`/`sssd` pair (`realm join example.com`) or Samba winbind does the same job. `expect` still works for automating interactive installers, but note that passing a password as a command-line argument, as this script does, exposes it in the process list; prefer reading it from a protected file or environment variable. The `smbfs` package it installs has been replaced by `cifs-utils`.
