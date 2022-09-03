#!/bin/bash
# 使用more来查看gzip文件

# 定义错误退出代码
NOARGS=65
NOTFOUND=66
NOTGZIP=67

# 判断是否传递参数
if [ $# -eq 0 ] 
then
  echo "Usage: `basename $0` filename " >&2
  exit $NOARGS
fi

filename=$1
if [ ! -f "$filename" ]
then
  echo "File $filename no found !" >&2
  exit $NOTFOUND
fi

# 检查文件“扩展名”
# 其实，这不是最佳的判断是否是zip格式的方法
if [ ${filename##*.} != "gz" ]
then
  echo "File $1 is not a gzipped file !"
  exit $NOTZIP
fi

zcat $1 | more
exit 0
