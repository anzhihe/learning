#!/bin/bash
# 使用shift来逐步存取所有位置参数
# 需要传递本脚本多个位置参数，比如：
# 04-07shift.sh a b c d 1 2 3

until [ -z "$1" ]
do 
  echo -n "$1 "
  shift
done

echo 
exit 0
