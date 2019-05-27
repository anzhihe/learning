#!/bin/bash
if [ "$1" = "start" ];then
  psid=`ps aux|grep "yorserver"|grep -v "grep"|wc -l`
  if [ $psid -gt 2 ];then
    echo "yorserver is running!"
    exit 0
  else
    cd /usr/local/yorserver/bin
    ./yorserver &
  fi
elif [ "$1" = "stop" ];then
  killall -9 yorserver
  sleep 2
  echo "Stop yorserver service [OK]"
elif [ "$1" = "restart" ];then
  killall -9 yorserver
  cd /usr/local/yorserver/bin
  ./yorserver &
  echo "Restart yorserver service [OK]"
else
  echo "Usages: sh server.sh [start|stop|restart]"
fi