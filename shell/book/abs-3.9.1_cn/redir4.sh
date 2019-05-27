#!/bin/bash

if [ -z "$1" ]
then
  Filename=names.data          # 如果没有指定文件名就使用默认值. 
else
  Filename=$1
fi  

line_count=`wc $Filename | awk '{ print $1 }'`
#           目标文件的行数. 
#
#  此处的代码太过做作, 并且写得很难看, 
#+ 但至少展示了"for"循环的stdin可以重定向...
#+ 当然, 你得足够聪明, 才能看得出来. 
#
# 更简洁的写法是     line_count=$(wc -l < "$Filename")


for name in `seq $line_count`  # "seq"打印出数字序列. 
# while [ "$name" != Smith ]   --   比"while"循环更复杂   --
do
  read name                    # 从$Filename中, 而非从stdin中读取. 
  echo $name
  if [ "$name" = Smith ]       # 因为用for循环, 所以需要这个多余测试. 
  then
    break
  fi  
done <"$Filename"              # 重定向stdin到文件$Filename. 
#    ^^^^^^^^^^^^

exit 0
