---
title: "Desktop login and SMB/CIFS mountpoints made easy"
date: 2014-08-19
post_lang: en
tags: [divertimento]
original_url: http://www.joanmarcriera.es/2014/08/19/desktop-login-and-smbcifs-mountpoints-made-easy/
summary: "A logon script and an expect script that put a ready-to-use network share mount icon on each user's Linux desktop."
draft: false
---

Having lots of users with kind of "magic hands" got us to think what they did not need to think about, so they could do more of their research. Since we got everyone on AD using Quest ([see previous post](/archive/2014/link-unix-machines-to-ad-using-quest-autentication-services-install-it-using-expect/)) we where able to launch the following script each time they log on their Desktops, making a nice direct access to all the resource from their groups and from their research. Also, we used the [library](/archive/2014/the-scripts-that-become-functions-and-the-functions-that-belong-to-a-library/).

```bash
#!/bin/bash -x
#===============================================================================
#
#          FILE:  logon_script_workstation.sh
# 
#         USAGE:  ./logon_script_workstation.sh 
# 
#   DESCRIPTION:  
# 
#       OPTIONS:  ---
#  REQUIREMENTS:  ---
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR: Joan Marc Riera Duocastella (), 
#       CREATED: 12/22/2010 11:07:00 AM CET
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error

logger -i -s "$0 - launched"
#clean temp files
LOGFILE=/$0.log
cd /tmp
exec 1>>$LOGFILE
exec 2>>$LOGFILE
SERVERIP="server.example.com"
SERVERPATH="scripts"
MASTERURL=http://$SERVERIP/$SERVERPATH
## Don't edit above this line
SCRIPTNAME=$0
DATETIME=`date +%Y%m%d%H%M%S`
HNAME=`hostname`
# load marcs library
tempscript="library.sh"
if [ ! -f /tmp/$tempscript ]
then
         wget $MASTERURL/lib/$tempscript -O /tmp/$tempscript
         . /tmp/$tempscript && rm /tmp/$tempscript
fi
# define environment
shootProfile
# check if USER env variable is set, or otherwise set it
[ -n "${USER:-x}" ] && USER=`whoami` 
#check if .desktop exists else do it
if [[ -f /home/$USER/.config/user-dirs.dirs ]]
then
	desktop_dir=/home/$USER/`grep XDG_DESKTOP_DIR /home/$USER/.config/user-dirs.dirs  | cut -f2 -d\" | cut -f2 -d\/`
fi
if [[ -n "${desktop_dir:+x}" ]] && [[ ! -f "$desktop_dir/montar unitat de xarxa.desktop" ]]
then
	
	case $OS in
		 linux )	
			  tempscript="fs_share.tar"
			  ;;
		 mac )
			  tempscript="fs_share_macosx.tar"
			  ;;
		 * ) #at least try if there is luck
			  tempscript="fs_share.tar"
			  ;;
	esac
	
	#download fs_share.tar
	if [ ! -f /tmp/$tempscript ]
	then
		 wget $MASTERURL/src/$tempscript -O /tmp/$tempscript
	fi
	cd /tmp
	tar -xvf /tmp/$tempscript 
	rm  /tmp/$tempscript
	cd ${tempscript%%.???}
	datasrc_dir="`pwd`/data"
	#if [[ $CANGOSUDO -eq $TRUE ]]
	#then
	#we are not installing anything on a logonscript 
	#	sudo ./install.sh 
	#else
	cp $datasrc_dir/*.desktop $desktop_dir
	chmod +x $desktop_dir/montar*.desktop
	chmod +x $desktop_dir/desmontar*.desktop
	#fi
#	rm -r /tmp/${tempscript%%.???}
fi
#############################################mount end
##########################check sudoers
 # :TODO:12/22/2010 11:09:09 AM CET:: if uptime>15 dies mail with reboot and upgrade request
uptime
exit 0
```

Expect script to mount the remote CIFS

```bash
#!/usr/bin/expect -f

#mount the software repository

# Se definen la svariables USERNAME y PASS con el valor de los parametros que recibe el script.
set USERNAME [lindex $argv 0]
set PASS [lindex $argv 1]

# Montar //fileserver/software en /home/sysop/fs con los credenciales del usuario pasado como parametro
spawn mount.cifs //192.0.2.25/software /home/sysop/fs -o username=$USERNAME
#spawn mount -t cifs //192.0.2.25/software /home/sysop/fs -o username=$USERNAME
# Con la orden expect, indicamos la cadena de texto que esperamso que aparezca y con send, 
# se envia el parametro que queremso introducir de forma automatica
expect "Password:^"
sleep 5
send "$PASS\n"

expect eof
```

## 2026 note

Mounting a CIFS share still works with `mount.cifs` (package `cifs-utils`), but passing the password through `expect` and a command-line argument is not good practice today: use a credentials file with `credentials=` in the mount options, or `pam_mount` / a systemd automount unit so the share mounts at login without any password handling in a script. On current distributions `realmd` with `sssd` is the usual way of joining Linux machines to Active Directory.
