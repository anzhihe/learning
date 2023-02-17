#!/bin/sh
#进入文件目录
cd `dirname $0`
#将redis中所有key暂存至文件
redis-cli -h 192.168.128.167 -p 6381 -c  keys "*" > allkeys3.txt
sum=0
for key in `cat allkeys3.txt`; do
  #循环处理每一个key
  redis-cli -h 192.168.128.167 -p 6381 -c  MIGRATE 192.168.128.167 6379 $key 0 10000 COPY REPLACE
  sum=$((sum+1))
  if [ $((sum%1000)) -eq 0 ]; then
    echo "处理数据$((sum/1000))千"
  fi
done