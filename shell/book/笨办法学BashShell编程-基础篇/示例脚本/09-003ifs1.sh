#!/bin/bash
# 考察默认的IFS的值

msg="Welcome to  www	tom		tom"
# 第1个是一个空格，第2个是二个空格，第3个是一个Tab，第4个两个Tab

for item in $msg
do
  echo "[$item]"
done

exit 0

