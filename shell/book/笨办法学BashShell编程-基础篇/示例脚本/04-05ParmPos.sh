#!/bin/bash

# 调用这个脚本，至少需要10个参数
# ./04-05ParmPos.sh 1 2 3 4 5 6 7 8 9 10

MINPARAMS=10

# 脚本名称
echo "The name of this script is \"$0\"."
echo "The name of this script is \"`basename $0`\"."
echo

# 测试变量引用
if [ -n "$1" ]
then
  echo "Parameter #1 is $1"
fi

if [ -n "$2" ]
then
  echo "Parameter #2 is $2"
fi

if [ -n "$3" ]
then
  echo "Parameter #3 is $3"
fi
# ..... 以后，咱们用循环来写

if [ -n "${10}" ]
then
  echo "Parameter #10 is ${10}"
fi

echo "-------------------------"
echo "All the commnad-line parameters are: \"$*\""

if [ $# -lt "$MINPARAMS" ]
then
  echo 
  echo "This script needs at least $MINIPARAMS commnd-line arguments!"
fi

exit 0
