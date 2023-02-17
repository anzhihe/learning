#!/bin/sh
#进入文件目录
cd `dirname $0`
#将redis中所有key暂存至文件
redis-cli keys "*" > allkeys4.txt
sum=0
for key in `cat allkeys4.txt`; do
  #循环处理每一个key
  redis-cli -c  MIGRATE 192.168.128.167 6381 $key 0 10000 COPY REPLACE
  sum=$((sum+1))
  if [ $((sum%1000)) -eq 0 ]; then
    echo "处理数据$((sum/1000))千"
  fi
done