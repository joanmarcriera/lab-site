---
title: "SH  ( not bash) menu driven  for AIX (for example)"
date: 2014-08-19
post_lang: en
tags: [divertimento]
original_url: http://www.joanmarcriera.es/2014/08/19/sh-not-bash-menu-driven-for-aix-for-example/
summary: "A portable /bin/sh menu script (no bash needed, e.g. on AIX) that runs a list of Oracle SQL report scripts from a lettered menu."
draft: false
---

Useful menu structure. Nicely used when bash is not around, and you need some interactive menu.


```sh
#!/bin/sh
# sample.mnu
# A simple script menu under Unix
# Main logic starts at MAIN LOGIC
# The logo will be displayed at the top of the screen
LOGO="Oracle info report  Menu - Marc Riera (2012)"
#------------------------------------------------------
# MENU PROMPTS
#------------------------------------------------------
# A list of menu prompts to be displayed for the user.
# The list can be modified.
# In this first list, enter the menu prompt as it should appear
# on the screen for each of the letters A - L. In this example
# menu pick variables emenu through lmenu are blank as there
# are no menu selections for keys E through L.

amenu="a.  whoami.sql			:	rem Purpose:    Reports information about your current database context";
bmenu="b.  ver.sql			:	rem Purpose:    Show database version with options intalled"; 
cmenu="c.  usedsp.sql			:	rem Purpose:    Used space in Meg by segment type"; 
dmenu="d.  datos_generals.sql		:	rem Purpose:    General info about the connected database"; 
emenu="e.  version_bbdd.sql		:	rem Purpose:    Display v\$version database ";
fmenu="f.  tablespaces_size_free_percent2.sql	: rem Purpose:	Tablespaces size free percent 2  ";
gmenu="g.  redologs_status.sql 		:	rem Purpose:	Redologs status";
hmenu="h.  datafile_size_free_percent.sql	: rem Purpose:	Datafile size free percent ";
imenu="i.  control_file.sql 		:	rem Purpose:	Control files";
jmenu="j.  nls_parameters.sql		: 	rem Purpose:	Nls parameters ";
kmenu="k.  db_options.sql		:	rem Purpose:	Database options ";
lmenu=" "                                 ;
mmenu="m   Payroll Menu "                 ;

#------------------------------------------------------
# MENU FUNCTION DEFINITIONS
#------------------------------------------------------
 
# Define a function for invalid menu picks
# The function loads an error message into a variable
badchoice () { MSG="Invalid Selection ... Please Try Again" ; } 
 
# For each prompt displayed above, there is a list of 
# commands to execute in response to the user picking the
# associated letter.
# They are defined as functions
# apick () through lpick () where
# apick () corresponds to the menu
# prompt amenu which is selected
# selected by pressing a or A.
# bpick () corresponds to the menu
# prompt bmenu which is selected by
# pressing b or B and so on.
# Any menu item that is not
# assigned a set of commands, is
# assigned
# the function badchoice () as a default for that pick.
# If the user
# selects a menu key that is assigned
# to badchoice (). This function
# causes an error message to be
# displayed on the screen.
# To add items to this second
# list, replace badchoice ()
# with the commands to run when
# that letter is pressed.
# The following steps simply define
# the functions, but do not cause
# any shell program steps to be executed.

# Command example : sqlplus -S sys/CHANGE_ME@INSTANCE as sysdba @ask_version.sql
apick () { sqlplus -S sys/CHANGE_ME@INSTANCE as sysdba @whoami.sql ; echo Press Enter ; read DUMMY ; }
bpick () { sqlplus -S sys/CHANGE_ME@INSTANCE as sysdba @ver.sql; echo Press Enter ; read DUMMY ; }
cpick () { sqlplus -S sys/CHANGE_ME@INSTANCE as sysdba @usedsp.sql; echo Press Enter ; read DUMMY ; }
dpick () { sqlplus -S sys/CHANGE_ME@INSTANCE as sysdba @datos_generals.sql; echo Press Enter ; read DUMMY ; }
epick () { sqlplus -S sys/CHANGE_ME@INSTANCE as sysdba @version_bbdd.sql; echo Press Enter ; read DUMMY ; }
fpick () { sqlplus -S sys/CHANGE_ME@INSTANCE as sysdba @tablespaces_size_free_percent2.sql; echo Press Enter ; read DUMMY ; }
gpick () { sqlplus -S sys/CHANGE_ME@INSTANCE as sysdba @redologs_status.sql; echo Press Enter ; read DUMMY ; }
hpick () { sqlplus -S sys/CHANGE_ME@INSTANCE as sysdba @datafile_size_free_percent.sql; echo Press Enter ; read DUMMY ; }
ipick () { sqlplus -S sys/CHANGE_ME@INSTANCE as sysdba @control_file.sql; echo Press Enter ; read DUMMY ; }
jpick () { sqlplus -S sys/CHANGE_ME@INSTANCE as sysdba @nls_parameters.sql ; echo Press Enter ; read DUMMY ; }
kpick () { sqlplus -S sys/CHANGE_ME@INSTANCE as sysdba @db_options.sql ; echo Press Enter ; read DUMMY ; }
lpick () { badchoice ; }
mpick () { payroll.mnu ; }

#------------------------------------------------------
# DISPLAY FUNCTION DEFINITION
#------------------------------------------------------
# This function displays the menu.
# The routine clears the screen, echoes
# the logo and menu prompts
# and some additional messages.
# Note that this definition does
# not cause the function to
# be executed yet, it just defines
# it ready to be executed.

themenu () {
	# clear the screen
	clear
	echo `date`
	echo
	echo "\t\t\t" $LOGO
	echo
	echo "\t\tPlease Select:"
	echo
	echo "\t\t\t" $amenu
	echo "\t\t\t" $bmenu
	echo "\t\t\t" $cmenu
	echo "\t\t\t" $dmenu
	echo "\t\t\t" $emenu
	echo "\t\t\t" $fmenu
	echo "\t\t\t" $gmenu
	echo "\t\t\t" $hmenu
	echo "\t\t\t" $imenu
	echo "\t\t\t" $jmenu
	echo "\t\t\t" $kmenu
	echo "\t\t\t" $lmenu
	echo "\t\t\tx. Exit"
	echo
	echo $MSG
	echo
	echo Select by pressing the letter and then ENTER ;
}
 
#------------------------------------------------------
# MAIN LOGIC
#------------------------------------------------------
# Every thing up to this point has been to define
# variables or functions.
# The program actually starts running here.

# Clear out the error message variable
MSG=

# Repeat the menu over and over
# Steps are:
# 1. Display the menu
# 2. 'read' a line of input from the key board
# 3. Clear the error message
# 4. Check the answer for a or A or b or B etc. and dispatch
#    to the appropriate program or function or exit
# 5. If the entry was invalid call the badchoice () function
#    to initialize MSG to an error message
# 6. This error message is used when setting up the menu
#    for a menu pick that is valid but has no command
#    associated with it.

while  true
do
	# 1. display the menu
	themenu

	# 2. read a line of input from the keyboard
	read answer

	# 3. Clear any error message
	MSG=

	# 4. Execute one of the defined functions based on the
	#    letter entered by the user.

	# 5. If the choice was E through L, the pre-defined
	#    function for that pick will execute badchoice ()
	#    which loads an error message into MSG  
		case $answer in
		        a|A) apick;;
		        b|B) bpick;;
		        c|C) cpick;;
		        d|D) dpick;;
		        e|E) epick;;
		        f|F) fpick;;
		        g|G) gpick;;
		        h|H) hpick;;
		        i|I) ipick;;
		        j|J) jpick;;
		        k|K) kpick;;
		        l|L) lpick;;

	#      If the user selects x to exit then break out
	#      of this loop
			x|X) break;;

	# 6. If the entry was invalid call the badchoice function
	#    to initialize MSG to an error message
			*) badchoice;;
																 
		esac

	#     Do it again until the user enters x.
	done

exit 0
```

## 2026 note

A plain POSIX `sh` menu like this still runs anywhere, including AIX. `echo "\t"` is shell-dependent, so `printf` is more portable today, and putting the database password on the `sqlplus` command line exposes it in the process list; use OS authentication (`sqlplus / as sysdba`) or an Oracle wallet instead.
