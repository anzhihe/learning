#!/bin/bash

# 赋值
a=1
echo "The value of \"a\" is $a."
echo

# 使用let赋值
let a=1+2
echo "The value of \"a\" is now $a."
echo 

# 在for循环中
echo -n "Values of \"a\" in the loop are:"
for a in 7 8 9 10
do
  echo -n "$a "
done
echo

# 使用read命令
echo -n "Enter \"a\" "
read a
echo "The value of \"a\" is now $a. "
echo 

exit 0
