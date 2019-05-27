#!/bin/bash

dir1=/usr/local
dir2=/var/spool

pushd $dir1
# 将自动运行一个 'dirs' (把目录栈的内容列到stdout上).
echo "Now in directory `pwd`." # 使用后置引用的 'pwd'.

# 现在对'dir1'做一些操作.
pushd $dir2
echo "Now in directory `pwd`."

# 现在对'dir2'做一些操作.
echo "The top entry in the DIRSTACK array is $DIRSTACK."
popd
echo "Now back in directory `pwd`."

# 现在, 对'dir1'做更多的操作.
popd
echo "Now back in original working directory `pwd`."

exit 0

# 如果你不使用 'popd' 将会发生什么 -- 然后退出这个脚本?
# 你最后将落在哪个目录中? 为什么?
