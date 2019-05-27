#!/bin/bash

#  检查一些系统环境变量.
#  这是一种可以做一些预防性保护措施的好习惯.
#  比如, 如果$USER(用户在控制台上中的名字)没有被设置的话,
#+ 那么系统就会不认你.

: ${HOSTNAME?} ${USER?} ${HOME?} ${MAIL?}
  echo
  echo "Name of the machine is $HOSTNAME."
  echo "You are $USER."
  echo "Your home directory is $HOME."
  echo "Your mail INBOX is located in $MAIL."
  echo
  echo "If you are reading this message,"
  echo "critical environmental variables have been set."
  echo
  echo

# ------------------------------------------------------

#  ${variablename?}结构
#+ 也能够检查脚本中变量的设置情况.

ThisVariable=Value-of-ThisVariable
#  注意, 顺便提一下, 
#+ 这个字符串变量可能会被设置一些非法字符.
: ${ThisVariable?}
echo "Value of ThisVariable is $ThisVariable".
echo
echo


: ${ZZXy23AB?"ZZXy23AB has not been set."}
#  如果变量ZZXy23AB没有被设置的话, 
#+ 那么这个脚本会打印一个错误信息, 然后结束.

# 你可以自己指定错误消息.
# : ${variablename?"ERROR MESSAGE"}


# 等价于:    dummy_variable=${ZZXy23AB?}
#            dummy_variable=${ZZXy23AB?"ZXy23AB has not been set."}
#
#            echo ${ZZXy23AB?} >/dev/null

#  使用命令"set -u"来比较这些检查变量是否被设置的方法.
#



echo "You will not see this message, because script already terminated."

HERE=0
exit $HERE   # 不会在这里退出.

# 事实上, 这个脚本将会以返回值1作为退出状态(echo $?).
