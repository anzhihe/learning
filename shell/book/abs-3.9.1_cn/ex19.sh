#!/bin/bash
# 使用'shift'来逐步存取所有的位置参数. 

#  给脚本命个名, 比如shft,
#+ 然后给脚本传递一些位置参数, 比如: 
#          ./shft a b c def 23 skidoo

until [ -z "$1" ]  # 直到所有的位置参数都被存取完...
do
  echo -n "$1 "
  shift
done

echo               # 额外的换行.

exit 0
