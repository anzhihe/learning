#!/bin/bash
# rfe.sh: 修改文件扩展名.
#
# 用法:		rfe old_extension new_extension
#
# 示例:
# 将指定目录中所有的*.gif文件都重命名为*.jpg,
# 用法:		rfe gif jpg


E_BADARGS=65

case $# in
  0|1)             # 竖线"|"在这里表示"或"操作.
  echo "Usage: `basename $0` old_file_suffix new_file_suffix"
  exit $E_BADARGS  # 如果只有0个或1个参数的话, 那么就退出脚本.
  ;;
esac


for filename in *.$1
# 以第一个参数为扩展名的全部文件的列表.
do
  mv $filename ${filename%$1}$2
  #  把筛选出来的文件的扩展名去掉, 因为筛选出来的文件的扩展名都是第一个参数,
  #+ 然后把第2个参数作为扩展名, 附加到这些文件的后边.
done

exit 0
