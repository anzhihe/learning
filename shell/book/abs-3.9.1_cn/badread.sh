#!/bin/bash
#  badread.sh:
#  尝试使用'echo'和'read'命令
#+ 非交互的给变量赋值. 

a=aaa
b=bbb
c=ccc

echo "one two three" | read a b c
# 尝试重新给变量a, b, 和c赋值.

echo
echo "a = $a"  # a = aaa
echo "b = $b"  # b = bbb
echo "c = $c"  # c = ccc
# 重新赋值失败. 

# ------------------------------

# 试试下边这种方法. 

var=`echo "one two three"`
set -- $var
a=$1; b=$2; c=$3

echo "-------"
echo "a = $a"  # a = one
echo "b = $b"  # b = two
echo "c = $c"  # c = three 
# 重新赋值成功. 

# ------------------------------

#  也请注意, echo到'read'的值只会在子shell中起作用. 
#  所以, 变量的值*只*会在子shell中被修改. 

a=aaa          # 重新开始. 
b=bbb
c=ccc

echo; echo
echo "one two three" | ( read a b c;
echo "Inside subshell: "; echo "a = $a"; echo "b = $b"; echo "c = $c" )
# a = one
# b = two
# c = three
echo "-----------------"
echo "Outside subshell: "
echo "a = $a"  # a = aaa
echo "b = $b"  # b = bbb
echo "c = $c"  # c = ccc
echo

exit 0
