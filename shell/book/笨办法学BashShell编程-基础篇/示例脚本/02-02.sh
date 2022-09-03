#!/bin/bash
# 一个Bash脚本正确的开头部分

# 清除 v2
# 当然要以root身份来运行这个脚本
# 以后，在这个地方增加一个逻辑：
#   如果不是root用户执行本脚本，会自定义的错误提示，然后退出

# 如果使用变量，这样更加灵活、优雅
LOG_DIR=/var/log

cd $LOG_DIR

cat /dev/null > message
cat /dev/null > wtmp

echo "Logs cleaned up."

exit  # 这个命令是一种正确、合适的退出的办法。
      # 不带任何参数的exit，将返回退出的状态码
