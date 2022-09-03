#!/bin/bash
# param-sub.sh

# 一个变量是否被声明或设置，将会影响变量是否使用默认值

# 情况1：没有声明变量，直接使用
echo "username1 has not declared."
echo "Test1A: username1 = ${username1-`whoami`}" # 有输出 
echo "Test1B: username1 = ${username1:-`whoami`}" # 有输出 
echo 

# 情况2：声明了变量，但变量值为空null

username2=
echo "username2 has been declared, but is set to null."
echo "Test2A: username2 = ${username2-`whoami`}" # 无输出 
echo "Test2B: username2 = ${username2:-`whoami`}" # 有输出 
# 有输出,因为:-会比-多了一个测试条件
