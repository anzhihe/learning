#!/bin/sh
#进入文件目录
cd `dirname $0`
#将redis中所有key暂存至文件
redis-cli keys "*" > allkeys.txt
echo '' > allvalues.txt
sum=0
for key in `cat allkeys.txt`; do
  #循环处理每一个key
  value=`redis-cli get $key`
  echo set ${key} ${value} >> allvalues.txt
  sum=$((sum+1))
  if [ "$((sum%1000))" = "0" ]; then
    echo "处理数据$((sum/1000))千"
  fi
done