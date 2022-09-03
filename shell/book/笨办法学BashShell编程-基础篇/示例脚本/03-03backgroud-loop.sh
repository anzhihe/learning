#!/bin/bash
# 03-03backgroud-loop.sh

for i in 1 2 3 4 5 6 7 8 9 10 # 第一个循环
do
  echo -n "$i "
done &   # 在后台执行这个循环

echo 

for i in 11 12 13 14 15 16 17 18 19 20 # 第二个循环
do
  echo -n "$i "
done    # 正常地在前台执行这个循环

echo 
exit 0
