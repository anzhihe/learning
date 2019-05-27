#!/bin/bash

#  delete.sh, 不是很聪明的文件删除方法. 
#  Usage: delete filename

E_BADARGS=65

if [ -z "$1" ]
then
  echo "Usage: `basename $0` filename"
  exit $E_BADARGS  # 没有参数? 退出脚本. 
else  
  file=$1          # 设置文件名.
fi  


[ ! -f "$file" ] && echo "File \"$file\" not found. \
Cowardly refusing to delete a nonexistent file."
# 与列表, 在文件不存在时将会给出错误信息. 
# 注意echo命令使用了一个续行符, 这样下一行的内容, 也会作为echo命令的参数. 

[ ! -f "$file" ] || (rm -f $file; echo "File \"$file\" deleted.")
# 或列表, 如果文件存在, 那就删除此文件. 

# 注意, 上边的两个逻辑相反. 
# 与列表在true的情况下才执行, 或列表在false的时候才执行. 

exit 0
