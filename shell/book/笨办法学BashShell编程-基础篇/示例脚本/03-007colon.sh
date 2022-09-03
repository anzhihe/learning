#!/bin/bash
# 示例代码：冒号 colon，空命令 null command

# 例1：死循环 Endless loop

while :   # 本行等同于 while true
do
  operation-1
  operation-2
  operation-3
done 

# 例2：if/then的占用符 placeholder

if condition
then : 	# 什么都不做，引出分支，有可能以后再补充 
else
  take-some-action
fi 

# 例3：清空一个文件，但不会修改该文件的权限，也cat /dev/null类似
#	由于空命令是一个内建的命令，所以不会生产一个新进程 

: > testdata.txt

