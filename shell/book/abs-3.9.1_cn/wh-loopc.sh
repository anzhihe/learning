#!/bin/bash
# wh-loopc.sh: 循环10次的"while"循环.

LIMIT=10
a=1

while [ "$a" -le $LIMIT ]
do
  echo -n "$a "
  let "a+=1"
done           # 到目前为止都没有什么令人惊奇的地方.

echo; echo

# +=================================================================+

# 现在, 重复C风格的语法.

((a = 1))      # a=1
# 双圆括号允许赋值两边的空格, 就像C语言一样.

while (( a <= LIMIT ))   # 双圆括号, 变量前边没有"$".
do
  echo -n "$a "
  ((a += 1))   # let "a+=1"
  # Yes, 看到了吧.
  # 双圆括号允许像C风格的语法一样增加变量的值.
done

echo

# 现在, C程序员可以在Bash中找到回家的感觉了吧.

exit 0
