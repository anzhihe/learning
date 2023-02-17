#!/bin/sh
#进入文件目录
cd `dirname $0`
cat allvalues.txt|redis-cli
sum=`cat allvalues.txt|wc -l`
echo "导入完毕,条数:${sum}"