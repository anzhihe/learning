#!/bin/bash
# "裸体"变量

echo

# 变量什么时候是"裸体"的, 比如前边少了$的时候?
# 当它被赋值的时候, 而不是被引用的时候.

# 赋值
a=879
echo "The value of \"a\" is $a."

# 使用'let'赋值
let a=16+5
echo "The value of \"a\" is now $a."

echo

# 在'for'循环中(事实上, 这是一种伪赋值):
echo -n "Values of \"a\" in the loop are: "
for a in 7 8 9 11
do
  echo -n "$a "
done

echo
echo

# 使用'read'命令进行赋值(这也是一种赋值的类型):
echo -n "Enter \"a\" "
read a
echo "The value of \"a\" is now $a."

echo

exit 0
