#!/bin/sh
rrdfile=$1
rrdtype=$2

if [ "$rrdtype" == "time" ]; then
    /usr/bin/rrdtool updatev $rrdfile $8:$3:$4:$5:$6:$7   
elif [ "$rrdtype" == "download" ]; then
    /usr/bin/rrdtool updatev $rrdfile $4:$3
elif [ "$rrdtype" == "unavailable" ]; then
    /usr/bin/rrdtool updatev $rrdfile $4:$3
else
    echo "ERROR!"
fi