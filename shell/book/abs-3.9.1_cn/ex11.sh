#!/bin/bash

echo

if test -z "$1"
then
  echo "No command-line arguments."
else
  echo "First command-line argument is $1."
fi

echo

if /usr/bin/test -z "$1"      # 与内建的"test"命令结果相同. 
then
  echo "No command-line arguments."
else
  echo "First command-line argument is $1."
fi

echo

if [ -z "$1" ]                # 与上边的代码块作用相同.
#   if [ -z "$1"                应该能够运行, 但是...
#+  Bash报错, 提示缺少关闭条件测试的右中括号. 
then
  echo "No command-line arguments."
else
  echo "First command-line argument is $1."
fi

echo


if /usr/bin/[ -z "$1" ]       # 再来一个, 与上边的代码块作用相同.
# if /usr/bin/[ -z "$1"       # 能够工作, 但是还是给出一个错误消息.
#                             # 注意:
#                               在版本3.x的Bash中, 这个bug已经被修正了.
then
  echo "No command-line arguments."
else
  echo "First command-line argument is $1."
fi

echo

exit 0
