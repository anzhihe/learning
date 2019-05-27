#!/bin/bash

ROOT_UID=0   # 只有$UID为0的用户才拥有root权限.
E_NOTROOT=65
E_NOPARAMS=66

if [ "$UID" -ne "$ROOT_UID" ]
then
  echo "Must be root to run this script."
  # "Run along kid, it's past your bedtime."
  exit $E_NOTROOT
fi  

if [ -z "$1" ]
then
  echo "Usage: `basename $0` find-string"
  exit $E_NOPARAMS
fi


echo "Updating 'locate' database..."
echo "This may take a while."
updatedb /usr &     # 必须使用root身份来运行.

wait
# 将不会继续向下运行, 除非'updatedb'命令执行完成.
# 你希望在查找文件名之前更新database.

locate $1

#  如果没有'wait'命令的话, 而且在比较糟的情况下,
#+ 脚本可能在'updatedb'命令还在运行的时候退出,
#+ 这将会导致'updatedb'成为一个孤儿进程.

exit 0
