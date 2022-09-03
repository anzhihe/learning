#!/bin/bash

# 使用set命令来改变位置参数
# 测试时，需要给这个脚本传递三个参数如 1 2 3

# 显示传递给脚本的三个参数
echo
echo "Command-line argumnet #1 = $1"
echo "Command-line argumnet #2 = $2"
echo "Command-line argumnet #3 = $3"

# 使用set修改位置参数
# 将uname -a的结果，替换原有的参数
set `uname -a`

# 显示修改后的参数的值
echo 
echo "==============================="
echo "Filed #1 of 'uname -a' = $1"
echo "Filed #2 of 'uname -a' = $2"
echo "Filed #3 of 'uname -a' = $3"

exit 0 
