#!/bin/bash
# timeout.sh

#  由Stephane Chazelas所编写,
#+ 本书作者做了一些修改.

INTERVAL=5                # 超时间隔

timedout_read() {
  timeout=$1
  varname=$2
  old_tty_settings=`stty -g`
  stty -icanon min 0 time ${timeout}0
  eval read $varname      # 或者仅仅读取$varname变量
  stty "$old_tty_settings"
  # 参考"stty"的man页.
}

echo; echo -n "What's your name? Quick! "
timedout_read $INTERVAL your_name

#  这种方法可能并不是在每种终端类型上都可以正常使用的.
#  最大的超时时间依赖于具体的中断类型.
#+ (通常是25.5秒).

echo

if [ ! -z "$your_name" ]  # 如果在超时之前名字被键入...
then
  echo "Your name is $your_name."
else
  echo "Timed out."
fi

echo

# 这个脚本的行为可能与脚本"timed-input.sh"的行为有些不同.
# 每次按键, 计时器都会重置(译者注: 就是从0开始).

exit 0
