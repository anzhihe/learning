#!/bin/bash
# 把一个文件的内容全部转换为大写. 

E_BADARGS=65

if [ -z "$1" ]  # 检查命令行参数.
then
  echo "Usage: `basename $0` filename"
  exit $E_BADARGS
fi  

tr a-z A-Z <"$1"

# 与上边的作用相同, 但是使用了POSIX字符集标记方法:
#        tr '[:lower:]' '[:upper:]' <"$1"
# 感谢, S.C.

exit 0

#  练习:
#  重写这个脚本, 通过选项可以控制脚本或者
#+ 转换为大写或者转换为小写.
