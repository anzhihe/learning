#!/bin/bash
# 引用练习 + 变量赋值练习

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
exit

