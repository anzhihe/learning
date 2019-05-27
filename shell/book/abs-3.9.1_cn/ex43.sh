#!/bin/bash

y=`eval ls -l`  #  与 y=`ls -l` 很相似
echo $y         #+ 但是换行符将会被删除, 因为"echo"的变量未被""引用.
echo
echo "$y"       #  用""将变量引用起来, 换行符就不会被空格替换了.

echo; echo

y=`eval df`     #  与 y=`df` 很相似
echo $y         #+ 换行符又被空格替换了.

#  当没有LF(换行符)出现时, 如果使用"awk"这样的工具来分析输出的结果, 
#+ 应该能更容易一些.

echo
echo "==========================================================="
echo

# 现在,来看一下怎么用"eval"命令来"扩展"一个变量 . . .

for i in 1 2 3 4 5; do
  eval value=$i
  #  value=$i 具有相同的效果, 在这里并不是非要使用"eval"不可. 
  #  一个缺乏特殊含义的变量将被评价为自身 -- 也就是说,
  #+ 这个变量除了能够被扩展成自身所表示的字符外, 不能被扩展成任何其他的含义.
  echo $value
done

echo
echo "---"
echo

for i in ls df; do
  value=eval $i
  #  value=$i 在这里就与上边这句有了本质上的区别.
  #  "eval" 将会评价命令 "ls" 和 "df" . . .
  #  术语 "ls" 和 "df" 就具有特殊含义,
  #+ 因为它们被解释成命令,
  #+ 而不是字符串本身.
  echo $value
done


exit 0
