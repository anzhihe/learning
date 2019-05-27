#!/bin/bash

PROCNAME=pppd        # ppp守护进程
PROCFILENAME=status  # 在这里寻找信息. 
NOTCONNECTED=65
INTERVAL=2           # 每2秒刷新一次. 

pidno=$( ps ax | grep -v "ps ax" | grep -v grep | grep $PROCNAME | awk '{ print $1 }' )
# 找出'pppd'所对应的进程号, 即'ppp守护进程'. 
# 必须过滤掉由搜索本身所产生的进程行. 
#
#  然而, 就像Oleg Philon所指出的那样, 
#+ 如果使用"pidof"的话, 就会非常简单. 
#  pidno=$( pidof $PROCNAME )
#
#  从经验中总结出来的忠告: 
#+ 当命令序列变得非常复杂的时候, 一定要找到更简洁的方法. 


if [ -z "$pidno" ]   # 如果没有找到匹配的pid, 那么就说明相应的进程没运行. 
then
  echo "Not connected."
  exit $NOTCONNECTED
else
  echo "Connected."; echo
fi

while [ true ]       # 死循环, 这里可以改进一下. 
do

  if [ ! -e "/proc/$pidno/$PROCFILENAME" ]
  # 进程运行时, 相应的"status"文件就会存在. 
  then
    echo "Disconnected."
    exit $NOTCONNECTED
  fi

netstat -s | grep "packets received"  # 获得一些连接统计. 
netstat -s | grep "packets delivered"


  sleep $INTERVAL
  echo; echo

done

exit 0

# 如果你想停止这个脚本, 只能使用Control-C. 

#    练习:
#    -----
#    改进这个脚本, 使它可以按"q"键退出. 
#    提高这个脚本的用户友好性. 
