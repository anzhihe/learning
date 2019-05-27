#!/bin/sh
rrdfile=$1
pngfile=$2
rrdtype=$3
appname=$4
GraphStart=$5
GraphEnd=$6
ymax=$7
Alarm=$8

rrdtool_font="/data/www/Servermonitor/site_media/font/simhei.ttf"
export LANG==zh_CN.utf8
export LC_ALL==zh_CN.utf8
export LANG==zh_CN.utf8
export LANGUAGE==zh_CN.utf8
export LC_CTYPE==zh_CN.utf8
export LC_TIME==zh_CN.utf8


if [ "$rrdtype" == "time" ]; then
 /usr/bin/rrdtool graph ${pngfile} -w 500 -h 207 \
-n TITLE:10:${rrdtool_font} \
-n UNIT:8:${rrdtool_font} \
-n LEGEND:8:${rrdtool_font} \
-n AXIS:8:${rrdtool_font} \
-c SHADEA#808080 \
-c SHADEB#808080 \
-c FRAME#006600 \
-c ARROW#FF0000 \
-c AXIS#000000 \
-c FONT#000000 \
-c CANVAS#eeffff \
-c BACK#ffffff \
--title "Website 中国 response time statistics-${appname}" -v "(Seconds)" \
--start ${GraphStart} \
 --end ${GraphEnd} \
--lower-limit=0 \
--base=1024 \
-u ${ymax} -r  \
DEF:NAMELOOKUP_TIME=${rrdfile}:NAMELOOKUP_TIME:AVERAGE \
DEF:CONNECT_TIME=${rrdfile}:CONNECT_TIME:AVERAGE \
DEF:PRETRANSFER_TIME=${rrdfile}:PRETRANSFER_TIME:AVERAGE \
DEF:STARTTRANSFER_TIME=${rrdfile}:STARTTRANSFER_TIME:AVERAGE \
DEF:TOTAL_TIME=${rrdfile}:TOTAL_TIME:AVERAGE \
COMMENT:" \n" \
AREA:TOTAL_TIME#0011ff:TotalTime \
GPRINT:TOTAL_TIME:LAST:"Current\:%0.2lf %Ss"  \
GPRINT:TOTAL_TIME:AVERAGE:"Avg\:%0.2lf %Ss"  \
GPRINT:TOTAL_TIME:MAX:"Max\:%0.2lf %Ss"  \
GPRINT:TOTAL_TIME:MIN:"Min\:%0.2lf %Ss"  \
COMMENT:" \n" \
LINE1:NAMELOOKUP_TIME#eeee00:NAMELOOKUP \
GPRINT:NAMELOOKUP_TIME:LAST:"Current\:%0.2lf %Ss"  \
GPRINT:NAMELOOKUP_TIME:AVERAGE:"Avg\:%0.2lf %Ss"  \
GPRINT:NAMELOOKUP_TIME:MAX:"Max\:%0.2lf %Ss"  \
GPRINT:NAMELOOKUP_TIME:MIN:"Min\:%0.2lf %Ss"  \
COMMENT:" \n" \
LINE1:CONNECT_TIME#00aa00:CONNECT_TIME \
GPRINT:CONNECT_TIME:LAST:"Current\:%0.2lf %Ss"  \
GPRINT:CONNECT_TIME:AVERAGE:"Avg\:%0.2lf %Ss"  \
GPRINT:CONNECT_TIME:MAX:"Max\:%0.2lf %Ss"  \
GPRINT:CONNECT_TIME:MIN:"Min\:%0.2lf %Ss"  \
COMMENT:" \n" \
LINE1:PRETRANSFER_TIME#ff5511:PRETRANSFER_TIME \
GPRINT:PRETRANSFER_TIME:LAST:"Current\:%0.2lf %Ss"  \
GPRINT:PRETRANSFER_TIME:AVERAGE:"Avg\:%0.2lf %Ss"  \
GPRINT:PRETRANSFER_TIME:MAX:"Max\:%0.2lf %Ss"  \
GPRINT:PRETRANSFER_TIME:MIN:"Min\:%0.2lf %Ss"  \
COMMENT:" \n" \
LINE1:STARTTRANSFER_TIME#004455:STARTTRANSFER_TIME \
GPRINT:STARTTRANSFER_TIME:LAST:"Current\:%0.2lf %Ss"  \
GPRINT:STARTTRANSFER_TIME:AVERAGE:"Avg\:%0.2lf %Ss"  \
GPRINT:STARTTRANSFER_TIME:MAX:"Max\:%0.2lf %Ss"  \
GPRINT:STARTTRANSFER_TIME:MIN:"Min\:%0.2lf %Ss"  \
COMMENT:" \n" \
HRULE:${Alarm}#ff0000:"(Alarm)" \
COMMENT:" \n" \
COMMENT:" \n" \
COMMENT:"\t\t\t\t\t\t\t\t\t\tLast Updated \:$(date '+%Y-%m-%d %H\:%M')\n"

elif [ "$rrdtype" == "download" ]; then
/usr/local/rrdtool/bin/rrdtool graph ${pngfile} -w 320 -h 102 \
-c SHADEA#808080 \
-c SHADEB#808080 \
-c FRAME#006600 \
-c ARROW#FF0000 \
-c AXIS#000000 \
-c CANVAS#eeffff \
-c BACK#ffffff \
-t "Website download speed statistics-${appname}" -v "Speed(Bytes/sec)" \
--start ${GraphStart} \
 --end ${GraphEnd} \
--lower-limit=0 \
--base=1024 \
-u ${ymax} -r  \
DEF:SPEED_DOWNLOAD=${rrdfile}:SPEED_DOWNLOAD:AVERAGE \
COMMENT:" \n" \
AREA:SPEED_DOWNLOAD#68CEFF:SPEED_DOWNLOAD \
GPRINT:SPEED_DOWNLOAD:AVERAGE:"Avg\:%6.0lf%Sbyte"  \
GPRINT:SPEED_DOWNLOAD:MAX:"Max\:%6.0lf%Sbyte"  \
GPRINT:SPEED_DOWNLOAD:MIN:"Min\:%6.0lf%Sbyte"  \
COMMENT:" \n"

elif [ "$rrdtype" == "unavailable" ]; then
/usr/local/rrdtool/bin/rrdtool graph ${pngfile}  -w 320 -h 102 \
-c SHADEA#808080 \
-c SHADEB#808080 \
-c FRAME#006600 \
-c ARROW#FF0000 \
-c AXIS#000000 \
-c CANVAS#eeffff \
-c BACK#ffffff \
-t "Website usability statistics-${appname}" -v "Number" \
--start ${GraphStart} \
 --end ${GraphEnd} \
--lower-limit=0 \
--base=1024 \
-u 1 -r  \
DEF:UNAVAILABLE=${rrdfile}:UNAVAILABLE:AVERAGE \
COMMENT:" \n" \
AREA:UNAVAILABLE#33ff00:Serviceunavailable \
GPRINT:UNAVAILABLE:AVERAGE:"Avg\:%0.2lf"  \
GPRINT:UNAVAILABLE:MAX:"Max\:%0.2lf"  \
GPRINT:UNAVAILABLE:MIN:"Min\:%0.2lf"  \
COMMENT:" \n"
else
    echo "ERROR!"
fi