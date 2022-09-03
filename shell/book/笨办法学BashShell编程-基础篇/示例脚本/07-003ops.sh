#!/bin/bash
declare -a colors
echo "Enter your favorite colors (separated from each other by a space)."
read -a colors

# 直接输出所有元素
echo 
echo ${colors[@]}

# 遍历方法1
echo
element_count=${#colors[@]}	# 使用${#color[*]}也一样
index=0
while [ "$index" -lt "$element_count" ]
do
  echo ${colors[$index]}
  let "index=$index+1"		# index+=1
done

# 遍历方法2
echo
for i in "${colors[@]}"
do
  echo "$i"
done

exit 0
