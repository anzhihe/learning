#!/bin/bash

# 测试1：转义的空格
set a\ b c d\ e
#     ^      ^     转义的空格
#       ^ ^      未转义的空格

echo "Test1 Paramter Count: $#"

# 测试2：反转位置参数
OldIFS=$IFS ; IFS=:

until [ $# -eq 0 ]
do
  echo "### k0 = "$k""
  k=$1:$k

  echo "### k = "$k""
  shift
done

set $k
echo "Test2 Paramter Count: $#"

for i 	# 如果省略了"in list"结构，就用位置参数来设置变量i
do
  echo $i
done
IFS=$OldIFS

exit 0
