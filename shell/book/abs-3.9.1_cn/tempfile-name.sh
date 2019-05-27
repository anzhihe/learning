#!/bin/bash
# tempfile-name.sh:  临时文件名产生器

BASE_STR=`mcookie`   # 32-字符的magic cookie. 
POS=11               # 字符串中随便的一个位置. 
LEN=5                # 取得$LEN长度连续的字符串. 

prefix=temp          #  最终的一个"临时"文件. 
                     #  如果想让这个文件更加"唯一", 
                     #+ 可以对这个前缀也采用下边的方法进行生成. 

suffix=${BASE_STR:POS:LEN}
                     # 提取从第11个字符之后的长度为5的字符串. 

temp_filename=$prefix.$suffix
                     # 构造文件名. 

echo "Temp filename = "$temp_filename""

# sh tempfile-name.sh
# Temp filename = temp.e19ea

#  与使用'date'命令(参考 ex51.sh)来创建"唯一"文件名
#+ 的方法相比较.

exit 0
