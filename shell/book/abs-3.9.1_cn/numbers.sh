#!/bin/bash
# numbers.sh: 几种不同数制的数字表示法.

# 10进制: 默认情况
let "dec = 32"
echo "decimal number = $dec"             # 32
# 这没什么特别的.


# 8进制: 以'0'(零)开头 
let "oct = 032"
echo "octal number = $oct"               # 26
# 表达式结果是用10进制表示的.
# ---------------------------

# 16进制: 以'0x'或者'0X'开头的数字
let "hex = 0x32"
echo "hexadecimal number = $hex"         # 50
# 表达式结果是用10进制表示的.

# 其他进制: BASE#NUMBER
# BASE的范围在2到64之间.
# NUMBER的值必须使用BASE范围内的符号来表示, 具体看下边的示例. 


let "bin = 2#111100111001101"
echo "binary number = $bin"              # 31181

let "b32 = 32#77"
echo "base-32 number = $b32"             # 231

let "b64 = 64#@_"
echo "base-64 number = $b64"             # 4031
# 这个表示法只能工作于受限的ASCII字符范围(2 - 64).
# 10个数字 + 26个小写字母 + 26个大写字符 + @ + _


echo

echo $((36#zz)) $((2#10101010)) $((16#AF16)) $((53#1aA))
                                         # 1295 170 44822 3375


#  重要的注意事项:
#  ---------------
#  使用一个超出给定进制的数字的话, 
#+ 将会引起一个错误. 

let "bad_oct = 081"
# (部分的) 错误消息输出:
#  bad_oct = 081: value too great for base (error token is "081")
#              Octal numbers use only digits in the range 0 - 7.

exit 0       # 感谢, Rich Bartell 和 Stephane Chazelas的指正. 
