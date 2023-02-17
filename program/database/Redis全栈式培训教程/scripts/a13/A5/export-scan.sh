#!/bin/sh
cursor=-1;keys='';pattern=*;count=100;sum=0
echo ''>allkeys.txt
#从游标0开始循环
while [ $cursor -ne 0 ]; do
   if [ $cursor -eq -1 ]; then
     cursor=0
   fi
   reply=`redis-cli --csv SCAN $cursor MATCH "$pattern" COUNT $count`
   #替换双引号,把"a1","b2","a3"替换为a1,b2,a3
   reply=`echo $reply | sed 's/\"//g'`
   #第一列为下次游标数
   cursor=`echo $reply | awk -F ',' '{print $1}'`
   #其它的列为key列表
   cols=`echo $reply | awk -F ',' '{$1="";print $0}'`
   #分割字符串，循环处理
   array=(${cols})
   for col in ${array[@]}; do
    sum=$((sum+1))
    if [ $((sum%1000)) -eq 0 ]; then
      echo "处理数据$((sum/1000))千"
    fi
    #下面则是业务处理
    echo "$col" >> allkeys.txt
   done
done
echo "导出key数量为:${sum1}"