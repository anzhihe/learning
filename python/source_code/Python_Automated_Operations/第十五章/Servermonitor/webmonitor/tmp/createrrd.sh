#!/bin/sh
rrdfile=$1
rrdtype=$2

if [ "$rrdtype" == "time" ]; then
    /usr/bin/rrdtool create $rrdfile \
    --start $(date -d "now" +%s) \
    --step 300 \
    DS:NAMELOOKUP_TIME:GAUGE:600:0:U \
    DS:CONNECT_TIME:GAUGE:600:0:U \
    DS:PRETRANSFER_TIME:GAUGE:600:0:U \
    DS:STARTTRANSFER_TIME:GAUGE:600:0:U \
    DS:TOTAL_TIME:GAUGE:600:0:U \
    RRA:AVERAGE:0.5:1:600 \
    RRA:AVERAGE:0.5:6:700 \
    RRA:AVERAGE:0.5:24:775 \
    RRA:AVERAGE:0.5:288:797 \
    RRA:MAX:0.5:1:600 \
    RRA:MAX:0.5:6:700 \
    RRA:MAX:0.5:24:775 \
    RRA:MAX:0.5:444:797 \
    RRA:MIN:0.5:1:600 \
    RRA:MIN:0.5:6:700 \
    RRA:MIN:0.5:24:775 \
    RRA:MIN:0.5:444:797
    
elif [ "$rrdtype" == "download" ]; then
    /usr/bin/rrdtool create $rrdfile \
    --start $(date -d "now" +%s) \
    --step 300 \
    DS:SPEED_DOWNLOAD:GAUGE:600:0:U \
    RRA:AVERAGE:0.5:1:600 \
    RRA:AVERAGE:0.5:6:700 \
    RRA:AVERAGE:0.5:24:775 \
    RRA:AVERAGE:0.5:288:797 \
    RRA:MAX:0.5:1:600 \
    RRA:MAX:0.5:6:700 \
    RRA:MAX:0.5:24:775 \
    RRA:MAX:0.5:444:797 \
    RRA:MIN:0.5:1:600 \
    RRA:MIN:0.5:6:700 \
    RRA:MIN:0.5:24:775 \
    RRA:MIN:0.5:444:797

elif [ "$rrdtype" == "unavailable" ]; then
    /usr/bin/rrdtool create $rrdfile \
    --start $(date -d "now" +%s) \
    --step 300 \
    DS:UNAVAILABLE:GAUGE:600:0:U \
    RRA:AVERAGE:0.5:1:600 \
    RRA:AVERAGE:0.5:6:700 \
    RRA:AVERAGE:0.5:24:775 \
    RRA:AVERAGE:0.5:288:797 \
    RRA:MAX:0.5:1:600 \
    RRA:MAX:0.5:6:700 \
    RRA:MAX:0.5:24:775 \
    RRA:MAX:0.5:444:797 \
    RRA:MIN:0.5:1:600 \
    RRA:MIN:0.5:6:700 \
    RRA:MIN:0.5:24:775 \
    RRA:MIN:0.5:444:797

else
    echo "ERROR!"
fi