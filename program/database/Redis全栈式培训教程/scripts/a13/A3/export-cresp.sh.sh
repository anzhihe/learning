#!/bin/sh
#进入文件目录
cd `dirname $0`
#将 redis 中所有 key 暂存至文件
redis-cli keys "*" > allkeys1.txt
echo '' > allvalues1.txt
sum=0
for key in `cat allkeys1.txt`; do
 #循环处理每一个 key
 value=`redis-cli --no-raw dump $key`
 echo -E "restore ${key} 0 ${value} replace" >> allvalues1.txt
 sum=$((sum+1))
 if [ "$((sum%1000))" = "0" ]; then
  echo "处理数据$((sum/1000))千"
 fi
done