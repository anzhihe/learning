#!/bin/bash

var0=0
LIMIT=10

while [ "$var0" -lt "$LIMIT" ]
do
  echo -n "$var0 "        # -n 将会阻止产生新行. 
  #             ^           空格, 数字之间的分隔.

  var0=`expr $var0 + 1`   # var0=$(($var0+1))  也可以.
                          # var0=$((var0 + 1)) 也可以.
                          # let "var0 += 1"    也可以.
done                      # 使用其他的方法也行.

echo

exit 0
