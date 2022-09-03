#!/bin/bash
# 整型还是数字？

a=2334		# 全是数字，所以是整型
let "a += 1"
echo "a = $a"	# a =2335，还是整型
echo

# 变量扩展，子串替换，将23替换成BB，就变成字符串了
b=${a/23/BB}
echo "b = $b"	# b = BB35
echo 

# 即使被declare命令声明为整型，也是无效的
declare -i b
echo "b = $b"	# b = BB35
echo 

# 在四则运算时，let命令会将字符串当作零
let "b += 1"	# BB35 +1 = 
echo "b = $b"	# b = 1
echo

c=BB34
echo "c = $c"	# c = BB34
d=${c/BB/23}	# 替换后，$d变成一个整型
echo "d = $d"	# d = 2334
let "d += 1"	# 2334+1
echo "d = $d"	# d = 2335
echo

# 空字符串呢？
e=""
echo "e = $e"	# e = 
let "e += 1"	# 空字符串也被当作零
echo "e = $e"	# e = 1
echo 

# 未声明的变量呢？
echo "f = $f"	# f = 
let "f += 1"	# 未声明的变量也被当作零
echo "f = $f"	# f = 1

exit 0
