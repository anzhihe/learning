#!/bin/bash
# 循环指定数的再种方法

# 方法1：传统的办法
n=0
for a in 1 2 3 4 5 6 7 8 9 10; do
  let "n=$n+$a"
done
echo $n 

# 方法：C语言风格
n=0
for ((a=1; a<=100; a++)); do
  let "n=$n+$a"
done
echo $n

exit 0
