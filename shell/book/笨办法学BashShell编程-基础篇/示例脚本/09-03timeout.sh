#!/bin/bash
# 通过stty来实现限时输入

INTERVAL=3

timedout_read() {
  timeout=$1
  varname=$2
  old_tty_setting=`stty -g` 		# 保存当前配置
  stty -icanon min 0 time ${timeout}0 	# 注意time后面是十分之一秒
  eval read $varname
  stty "$old_tty_setting"		# 恢复原有配置
}

echo -n "What's your name? Quick! "
timedout_read $INTERVAL your_name

echo 
if [ ! -z "$your_name" ]; then
  echo "Your name is $your_name."
else
  echo "Timed out."
fi 

exit 0 
