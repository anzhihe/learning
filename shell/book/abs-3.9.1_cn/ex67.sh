#!/bin/bash

declare -a colors
#  脚本中所有的后续命令都会把
#+ 变量"colors"看作数组. 

echo "Enter your favorite colors (separated from each other by a space)."

read -a colors    # 至少需要键入3种颜色, 以便于后边的演示. 
#  'read'命令的特殊选项, 
#+ 允许给数组元素赋值. 

echo

element_count=${#colors[@]}
# 提取数组元素个数的特殊语法. 
#     用element_count=${#colors[*]}也一样. 
#
#  "@"变量允许在引用中存在单词分割(word splitting)
#+ (依靠空白字符来分隔变量). 
#
#  这就好像"$@"和"$*"
#+ 在位置参数中的所表现出来的行为一样. 

index=0

while [ "$index" -lt "$element_count" ]
do    # 列出数组中的所有元素. 
  echo ${colors[$index]}
  let "index = $index + 1"
  # 或:
  #    index+=1
  # 如果你运行的Bash版本是3.1以后的话, 才支持这种语法. 
done
# 每个数组元素被列为单独的一行. 
# 如果没有这种要求的话, 可以使用echo -n "${colors[$index]} "
#
# 也可以使用"for"循环来做: 
#   for i in "${colors[@]}"
#   do
#     echo "$i"
#   done
# (感谢, S.C.)

echo

# 再次列出数组中的所有元素, 不过这次的做法更优雅. 
  echo ${colors[@]}          # 用echo ${colors[*]}也行. 

echo

# "unset"命令即可以删除数组数据, 也可以删除整个数组. 
unset colors[1]              # 删除数组的第2个元素. 
                             # 作用等效于   colors[1]=
echo  ${colors[@]}           # 再次列出数组内容, 第2个元素没了. 

unset colors                 # 删除整个数组. 
                             #  unset colors[*] 或
                             #+ unset colors[@] 都可以. 
echo; echo -n "Colors gone."			   
echo ${colors[@]}            # 再次列出数组内容, 内容为空. 

exit 0
