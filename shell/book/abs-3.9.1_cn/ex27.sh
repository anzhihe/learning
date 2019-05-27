#!/bin/bash

END_CONDITION=end

until [ "$var1" = "$END_CONDITION" ]
# 在循环的顶部进行条件判断.
do
  echo "Input variable #1 "
  echo "($END_CONDITION to exit)"
  read var1
  echo "variable #1 = $var1"
  echo
done  

exit 0
