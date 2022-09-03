#!/bin/bash

LINES=5
logfile=testlogfile.log
( date; uname -a ) >> $logfile

echo "---------------------------" >> $logfile
tail -$LINES /var/log/messages | xargs | fmt -s >> $logfile
echo >> $logfile
echo >> $logfile

exit 0
