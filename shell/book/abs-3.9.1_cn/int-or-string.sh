#!/bin/bash
# int-or-string.sh: 整型还是字符串?

a=2334                   # 整型.
let "a += 1"
echo "a = $a "           # a = 2335
echo                     # 还是整型.


b=${a/23/BB}             # 将"23"替换成"BB".
                         # 这将把变量b从整型变为字符串.
echo "b = $b"            # b = BB35
declare -i b             # 即使使用declare命令也不会对此有任何帮助.
echo "b = $b"            # b = BB35

let "b += 1"             # BB35 + 1 =
echo "b = $b"            # b = 1
echo

c=BB34
echo "c = $c"            # c = BB34
d=${c/BB/23}             # 将"BB"替换成"23".
                         # 这使得变量$d变为一个整形.
echo "d = $d"            # d = 2334
let "d += 1"             # 2334 + 1 =
echo "d = $d"            # d = 2335
echo

# null变量会如何呢?
e=""
echo "e = $e"            # e =
let "e += 1"             # 算术操作允许一个null变量?
echo "e = $e"            # e = 1
echo                     # null变量将被转换成一个整型变量.

# 如果没有声明变量会怎样?
echo "f = $f"            # f =
let "f += 1"             # 算术操作能通过么?
echo "f = $f"            # f = 1
echo                     # 未声明的变量将转换成一个整型变量.



# 所以说Bash中的变量都是不区分类型的.

exit 0
