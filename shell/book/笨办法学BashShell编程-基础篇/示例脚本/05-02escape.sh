#!/bin/bash
# 转义符

# 在双引号中，会输出 \v\v\v\v
echo "\v\v\v\v"
echo 

# echo 使用-e选项，做转义处理
echo "================"
echo "VERTICAL TABS"
echo -e "\v\v\v\v"	# 打印4个垂直制表符
echo "================"

echo "QUOTATION MARK"
echo -e "\042"		# 8进制ASCII码的42，是双引号
echo "================"
echo

# 如果使用$'\X'结构，就不需要-e选项了
echo "NEWLINE AND BEEP"
echo $'\n'
echo $'\a'		# 蜂鸣
echo "================"

echo
echo "QUOTATION MARKS"
echo $'\t \042 \t'	# 被水平制表符 包围的双引号
echo $'\t \x22 \t'	# 与上面类似，换成16进制数
echo "================"

# 给变量赋值，ASCII字符
quote=$'\042'
echo "$quote This is a quoted stirng, $quote and this lies outside the qutotes"
echo 

# 变量的值，可以有多个ASCII字符
triple_underline=$'\137\137\137' # 八进制137是下划线
echo "$triple_underline UNDERLINE $triple_underline"
echo 

exit 0
