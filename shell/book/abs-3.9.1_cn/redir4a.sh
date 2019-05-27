#!/bin/bash

if [ -z "$1" ]
then
  Filename=names.data          # 如果没有指定文件名, 则使用默认值. 
else
  Filename=$1
fi  

Savefile=$Filename.new         # 保存最终结果的文件名. 
FinalName=Jonah                # 终止"read"时的名称. 

line_count=`wc $Filename | awk '{ print $1 }'`  # 目标文件的行数. 


for name in `seq $line_count`
do
  read name
  echo "$name"
  if [ "$name" = "$FinalName" ]
  then
    break
  fi  
done < "$Filename" > "$Savefile"     # 重定向stdin到文件$Filename, 
#    ^^^^^^^^^^^^^^^^^^^^^^^^^^^       并且将它保存到备份文件中. 

exit 0
