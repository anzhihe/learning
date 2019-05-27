#!/bin/bash
# bin-grep.sh: 在一个二进制文件中定位匹配字串.

# 对于二进制文件的"grep"替换. 
# 与"grep -a"的效果相似

E_BADARGS=65
E_NOFILE=66

if [ $# -ne 2 ]
then
  echo "Usage: `basename $0` search_string filename"
  exit $E_BADARGS
fi

if [ ! -f "$2" ]
then
  echo "File \"$2\" does not exist."
  exit $E_NOFILE
fi  


IFS=$'\012'       # 由Paulo Marcel Coelho Aragao提出的建议.
                  # 也就是:  IFS="\n"
for word in $( strings "$2" | grep "$1" )
# "strings" 命令列出二进制文件中的所有字符串.
# 输出到管道交给"grep",然后由grep命令来过滤字符串.
do
  echo $word
done

# S.C. 指出, 行23 - 29 可以被下边的这行来代替,
#    strings "$2" | grep "$1" | tr -s "$IFS" '[\n*]'


# 试试用"./bin-grep.sh mem /bin/ls"来运行这个脚本.

exit 0
