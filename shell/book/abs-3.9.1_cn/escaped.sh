#!/bin/bash
# escaped.sh: 转义符

echo; echo

echo "\v\v\v\v"      # 逐字的打印\v\v\v\v.
# 使用-e选项的'echo'命令来打印转义符.
echo "============="
echo "VERTICAL TABS"
echo -e "\v\v\v\v"   # 打印4个垂直制表符.
echo "=============="

echo "QUOTATION MARK"
echo -e "\042"       # 打印" (引号, 8进制的ASCII 码就是42).
echo "=============="

# 如果使用$'\X'结构,那-e选项就不必要了.
echo; echo "NEWLINE AND BEEP"
echo $'\n'           # 新行.
echo $'\a'           # 警告(蜂鸣).

echo "==============="
echo "QUOTATION MARKS"
# 版本2以后Bash允许使用$'\nnn'结构.
# 注意在这里, '\nnn\'是8进制的值.
echo $'\t \042 \t'   # 被水平制表符括起来的引号(").

# 当然,也可以使用16进制的值,使用$'\xhhh' 结构.
echo $'\t \x22 \t'  # 被水平制表符括起来的引号(").
# 感谢, Greg Keraunen, 指出了这点.
# 早一点的Bash版本允许'\x022'这种形式.
echo "==============="
echo


# 分配ASCII字符到变量中.
# ----------------------------------------
quote=$'\042'        # " 被赋值到变量中.
echo "$quote This is a quoted string, $quote and this lies outside the quotes."

echo

# 变量中的连续的ASCII字符.
triple_underline=$'\137\137\137'  # 137是八进制的'_'.
echo "$triple_underline UNDERLINE $triple_underline"

echo

ABC=$'\101\102\103\010'           # 101, 102, 103是八进制码的A, B, C.
echo $ABC

echo; echo

escape=$'\033'                    # 033 是八进制码的esc.
echo "\"escape\" echoes as $escape"
#                                   没有变量被输出.

echo; echo

exit 0
