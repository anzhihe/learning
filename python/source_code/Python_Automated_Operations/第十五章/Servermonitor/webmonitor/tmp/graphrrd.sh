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
--title "应用请求响应时间统计-${appname}" -v "速度 (秒)" \
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
AREA:TOTAL_TIME#0011ff:总共时间 \
GPRINT:TOTAL_TIME:LAST:"当前\:%0.2lf %Ss"  \
GPRINT:TOTAL_TIME:AVERAGE:"平均\:%0.2lf %Ss"  \
GPRINT:TOTAL_TIME:MAX:"最大\:%0.2lf %Ss"  \
GPRINT:TOTAL_TIME:MIN:"最小\:%0.2lf %Ss"  \
COMMENT:" \n" \
LINE1:NAMELOOKUP_TIME#eeee00:域名解析 \
GPRINT:NAMELOOKUP_TIME:LAST:"当前\:%0.2lf %Ss"  \
GPRINT:NAMELOOKUP_TIME:AVERAGE:"平均\:%0.2lf %Ss"  \
GPRINT:NAMELOOKUP_TIME:MAX:"最大\:%0.2lf %Ss"  \
GPRINT:NAMELOOKUP_TIME:MIN:"最小\:%0.2lf %Ss"  \
COMMENT:" \n" \
LINE1:CONNECT_TIME#00aa00:连接时间 \
GPRINT:CONNECT_TIME:LAST:"当前\:%0.2lf %Ss"  \
GPRINT:CONNECT_TIME:AVERAGE:"平均\:%0.2lf %Ss"  \
GPRINT:CONNECT_TIME:MAX:"最大\:%0.2lf %Ss"  \
GPRINT:CONNECT_TIME:MIN:"最小\:%0.2lf %Ss"  \
COMMENT:" \n" \
LINE1:PRETRANSFER_TIME#ff5511:开始传输 \
GPRINT:PRETRANSFER_TIME:LAST:"当前\:%0.2lf %Ss"  \
GPRINT:PRETRANSFER_TIME:AVERAGE:"平均\:%0.2lf %Ss"  \
GPRINT:PRETRANSFER_TIME:MAX:"最大\:%0.2lf %Ss"  \
GPRINT:PRETRANSFER_TIME:MIN:"最小\:%0.2lf %Ss"  \
COMMENT:" \n" \
LINE1:STARTTRANSFER_TIME#004455:第一字节 \
GPRINT:STARTTRANSFER_TIME:LAST:"当前\:%0.2lf %Ss"  \
GPRINT:STARTTRANSFER_TIME:AVERAGE:"平均\:%0.2lf %Ss"  \
GPRINT:STARTTRANSFER_TIME:MAX:"最大\:%0.2lf %Ss"  \
GPRINT:STARTTRANSFER_TIME:MIN:"最小\:%0.2lf %Ss"  \
COMMENT:" \n" \
HRULE:${Alarm}#ff0000:"(报警值)" \
COMMENT:" \n" \
COMMENT:" \n" \
COMMENT:"\t\t\t\t\t\t\t\t\t\t最后更新 \:$(date '+%Y-%m-%d %H\:%M')\n"

elif [ "$rrdtype" == "download" ]; then
/usr/bin/rrdtool graph ${pngfile} -w 320 -h 102 \
-n TITLE:10:${rrdtool_font} \
-n UNIT:8:${rrdtool_font} \
-n LEGEND:8:${rrdtool_font} \
-n AXIS:8:${rrdtool_font} \
-c SHADEA#808080 \
-c SHADEB#808080 \
-c FRAME#006600 \
-c ARROW#FF0000 \
-c AXIS#000000 \
-c CANVAS#eeffff \
-c BACK#ffffff \
-t "应用下载速度统计-${appname}" -v "速度 (字节/秒)" \
--start ${GraphStart} \
 --end ${GraphEnd} \
--lower-limit=0 \
--base=1024 \
-u ${ymax} -r  \
DEF:SPEED_DOWNLOAD=${rrdfile}:SPEED_DOWNLOAD:AVERAGE \
COMMENT:" \n" \
AREA:SPEED_DOWNLOAD#68CEFF:下载速度 \
GPRINT:SPEED_DOWNLOAD:AVERAGE:"平均\:%6.0lf%Sbyte"  \
GPRINT:SPEED_DOWNLOAD:MAX:"最大\:%6.0lf%Sbyte"  \
GPRINT:SPEED_DOWNLOAD:MIN:"最小\:%6.0lf%Sbyte"  \
COMMENT:" \n"

elif [ "$rrdtype" == "unavailable" ]; then
/usr/bin/rrdtool graph ${pngfile}  -w 320 -h 102 \
-n TITLE:10:${rrdtool_font} \
-n UNIT:8:${rrdtool_font} \
-n LEGEND:8:${rrdtool_font} \
-n AXIS:8:${rrdtool_font} \
-c SHADEA#808080 \
-c SHADEB#808080 \
-c FRAME#006600 \
-c ARROW#FF0000 \
-c AXIS#000000 \
-c CANVAS#eeffff \
-c BACK#ffffff \
-t "应用可用性统计-${appname}" -v "次数 (次)" \
--start ${GraphStart} \
 --end ${GraphEnd} \
--lower-limit=0 \
--base=1024 \
-u 1 -r  \
DEF:UNAVAILABLE=${rrdfile}:UNAVAILABLE:AVERAGE \
COMMENT:" \n" \
AREA:UNAVAILABLE#33ff00:服务不可用 \
GPRINT:UNAVAILABLE:AVERAGE:"平均\:%0.2lf"  \
GPRINT:UNAVAILABLE:MAX:"最大\:%0.2lf"  \
GPRINT:UNAVAILABLE:MIN:"最小\:%0.2lf"  \
COMMENT:" \n"
else
    echo "ERROR!"
fi