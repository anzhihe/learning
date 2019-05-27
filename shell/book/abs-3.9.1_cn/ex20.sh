#!/bin/bash

func1 ()
{
echo This is a function.
}

declare -f        # 列出前面定义的所有函数.

echo

declare -i var1   # var1是个整型变量.
var1=2367
echo "var1 declared as $var1"
var1=var1+1       # 整型变量的声明并不需要使用'let'命令.
echo "var1 incremented by 1 is $var1."
# 尝试修改一个已经声明为整型变量的值.
echo "Attempting to change var1 to floating point value, 2367.1."
var1=2367.1       # 产生错误信息, 并且变量并没有被修改.
echo "var1 is still $var1"

echo

declare -r var2=13.36         # 'declare'允许设置变量的属性, 
                              #+ 同时给变量赋值.
echo "var2 declared as $var2" # 试图修改只读变量的值.
var2=13.37                    # 产生错误消息, 并且从脚本退出.

echo "var2 is still $var2"    # 将不会执行到这行.

exit 0                        # 脚本也不会从此处退出.
