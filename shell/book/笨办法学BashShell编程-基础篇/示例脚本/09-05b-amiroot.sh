#!/bin/bash
# 判断是否是root用户（2）

ROOT_NAME=root

username=`id -nu`	# 或者 usrename=`whoami`

if [ "$username" = "$ROOT_NAME" ]
then
  echo "You are root."
else
  echo "You are just an ordinary usr."
fi

exit 0
