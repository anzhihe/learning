#!/bin/bash
# keypress.sh: 检测用户按键("hot keys").

echo

old_tty_settings=$(stty -g)   # 保存老的设置(为什么?). 
stty -icanon
Keypress=$(head -c1)          # 或者使用$(dd bs=1 count=1 2> /dev/null)
                              # 在非GNU系统上

echo
echo "Key pressed was \""$Keypress"\"."
echo

stty "$old_tty_settings"      # 恢复老的设置. 

# 感谢, Stephane Chazelas.

exit 0
