#!/bin/bash
# 03-02rpm-check-v2.sh

# 获得一个rpm文件的描述、文件列表，将检查是否已经安装
# 并将结果保存到一个文件中
# 此脚本通过一个代码块来实现 

SUCCESS=0
E_NOARGS=65
E_NOFILE=66

# 判断是否给此脚本传递参数
if [ -z "$1" ]
then
  echo "Usage: `basename $0` rpm-file"
  exit $E_NOARGS
fi

# 判断文件是否存在
if [ ! -f "$1" ]
then
  echo "$1 not exist!"
  exit $E_NOFILE
fi

{
  echo 
  echo "Archive Description:"
  rpm -qpi $1  # rpm文件的描述 
  echo 
  echo "Archive Listing:"
  rpm -qpl $1  # rpm中文件的列表
  echo
  rpm -i --test $1 # 检查rpm包是否可以安装
  if [ "$?" -eq $SUCCESS ]
  then
    echo "$1 can be installed."
  else
    echo "$1 cannot be installed."
  fi
  echo 
} > "$1.test"  # 将代码块的所有输出重定向到文件中

echo "Results of rpm test in file $1.test"

exit 0
