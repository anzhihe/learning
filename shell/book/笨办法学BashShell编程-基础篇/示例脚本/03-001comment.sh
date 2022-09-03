#!/bin/bash

# This is a comment.

echo "A commnet will follow " # 注释在这里
# 注意上一条语句中，#号前面要有一个空格

	# A tab precede this comment
# 注意上一条语句中，注释是放在本行 行首空白的后面

# echo中被引号的#，是不能被当作的注释的
# echo中被转义的#，是不能被当作的注释的
# 反斜线是转义字符

echo "111-双引号  The # here does not begin a comment." 
echo '222-单引号  The # here does not begin a comment.' 
echo 333-无引导且有转义  The \# here does not begin a comment.
echo 444-无引号无转义 The # here begin a comment.

# 在特定的参数替换结构中，#号不是注释
echo ${PATH#*:} # 效果：将第一个冒号之前的删除

# 在数字常量表达式中，#号不是注释
echo $((2#101011))  # 数制转换，2进制转换为10进制，这不是注释 
