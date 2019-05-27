#!/bin/bash
# Faxing (前提是'fax'必须已经安装好).

EXPECTED_ARGS=2
E_BADARGS=65

if [ $# -ne $EXPECTED_ARGS ]
# 检查命令行参数的个数是否正确.
then
   echo "Usage: `basename $0` phone# text-file"
   exit $E_BADARGS
fi


if [ ! -f "$2" ]
then
  echo "File $2 is not a text file"
  exit $E_BADARGS
fi
  

fax make $2              # 从纯文本文件中创建传真格式的文件.

for file in $(ls $2.0*)  # 连接转换过的文件.
                         # 在变量列表中使用通配符.
do
  fil="$fil $file"
done  

efax -d /dev/ttyS3 -o1 -t "T$1" $fil   # 干活的地方.


# S.C. 指出, 通过下边的命令可以省去for循环.
#    efax -d /dev/ttyS3 -o1 -t "T$1" $2.0*
# 但这并不十分具有讲解意义[嘿嘿].

exit 0
