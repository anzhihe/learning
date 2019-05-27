#/bin/sh

#update rrd
/usr/bin/python /data/www/Servermonitor/webmonitor/updaterrd.py

#graph rrd
/usr/bin/python /data/www/Servermonitor/webmonitor/graphrrd.py
