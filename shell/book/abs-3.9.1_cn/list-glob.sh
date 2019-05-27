#!/bin/bash
# list-glob.sh: 使用"globbing", 在for循环中产生[list]

echo

for file in *
#           ^  在表达式中识别文件名匹配时,
#+             Bash将执行文件名扩展.
do
  ls -l "$file"  # 列出在$PWD(当前目录)中的所有文件.
  #  回想一下,通配符"*"能够匹配所有文件,
  #+ 然而,在"globbing"中,是不能比配"."文件的.

  #  如果没匹配到任何文件,那它将扩展成自己.
  #  为了不让这种情况发生,那就设置nullglob选项
  #+   (shopt -s nullglob).
  #  感谢, S.C.
done

echo; echo

for file in [jx]*
do
  rm -f $file    # 只删除当前目录下以"j"或"x"开头的文件.
  echo "Removed file \"$file\"".
done

echo

exit 0
