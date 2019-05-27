#!/bin/bash
# 和前面的例子相同, 但使用的是"until"循环. 

if [ -z "$1" ]
then
  Filename=names.data         # 如果没有指定文件名那就使用默认值. 
else
  Filename=$1
fi  

# while [ "$name" != Smith ]
until [ "$name" = Smith ]     # 把!=改为=.
do
  read name                   # 从$Filename中读取, 而不是从stdin中读取. 
  echo $name
done <"$Filename"             # 重定向stdin到文件$Filename. 
#    ^^^^^^^^^^^^

# 结果和前面例子的"while"循环相同. 

exit 0
