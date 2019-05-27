#!/bin/bash
# zmore

#使用'more'来查看gzip文件

NOARGS=65
NOTFOUND=66
NOTGZIP=67

if [ $# -eq 0 ] # 与if [ -z "$1" ]效果相同
# (译者注: 上边这句注释有问题), $1是可以存在的, 可以为空, 如:  zmore "" arg2 arg3
then
  echo "Usage: `basename $0` filename" >&2
  # 错误消息输出到stderr.
  exit $NOARGS
  # 返回65作为脚本的退出状态的值(错误码).
fi  

filename=$1

if [ ! -f "$filename" ]   # 将$filename引用起来, 这样允许其中包含空白字符. 
then
  echo "File $filename not found!" >&2
  # 错误消息输出到stderr.
  exit $NOTFOUND
fi  

if [ ${filename##*.} != "gz" ]
# 在变量替换中使用中括号结构.
then
  echo "File $1 is not a gzipped file!"
  exit $NOTGZIP
fi  

zcat $1 | more

# 使用过滤命令'more.'
# 当然, 如果你愿意, 也可以使用'less'.


exit $?   # 脚本将把管道的退出状态作为返回值.
# 事实上, 也不一定非要加上"exit $?", 因为在任何情况下,
# 脚本都会将最后一条命令的退出状态作为返回值.
