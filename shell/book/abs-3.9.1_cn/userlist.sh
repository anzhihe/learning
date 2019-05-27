#!/bin/bash
# userlist.sh

PASSWORD_FILE=/etc/passwd
n=1           # User number

for name in $(awk 'BEGIN{FS=":"}{print $1}' < "$PASSWORD_FILE" )
# 域分隔 = :             ^^^^^^
# 打印出第一个域                 ^^^^^^^^
# 从password文件中取得输入                     ^^^^^^^^^^^^^^^^^
do
  echo "USER #$n = $name"
  let "n += 1"
done  


# USER #1 = root
# USER #2 = bin
# USER #3 = daemon
# ...
# USER #30 = bozo

exit 0

#  练习:
#  -----
#  一个普通用户(或者是一个普通用户运行的脚本)
#+ 怎么才能够读取/etc/passwd呢?
#  这是否是一个安全漏洞? 为什么是?为什么不是?
