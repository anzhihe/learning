#!/bin/bash

# 从/var/log/messagesGenerates的尾部开始
# 产生当前目录下的一个lof文件.

# 注意: 如果这个脚本被一个一般用户调用的话,
# /var/log/messages 必须是全部可读的.
#         #root chmod 644 /var/log/messages

LINES=5

( date; uname -a ) >>logfile
# 时间和机器名
echo --------------------------------------------------------------------- >>logfile
tail -$LINES /var/log/messages | xargs |  fmt -s >>logfile
echo >>logfile
echo >>logfile

exit 0

#  注意:
#  -----
#  像 Frank Wang 所指出,
#+ 在原文件中的任何不匹配的引号(包括单引号和双引号)
#+ 都会给xargs造成麻烦.
#                                                                             
#  他建议使用下边的这行来替换上边的第15行:
#     tail -$LINES /var/log/messages | tr -d "\"'" | xargs | fmt -s >>logfile



#  练习:
#  -----
#  修改这个脚本, 使得这个脚本每个20分钟
#+ 就跟踪一下 /var/log/messages 的修改记录.
#  提示: 使用 "watch" 命令. 
