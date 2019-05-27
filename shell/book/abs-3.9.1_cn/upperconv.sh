#!/bin/bash
# upperconv.sh
# 将一个指定的输入文件转换为大写. 

E_FILE_ACCESS=70
E_WRONG_ARGS=71

if [ ! -r "$1" ]     # 判断指定的输入文件是否可读? 
then
  echo "Can't read from input file!"
  echo "Usage: $0 input-file output-file"
  exit $E_FILE_ACCESS
fi                   #  即使输入文件($1)没被指定
                     #+ 也还是会以相同的错误退出(为什么?). 

if [ -z "$2" ]
then
  echo "Need to specify output file."
  echo "Usage: $0 input-file output-file"
  exit $E_WRONG_ARGS
fi


exec 4<&0
exec < $1            # 将会从输入文件中读取. 

exec 7>&1
exec > $2            # 将写到输出文件中. 
                     # 假设输出文件是可写的(添加检查?). 

# -----------------------------------------------
    cat - | tr a-z A-Z   # 转换为大写. 
#   ^^^^^                # 从stdin中读取. 
#           ^^^^^^^^^^   # 写到stdout上. 
# 然而, stdin和stdout都被重定向了. 
# -----------------------------------------------

exec 1>&7 7>&-       # 恢复stout.
exec 0<&4 4<&-       # 恢复stdin.

# 恢复之后, 下边这行代码将会如预期的一样打印到stdout上. 
echo "File \"$1\" written to \"$2\" as uppercase conversion."

exit 0
