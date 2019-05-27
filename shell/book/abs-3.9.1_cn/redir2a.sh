#!/bin/bash

# 这是上个脚本的另一个版本. 

#  Heiner Steven建议, 
#+ 为了避免重定向循环运行在子shell中(老版本的shell会这么做), 最好让重定向循环运行在当前工作区内, 
#+ 这样的话, 需要提前进行文件描述符重定向, 
#+ 因为变量如果在(子shell上运行的)循环中被修改的话, 循环结束后并不会保存修改后的值. 


if [ -z "$1" ]
then
  Filename=names.data     # 如果没有指定文件名则使用默认值. 
else
  Filename=$1
fi  


exec 3<&0                 # 将stdin保存到文件描述符3. 
exec 0<"$Filename"        # 重定向标准输入. 

count=0
echo


while [ "$name" != Smith ]
do
  read name               # 从stdin(现在已经是$Filename了)中读取. 
  echo $name
  let "count += 1"
done                      #  从文件$Filename中循环读取
                          #+ 因为文件(译者注：指默认文件, 在本节最后)有20行. 

#  这个脚本原先在"while"循环的结尾还有一句: 
#+      done <"$Filename" 
#  练习:
#  为什么不需要这句了? 


exec 0<&3                 # 恢复保存的stdin. 
exec 3<&-                 # 关闭临时文件描述符3. 

echo; echo "$count names read"; echo

exit 0
