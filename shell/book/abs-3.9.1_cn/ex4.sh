#!/bin/bash

#  "替换", 这个脚本的用途: 
#+ 将一个文件中的某个字符串(或匹配模式), 替换为另一个字符串(或匹配模式), 
#+ 比如, "subst Smith Jones letter.txt".

ARGS=3         # 这个脚本需要3个参数. 
E_BADARGS=65   # 传递给脚本的参数个数不对. 

if [ $# -ne "$ARGS" ]
# 测试脚本的参数个数(这是个好办法). 
then
  echo "Usage: `basename $0` old-pattern new-pattern filename"
  exit $E_BADARGS
fi

old_pattern=$1
new_pattern=$2

if [ -f "$3" ]
then
    file_name=$3
else
    echo "File \"$3\" does not exist."
    exit $E_BADARGS
fi


#  下面是实现功能的代码. 

# -----------------------------------------------
sed -e "s/$old_pattern/$new_pattern/g" $file_name
# -----------------------------------------------

#  's'在sed中是替换命令, 
#+ /pattern/表示匹配模式. 
#  "g", 即全局标志, 用来自动替换掉每行中
#+ 出现的全部$old_pattern模式, 而不仅仅替换掉第一个匹配.
#  如果想深入了解, 可以参考'sed'命令的相关书籍. 

exit 0    # 成功调用脚本, 将会返回0. 
