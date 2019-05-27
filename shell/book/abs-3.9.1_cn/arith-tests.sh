#!/bin/bash
# 算术测试.

# (( ... ))结构可以用来计算并测试算术表达式的结果. 
# 退出状态将会与[ ... ]结构完全相反!

(( 0 ))
echo "Exit status of \"(( 0 ))\" is $?."         # 1

(( 1 ))
echo "Exit status of \"(( 1 ))\" is $?."         # 0

(( 5 > 4 ))                                      # 真
echo "Exit status of \"(( 5 > 4 ))\" is $?."     # 0

(( 5 > 9 ))                                      # 假
echo "Exit status of \"(( 5 > 9 ))\" is $?."     # 1

(( 5 - 5 ))                                      # 0
echo "Exit status of \"(( 5 - 5 ))\" is $?."     # 1

(( 5 / 4 ))                                      # 除法也可以.
echo "Exit status of \"(( 5 / 4 ))\" is $?."     # 0

(( 1 / 2 ))                                      # 除法的计算结果 < 1.
echo "Exit status of \"(( 1 / 2 ))\" is $?."     # 截取之后的结果为 0.
                                                 # 1

(( 1 / 0 )) 2>/dev/null                          # 除数为0, 非法计算. 
#           ^^^^^^^^^^^
echo "Exit status of \"(( 1 / 0 ))\" is $?."     # 1

# "2>/dev/null"起了什么作用?
# 如果这句被删除会怎样?
# 尝试删除这句, 然后在运行这个脚本. 

exit 0
