#!/bin/bash
# 数组练习：打印一首诗
Line[1]="Moonlight before my bed,"
Line[2]="Could it be frost instead?"
Line[3]="Head up, I watch the moon;"
Line[4]="Head down, I think of home."
declare -A poem
poem["Author"]="Li Bai"
poem["Title"]="Quiet Night Thoughts"

echo
for index in 1 2 3 4 ; do	# 也可以使用`seq 1 4`
  echo ${Line[index]}
done

echo
for subscript in ${!poem[*]}; do
  echo ${poem[$subscript]}
done
exit 0
