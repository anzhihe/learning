#!/bin/bash

if [ -z "$1" ]
then
  Filename=names.data   # 如果文件名没有指定, 使用默认值. 
else
  Filename=$1
fi  

TRUE=1

if [ "$TRUE" ]          # if true    和   if :   都可以. 
then
 read name
 echo $name
fi <"$Filename"
#  ^^^^^^^^^^^^

# 只读取了文件的第一行. 
# An "if/then"测试结构不能自动地反复地执行, 除非把它们嵌到循环里. 

exit 0
