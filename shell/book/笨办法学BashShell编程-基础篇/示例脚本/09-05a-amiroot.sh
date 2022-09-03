#!/bin/bash
# 判断是否是root用户（1）

ROOT_UID=0

if [ "$UID" -eq "$ROOT_UID" ]
then
  echo "You are root."
else
  echo "You are just an ordinary usr."
fi

exit 0
