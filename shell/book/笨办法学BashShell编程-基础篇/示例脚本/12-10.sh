#!/bin/bash
# 说明：这是一个练习date的脚本

echo "The number of days since the year's beginning is `date +%j`."
# +%j 用来给出今天是本年度的第几天
# 注意不要少了+号

echo "The number of seconds elapsed since 1970/07/01 is `date +%s`."
# +%s 将输出从UNIX元年到现在为止的秒数

PREFIX=temp
SUFFIX=$(date +%s)
FILENAME=$PREFIX.$SUFFIX

echo $FILENAME
# 这是一种常用的非常好的办法来生成“唯一”临时文件的方法
# 拍砖：但是，如果在一秒内需要有多个临时文件呢？
# 但是，总是要比用$$要一些

exit 0
