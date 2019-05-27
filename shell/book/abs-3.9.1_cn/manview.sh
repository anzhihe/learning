#!/bin/bash
# manview.sh: 将man页源文件格式化以方便查看. 

#  当你想阅读man页的时候, 这个脚本就有用了. 
#  它允许你在运行的时候查看
#+ 中间结果. 

E_WRONGARGS=65

if [ -z "$1" ]
then
  echo "Usage: `basename $0` filename"
  exit $E_WRONGARGS
fi

# ---------------------------
groff -Tascii -man $1 | less
# 来自于groff的man页.
# ---------------------------

#  如果man页中包括表或者等式,
#+ 那么上边的代码就够呛了.
#  下边的这行代码可以解决上边的这个问题.
#
#   gtbl < "$1" | geqn -Tlatin1 | groff -Tlatin1 -mtty-char -man
#
#   感谢, S.C.

exit 0
