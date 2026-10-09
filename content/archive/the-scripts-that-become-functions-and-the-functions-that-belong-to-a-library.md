---
title: "The scripts that become functions, and the functions that belong to a library ."
date: 2014-08-19
post_lang: en
tags: [divertimento]
original_url: http://www.joanmarcriera.es/2014/08/19/the-scripts-that-become-functions-and-the-functions-that-belong-to-a-library/
summary: "A small sourced Bash library of helper functions (OS detection, package install, confirm, download-and-run) written to standardise scripts."
draft: false
---

Long ago, when I had the chance to build by myself a set of scripts that performed certain operations I ended up with a nice set of small things. I would like to share, but it needs some explanation. This library, group of tools, they do nothing by themselves, their only serve a single purpose which is **"To standardize"** . At that time I was a "one man army", I built stuff by myself, for myself and to myself, but then I realized that after me would come someone else, with different styles, different habits and so on,.. Since I needed to change as less code possible this library can be sourced and its functions called many times, they become read only , or they are atomic, so nothing has be worried about using its functions several times in a row.


```bash
#!/bin/bash
# Marcs library 
#TODO
# there are two lower case converters
# funcion to download all the scripts at once
# funcion to clean up all the scripts

# set variables 
declare -r TRUE=0
declare -r FALSE=1
declare -r PASSWD_FILE=/etc/passwd
declare -r RED='\033[0;41;30m'
declare -r STD='\033[0;0;39m'
declare -r CYAN='\e[1;37;44m'
declare -r TMPDIR='/tmp/'
##################################################################
# Purpose: Converts a string to lower case
# Arguments:
#   $1 -> String to convert to lower case
##################################################################
function to_lower() 
{
    local str="$@"
    local output     
    output=$(tr '[A-Z]' '[a-z]'<<<"${str}")
    echo $output
}
##################################################################
# Purpose: Display an error message and die
# Arguments:
#   $1 -> Message
#   $2 -> Exit status (optional)
##################################################################
function die() 
{
    local m="$1"	# message
    local e=${2-1}	# default exit status 1
    echo "$m" 
    exit $e
}
##################################################################
# Purpose: Return true if script is executed by the root user
# Arguments: none
# Return: True or False
##################################################################
function is_root() 
{
   [ $(id -u) -eq 0 ] && return $TRUE || return $FALSE
}
##################################################################
# Purpose: Return true $user exits in /etc/passwd
# Arguments: $1 (username) -> Username to check in /etc/passwd
# Return: True or False
##################################################################
function is_user_exits() 
{
    local u="$1"
    grep -q "^${u}" $PASSWD_FILE && return $TRUE || return $FALSE
}



##################################################################
# Purpose: Inform the user that this functions is not implemented
# Arguments: No arguments 
# Return: No returns
##################################################################
function notImplemented()
{
	 echo "This functions is not implemented yet."
	 echo "Press any Key to continue or press Ctrl-C."
	 read x
}
##################################################################
# Purpose: Converts a string to lower case
# Arguments:
#   $1 -> String to convert to lower case
##################################################################
lowercase(){
	echo "$1" | sed "y/ABCDEFGHIJKLMNOPQRSTUVWXYZ/abcdefghijklmnopqrstuvwxyz/"
}
##################################################################
# Purpose: Recover important information 
# Arguments: If $1 == "debug" then output for each var will be printed
# Return: TRUE is first time execution. FALSE if already executed
# Read Only variables set:
#	OS
#	DIST
#	DistroBasedOn
#	PSUEDONAME
#	REV
#	KERNEL
#	MACH
##################################################################
shootProfile(){
	 # This funcion creates readonly variables, if one of them has been set before it will crash
	 # check that all variables are unset.
	 [ -n "${OS+x}" ] && [ -n "${DIST+x}" ] && [ -n "${DistroBasedOn+x}" ] && [ -n "${PSUEDONAME+x}" ] && [ -n "${REV+x}" ] && [ -n "${KERNEL+x}" ] && [ -n "${MACH+x}" ] && echo " !!! shootProfile was called before. The variables are already available" &&  return $FALSE

	 OS=`lowercase \`uname\``
	 KERNEL=`uname -r`
	 MACH=`uname -m`

	 if [ "{$OS}" == "windowsnt" ]; then
		  OS=windows
	 elif [ "{$OS}" == "darwin" ]; then
		  OS=mac
	 else
		  OS=`uname`
		  if [ "${OS}" = "SunOS" ] ; then
				OS=Solaris
				ARCH=`uname -p`
				OSSTR="${OS} ${REV}(${ARCH} `uname -v`)"
			elif [ "${OS}" = "AIX" ] ; then
				OSSTR="${OS} `oslevel` (`oslevel -r`)"
			elif [ "${OS}" = "Linux" ] ; then
				if [ -f /etc/redhat-release ] ; then
					 DistroBasedOn='RedHat'
					 DIST=`cat /etc/redhat-release |sed s/\ release.*//`
					 PSUEDONAME=`cat /etc/redhat-release | sed s/.*\(// | sed s/\)//`
					 REV=`cat /etc/redhat-release | sed s/.*release\ // | sed s/\ .*//`
				elif [ -f /etc/SuSE-release ] ; then
					 DistroBasedOn='SuSe'
					 PSUEDONAME=`cat /etc/SuSE-release | tr "\n" ' '| sed s/VERSION.*//`
					 REV=`cat /etc/SuSE-release | tr "\n" ' ' | sed s/.*=\ //`
				elif [ -f /etc/mandrake-release ] ; then
					 DistroBasedOn='Mandrake'
					 PSUEDONAME=`cat /etc/mandrake-release | sed s/.*\(// | sed s/\)//`
					 REV=`cat /etc/mandrake-release | sed s/.*release\ // | sed s/\ .*//`
				 elif [ -f /etc/debian_version ] ; then
					 DistroBasedOn='Debian'
					 DIST=`cat /etc/lsb-release | grep '^DISTRIB_ID' | awk -F= '{ print $2 }'`
					 PSUEDONAME=`cat /etc/lsb-release | grep '^DISTRIB_CODENAME' | awk -F= '{ print $2 }'`
					 REV=`cat /etc/lsb-release | grep '^DISTRIB_RELEASE' | awk -F= '{ print $2 }'`
				 fi
				 if [ -f /etc/UnitedLinux-release ] ; then
					 DIST="${DIST}[`cat /etc/UnitedLinux-release | tr "\n" ' ' | sed s/VERSION.*//`]"
				  fi
				OS=`lowercase $OS`
				DistroBasedOn=`lowercase $DistroBasedOn`
				readonly OS
				readonly DIST
				readonly DistroBasedOn
				readonly PSUEDONAME
				readonly REV
				readonly KERNEL
				readonly MACH
		  fi

	 fi
	local debug=${1:-nodebug}
	 if [[ $debug = "debug" ]]; then
				echo $OS
				echo $DIST
				echo $DistroBasedOn
				echo $PSUEDONAME
				echo $REV
				echo $KERNEL
				echo $MACH
	 fi
	 return $TRUE
}
##################################################################
# Purpose: Make sure package on $1 is installed 
# Arguments:
#   $@ -> Packages wich should be installed
##################################################################
installPkg()
{
	 [ -n "${DistroBasedOn-x}" ] && shootProfile
	for i in $@
	do
		echo -n "Installing $i on $DistroBasedOn."
		case $DistroBasedOn in
			Debian | debian )
				 apt-get -y install $i
				 ;;
			SuSe | suse )
				 zypper install $i
				 ;;
			Mandrake | mandrake )
				 echo "do not know how to install $i package on mandrake "
				 ;;
			RedHat | redhat )
				 yum -y install $i
				 ;;
			*)
				 echo "\$DistroBasedOn variable has not a valid value. Value : ||$DistroBasedOn||"
				 ;;
		esac
	done
