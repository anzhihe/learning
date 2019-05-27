#!/bin/bash
# realname.sh
#
# 依靠username, 从/etc/passwd中获得"真名". 


ARGCOUNT=1       # 需要一个参数. 
E_WRONGARGS=65

file=/etc/passwd
pattern=$1

if [ $# -ne "$ARGCOUNT" ]
then
  echo "Usage: `basename $0` USERNAME"
  exit $E_WRONGARGS
fi  

file_excerpt ()  # 按照要求的模式来扫描文件, 然后打印文件相关的部分. 
{
while read line  # "while"并不一定非得有"[ condition ]"不可. 
do
  echo "$line" | grep $1 | awk -F":" '{ print $5 }'  # awk用":"作为界定符. 
done
} &lt;$file  # 重定向到函数的stdin. 

file_excerpt $pattern

# 是的, 整个脚本其实可以被缩减为
#       grep PATTERN /etc/passwd | awk -F":" '{ print $5 }'
# 或
#       awk -F: '/PATTERN/ {print $5}'
# 或
#       awk -F: '($1 == "username") { print $5 }' # 从username中获得真名. 
# 但是, 这些起不到示例的作用. 

exit 0
