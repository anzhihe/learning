#!/bin/bash
# 通过$*和$@列出所有的参数

# 需要传递给本脚本多个参数，以方便测试

E_BADARGS=65

if [ ! -n "$1" ] ; then
  echo "Usage: `basename $0` argument1 argument2 etc."
  exit $E_BADARGS
fi

# 测试1，使用$*。所有的参数看一个单词
echo "$*"
echo "=== List args with \"\$*\":"
index=1

for arg in "$*"
do 
  echo "Arg #$index = $arg"
  let "index+=1"
done

echo 

# 测试2，使用$@。把每个参数看成单独的单词
echo "$@"
echo "=== List args with \"\$@\":"
index=1

for arg in "$@"
do 
  echo "Arg #$index = $arg"
  let "index+=1"
done

exit 0 
