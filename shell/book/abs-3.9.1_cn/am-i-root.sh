#!/bin/bash
# am-i-root.sh:   我是不是root用户?

ROOT_UID=0   # Root的$UID为0.

if [ "$UID" -eq "$ROOT_UID" ]  # 只有真正的"root"才能经受得住考验?
then
  echo "You are root."
else
  echo "You are just an ordinary user (but mom loves you just the same)."
fi

exit 0


# ============================================= #
# 下边的代码不会执行, 因为脚本在上边已经退出了.

# 下边是另外一种判断root用户的方法:

ROOTUSER_NAME=root

username=`id -nu`              # 或者...   username=`whoami`
if [ "$username" = "$ROOTUSER_NAME" ]
then
  echo "Rooty, toot, toot. You are root."
else
  echo "You are just a regular fella."
fi
