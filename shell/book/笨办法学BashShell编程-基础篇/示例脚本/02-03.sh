#!/bin/bash
# 清除 v3

# 说明：这个脚本有好多新的特性，现在先有一个初步的印象
#       以后再详细说


LOG_DIR=/var/log
ROOT_UID=0	# $UID为0时，用户都有root的权限
LINES=50	# 默认的保存的行数
E_XCD=66	# 退出代码：表示不能修改目录位置
E_NOROOT=67	# 退出代码：表示不是root用户


# 当然要以root身份来运行这个脚本
if [ "$UID" -ne "$ROOT_UID" ]
then
  echo "Must be root to run this script."
  exit $E_NOROOT
fi 

# 测试是否给这个脚本传递有参数（非空）
if [ -n "$1" ]
then
  lines=$1
else
  lines=$LINES	# 如果没有在命令指定，就使用默认值
fi

cd $LOG_DIR

# 在处理log file之前，应当确定当前目录是否正确
# 如果不在/var/log目录中
if [ `pwd` != "$LOG_DIR" ] # 或 if [ "$PWD" != "$LOG_DIR"]
then
  echo "Can't change $LOG_DIR."
  exit $E_XCD
fi 

# 保留mssage文件中的最后部分，而不是全部清除
tail -$lines messages > mesg.tmp 
mv mesg.tmp messages

# 旧的办法，不再需要了。新的办法更加安全吗？
# cat /dev/null > messages

cat /dev/null > wtmp

echo "Logs cleaned up."

exit 0
# 退出时返回0，0表示成功
