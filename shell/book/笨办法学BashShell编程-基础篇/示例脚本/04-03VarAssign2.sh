#!/bin/bash
# 简单赋值与命令替换式的赋值

# 简单赋值
a=1
echo a$
b=2
echo b$

# 命令替换式赋值
c=`echo Hello!`
echo $c

# 如果将在命令行来执行第11行，会出错
# 这是因为感叹号!会触发Bash的“命令历史”机制

d=`ls -l`
#对比以下两次echo变量D的值，有什么不同
echo $d
echo 
echo "$d"

exit 0
