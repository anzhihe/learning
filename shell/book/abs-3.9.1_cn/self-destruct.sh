#!/bin/bash
# self-destruct.sh

kill $$  # 脚本将在此处结束自己的进程.
         # 回忆一下,"$$"就是脚本的PID.

echo "This line will not echo."
# 而且shell将会发送一个"Terminated"消息到stdout.

exit 0

#  在脚本结束自身进程之后,
#+ 它返回的退出码是什么?
#
# sh self-destruct.sh
# echo $?
# 143
#
# 143 = 128 + 15
#             结束信号
