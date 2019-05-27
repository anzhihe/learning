#!/bin/bash

# 所有在/usr/X11R6/bin中的神秘2进制文件都是些什么东西?

DIRECTORY="/usr/X11R6/bin"
# 也试试 "/bin", "/usr/bin", "/usr/local/bin", 等等.

for file in $DIRECTORY/*
do
  whatis `basename $file`   # 将会echo出这个2进制文件的信息.
done

exit 0

# 你可能希望将这个脚本的输出重定向, 像这样:
# ./what.sh >>whatis.db
# 或者一页一页的在stdout上察看,
# ./what.sh | less