return 0
}
##################################################################
# Purpose: Compare hostname
# Arguments: 
#	$1 => string 
# Return : TRUE if $1 = `hostname` false otherwhise.
##################################################################
hostnameGet(){
	 [[ "`hostname`" = "$1" ]] && return $TRUE || return $FALSE
}
##################################################################
# Purpose: Return TRUE if $1 is confirmed, or keypresed
# Arguments: 
#	$1 => string 
# Return : TRUE if $1 user presses the key.
##################################################################
confirm(){
	 read -sn 1 -p "$1 [y/N]? "
	 [[ $REPLY = [Yy] ]] && return $TRUE|| return $FALSE
}

#===  FUNCTION  ================================================================
#          NAME:  downloadAndExec
#   DESCRIPTION:  downloads and launches a script
#    PARAMETERS:  $1 = script name
#       RETURNS:  TRUE if OK
#===============================================================================

downloadAndExec ()
{
	scriptname=$1
	workdir="/tmp"
	workscript=$workdir/$scriptname
	[ -f $workscript ] && rm $workscript
	wget $MASTERURL/bin/$scriptname -O $workscript
	chmod +x $workscript
	$workscript
	[[ $? -eq 0 ]] && rm $workscript && return $TRUE || return $FALSE

}	# ----------  end of function downloadAndExec  ----------

return 0
```


## 2026 note

The idea of one sourced library of small, idempotent functions still holds. Today the OS detection would read `/etc/os-release` (`. /etc/os-release; echo $ID`) instead of the per-distro release files, Bash 4+ has `${var,,}` for lower-casing, and `ifconfig` and `/etc/lsb-release` are gone from most minimal installs. Downloading a script and running it as in `downloadAndExec` should be paired with a checksum or signature check.
