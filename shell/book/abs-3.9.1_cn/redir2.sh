#!/bin/bash
# redir2.sh

if [ -z "$1" ]
then
  Filename=names.data       # 如果没有指定文件名, 则使用这个默认值. 
else
  Filename=$1
fi  
#+ Filename=${1:-names.data}
#  这句可代替上面的测试(参数替换).

count=0

echo

while [ "$name" != Smith ]  # 为什么变量$name要用引号?
do
  read name                 # 从$Filename文件中读取输入, 而不是在stdin中读取输入. 
  echo $name
  let "count += 1"
done <"$Filename"           # 重定向stdin到文件$Filename. 
#    ^^^^^^^^^^^^

echo; echo "$count names read"; echo

exit 0

#  注意在一些比较老的shell脚本编程语言中, 
#+ 重定向的循环是放在子shell里运行的. 
#  因此, $count 值返回后会是 0, 此值是在循环开始前的初始值. 
#  *如果可能的话*, 尽量避免在Bash或ksh中使用子shell,
#+ 所以这个脚本能够正确的运行. 
#  (多谢Heiner Steven指出这个问题.)

#  然而 . . .
#  Bash有时还是*会*在一个使用管道的"while-read"循环中启动一个子shell, 
#+ 与重定向的"while"循环还是有区别的. 

abc=hi
echo -e "1\n2\n3" | while read l
     do abc="$l"
        echo $abc
     done
echo $abc

#  感谢, Bruno de Oliveira Schneider
#+ 给出上面的代码片段来演示此问题. 
#  同时, 感谢, Brian Onn, 修正了一个注释错误. 
