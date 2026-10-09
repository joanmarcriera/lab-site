---
title: "Dataguard alike using bash and cron"
date: 2014-08-19
post_lang: en
tags: [divertimento]
original_url: http://www.joanmarcriera.es/2014/08/19/dataguard-alike-using-bash-and-cron/
summary: "A bash and cron script that ships Oracle archive logs to a second server and applies them there, giving a manual standby database."
draft: false
---

Oracle EE is quite more expensive than SE, however sometimes you need a standby replica "just in case". This is how you get a standby replica on a different server, without breaking any Oracle licensing rules:

1. the following script has to be on both servers. It calls itself on remote.
2. set up a cronjob to launch the script on the primary server.
3. Check the log.

I must say that this script needs some big cleaning and ordering, but it works.

```bash
#!/bin/bash +x

#TODO:: fix the output processing when DEBUG=1
#TODO:: too many paths that must become variables


STB_SERVER=standby01                                     #the Standby database server # needs passwordless authentication to user oracle
LOG_FILE=/home/oracle/scripts/db_status.log             #

#load the environment variables
. ~/.bash_profile

# When debug=1 the scripts must be executed by hand , and most functions will not work as expected. Processing the functions output must be fixed
DEBUG=0

# is the local database OK ?
function check_status ()
{
[[ $DEBUG -eq 1 ]] && echo "DEBUG=check_Status"
#expected status "ok=1 ko=0"
INSTANCE_STATUS=$(echo "select STATUS from v\$instance; " | sqlplus -S / as sysdba|grep -E "MOUNTED|OPEN"|wc -l )
INSTANCE_ARCHIVER=$(echo "select ARCHIVER from v\$instance; " | sqlplus -S / as sysdba|grep "STARTED"| wc -l)
INSTANCE_DB_STATUS=$(echo "select DATABASE_STATUS from v\$instance; " | sqlplus -S / as sysdba|grep "ACTIVE" |wc -l)
INSTANCE_ACTIVE_STATE=$(echo "select ACTIVE_STATE from v\$instance; " | sqlplus -S / as sysdba|grep "NORMAL"|wc -l)

[[ $INSTANCE_STATUS -eq 1 ]] && [[ $INSTANCE_ARCHIVER -eq 1 ]] && [[ $INSTANCE_DB_STATUS -eq 1 ]] && [[ $INSTANCE_ACTIVE_STATE -eq 1 ]] && echo "STATUS = OK" || echo "STATUS = KO"

}

#check tns ping .
function tnsping_status ()
{
[[ $DEBUG -eq 1 ]] && echo "DEBUG=tnsping_status"
TNSPING=$(tnsping ORCL|tail -n1 |cut -d' ' -f1 |grep "OK"|wc -l)
[[ $TNSPING -eq 1 ]] && echo "STATUS = OK" || echo "STATUS = KO"
}

# get value for logcount on local database (open mode)
function archive_log_count ()
{
[[ $DEBUG -eq 1 ]] && echo "DEBUG=archive_log_count"
#don't return current, because is not finished. so return the last already switched.
#select max(SEQUENCE#) from V$ARCHIVED_LOG;
ARCHIVE_LOG=$(echo "select max(SEQUENCE#) from V\$ARCHIVED_LOG;" |sqlplus -S / as sysdba|tail -n2|head -n1|tr -d ' \t\r\f')
echo "LAST = $ARCHIVE_LOG"
}

#ask database to check for its local logcount  (standby mode)
function archive_log_count_stb ()
{
#select max(recid) from v$log_history;"
ARCHIVE_LOG_STB=$(echo "select max(recid) from v\$log_history;"|sqlplus -S / as sysdba |tail -n2 |head -n1|tr -d ' \t\r\f')
echo "LAST_STB = $ARCHIVE_LOG_STB"
}

#ask for remote logcount (standby mode)
function archive_log_count_stb_remote ()
{
ssh $STB_SERVER ~/scripts/db_status.sh archive_log_stb
}

#send new archive files to STB_SERVER
function send_files ()
{
#seq 452 $(expr 454 - 1)
FROM_FILE=$(ssh $STB_SERVER ~/scripts/db_status.sh archive_log_stb |cut -d'=' -f2)
TO_FILE=$(~/scripts/db_status.sh archive_log |cut -d'=' -f2)

[[ $FROM_FILE -eq $TO_FILE ]] && echo "SAME STATUS ON BOTH SIDES. " && exit 0

#files to send FROM TO -1
for FILE in $(seq $FROM_FILE $TO_FILE)
do
rsync -v /u01/orcl/ORADATA/DB_ARCHIVE/1_${FILE}_* $STB_SERVER:/u01/orcl/ORADATA/DB_ARCHIVE
done
}

#set remote database to recover automatically with archive logs already sent
function recover_standby_remote ()
{
#start recovery on standby
ssh $STB_SERVER ~/scripts/db_status.sh recover_local_standby
}

#recover with local archive logs
function recover_standby_local ()
{
sqlplus -S / as sysdba @/home/oracle/scripts/recover_standby_database.sql
}

#switch logfile  (debug purposes)
function switch_local ()
{
echo "alter system switch logfile;" |sqlplus -S / as sysdba
}

#delete old archive log files, this is used on STB_DATABASE because it does not have rman to clean it.
function clean_old_files_remote ()
{
ssh $STB_SERVER "find /u01/orcl/ORADATA/DB_ARCHIVE -mtime +7 -exec rm -rf {} \;"
}

#procedure when launched by cron.
function cron_mode ()
{
exec 1>> $LOG_FILE
exec 2>> $LOG_FILE
echo "CRON EXECUTION : $(date +%Y%m%d%H%M)"
#check status
check_status
tnsping_status
archive_log_count
archive_log_count_stb_remote
#send files
send_files
#recover
recover_standby_remote
clean_old_files_remote

echo "###### END CRON EXECUTION : $(date +%Y%m%d%H%M)"

}

case $1 in
        status)
                check_status
                ;;
        tnsping)
                tnsping_status
                ;;
        archive_log)
                archive_log_count
                ;;
        archive_log_stb)
                archive_log_count_stb
                ;;
        send_files)
                send_files
                ;;
        recover_remote_standby)
                recover_standby_remote
                ;;
        recover_local_standby)
                recover_standby_local
                ;;
        switch_logfile_local)
                switch_local
                ;;
        cron_mode)
                cron_mode
                ;;
        check_all)
                check_status
                tnsping_status
                archive_log_count
                archive_log_stb
                ;;
        *)
                echo "Usage: $0 {cron_mode|status|tnsping|archive_log|archive_log_stb|send_files|recover_remote_standby|recover_local_standby|switch_logfile_local|check_all}"
                exit 1
esac
```

## 2026 note

Shipping archived redo logs with rsync and applying them with a recovery script still works technically, because that is what a standby database is. Oracle's own Data Guard is an Enterprise Edition feature, so Standard Edition 2 users either keep a scripted approach like this one or use a third-party product built for the purpose; check Oracle's current licence terms before relying on it. The script would need more quoting and error handling today, and `find ... -exec rm -rf` is better written as `find ... -delete`.
