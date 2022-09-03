#!/bin/bash
# 使用参数替换和错误 信息

# ----------------------------------------------------
# 示例1：检查一些系统环境变量，这是一个预防性保护的好习惯
#        例如：如果$USER没有被设置，系统将无法识别你

: ${HOSTNAME?} ${USER?} ${HOME?} ${MAIL?}
# 向NULL命令传递四个参数。

echo 
echo "Name of the machine is $HOSTNAME."
echo "You are $USER."
echo "Your home directory is $HOME."
echo "Your mail INBOX is located in $MAIL."
echo 
echo "If you are reading this message, "
echo "critical environmental variables have been set."
echo 
echo 

# ----------------------------------------------------
# 示例2：# {variable?}结构也能检查脚本中变量的设置情况

ThisVariable=Value-of-ThisVariable
: "Value of ThisVariable is $ThisVariable".
echo
echo

: ${ZZxy23AB?"ZZxy23AB ha not been set."}
# 如果ZZxy23AB没有被设置的话，那么这个脚本会
# +打印一个错误消息，然后退出

# 你可以自己指定错误消息
# : ${variablename?"ERROR MESSAGE"}

# 上面的测试方法与下面的效果相同：
#	dummy_variable=${ZZXy23AB?}
#	dummy_variable=${ZZXy23AB?"ZXy23AB has not been set."}
#
#       echo ${ZZXy23AB?} > /dev/null

# Bash的设置值 set -u可以强制检查变量是否被设置的方法

echo "You will not sess this message, because script already terminated. "

HERE=0
exit $HERE 不会在这里退出

# 事实上，这个脚本将会返回值1作为退出状态（$echo $?)
