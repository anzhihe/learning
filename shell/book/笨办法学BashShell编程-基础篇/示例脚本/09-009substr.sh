#!/bin/bash
# 两种方法获得指定长度了子字符串

stringZ=abcABC123ABCabc

# 方法1 变量替换
#       如果未指定长度，则到末尾
echo ${stringZ:3:3}	# ABC
echo ${stringZ:1}	# bcABC123ABCabc
echo ${stringZ:3}	# ABC123ABCabc
echo 
echo ${stringZ:(-4)}	# Cabc
echo ${stringZ: -4}	# Cabc 注意冒号与-4之间要有空格
echo 

# 方法2 通过expr substr
#       必须指定长度
echo `expr substr $stringZ 1 2 `	# ab
echo `expr substr $stringZ 4 3 `	# ABC
exit 0
