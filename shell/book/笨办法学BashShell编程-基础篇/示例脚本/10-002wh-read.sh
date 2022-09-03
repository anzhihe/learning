#!/bin/bash
# while 与 read 结合处理文件

# 方法1
cat /etc/hosts |
while read line1
do 
  echo "$line1"
done

# 方法2
echo "============================"

while read line2
do
  echo "$line2"
done < /etc/hosts

exit 0
