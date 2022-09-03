#!/bin/bash
# 变量赋值和替换

a=123
hello=$a

# ------------------------------------------------------------------
# 强烈注意：赋值时，等号前后一定要不要空格
#
# 1、如果等号前面有空格？
# 	VARIABLE =value
#    将执行带一个参数=value的命令 VARIABLE
# 
# 2、如果等号后面有空格？
#	VARIABLE= value
#    将执行后面这个小写的value命令，并且带一个赋值为""的变量VARIABLE
# ------------------------------------------------------------------
 
echo hello # 这不是一个变量，所以只会输出hello

echo  $hello
echo  ${hello}  # 结果同上一行

echo "$hello"
echo '$hello'

echo 

# 新示例1：---------------------------------------------
#   引用变量，会保留其中的空白。变量替换就不保留空白
hello="A B  C   D"
echo $hello    # 会输出 A B C D
echo "$hello"  # 会输出 A B  C   D
echo

#   全引用将$解释为单独的字符，而不是变量的前缀
echo '$hello'  # 会输出$hello
echo  

# 设置变量，但是没有赋值，即值为null 空
#     这与unset一个变量是不一样的，虽然结果一样
hello=
echo "\$hello (null value) = $hello"
echo 


# 新示例2：---------------------------------------------
# 可以在同一行上设置多个变量，变量之间通过空格来分隔
# 由于这会降低了可读性、可移植性，所以不推荐！

var1=1 var2=2 var3=3
echo "var1=$var1 var2=$var22 var3=$var3"
echo 

# 新示例3：---------------------------------------------
# 如果变量的值存在空白，必须加处引用

# numbers=1 2 3   # 这是错误的写法
numbers="1 2 3"
echo "numbers=$numbers"
echo 

# 新示例4：---------------------------------------------
# 没有声明(初始化)变量，就直接引用, 是一个空值
echo "uninitialized_variable = $uninitialized_variable"

# 声明了变量，但没有赋值(初始化)，也是一个空值
uninitialized_variable=
echo "uninitialized_variable = $uninitialized_variable"
 
# unset一个变量，会清除占用的内存空间
uninitialized_variable=123
unset uninitialized_variable
echo "uninitialized_variable = $uninitialized_variable"
                               # 还是一个空值

echo
exit 0
