#!/bin/bash
# 反转位置参数
set a b c d e
echo "Test1 Paramter Count: $#"

k=""
until [ $# -eq 0 ]
do			# 步进位置参数
  echo "### k0 = "$k""	# 步进之前
  k=$1:$k		# 将当前变量加到K前面，用分号来分隔

  echo "### k = "$k""	# 步进之后
  shift
done

OldIFS=$IFS ; IFS=:	# 保存旧的IFS，设置新的IFS
set $k			# 设置新的位置参数
IFS=$OldIFS

echo "Test2 Paramter Count: $#"

# 显示新的位置参数
echo $*
for i 	# 如果省略了"in list"结构，就用位置参数来设置变量i
do
  echo $i
done

exit 0
