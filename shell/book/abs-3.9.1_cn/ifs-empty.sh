#!/bin/bash

#  如果$IFS被设置, 但其值为空,
#+ 那么"$*"和"$@"将不会像期望的那样显示位置参数. 

mecho ()       # 打印位置参数.
{
echo "$1,$2,$3";
}


IFS=""         # 设置了, 但值为空.
set a b c      # 位置参数.

mecho "$*"     # abc,,
mecho $*       # a,b,c

mecho $@       # a,b,c
mecho "$@"     # a,b,c

#  当$IFS值为空时, $*和$@的行为依赖于
#+ 正在运行的Bash或者sh的版本.
#  因此在脚本中使用这种"特性"是不明智的.


# 感谢, Stephane Chazelas.

exit 0
