#!/bin/bash
#  cvt.sh:
#  将一个目录下的所有MacPaint格式的图片文件都转换为"pbm"各式的图片文件. 

#  使用"netpbm"包中的"macptopbm"程序进行转换, 
#+ 这个程序主要是由Brian Henderson(bryanh@giraffe-data.com)来维护的.
#  Netpbm绝大多数Linux发行版的标准套件. 

OPERATION=macptopbm
SUFFIX=pbm          # 新的文件名后缀.

if [ -n "$1" ]
then
  directory=$1      # 如果目录名作为参数传递给脚本...
else
  directory=$PWD    # 否则使用当前的工作目录.
fi  
  
#  假定目标目录中的所有文件都是MacPaint格式的图像文件, 
#+ 并且都是以".mac"作为文件名后缀. 

for file in $directory/*    # 文件名匹配(filename globbing).
do
  filename=${file%.*c}      #  去掉文件名的".mac"后缀
                            #+ ('.*c' 将会匹配
			    #+ '.'和'c'之间任意字符串).
  $OPERATION $file > "$filename.$SUFFIX"
                            # 把结果重定向到新的文件中.
  rm -f $file               # 转换后删除原始文件.
  echo "$filename.$SUFFIX"  # 从stdout输出转换后文件的文件名.
done

exit 0

# 练习:
# -----
#  就像它现在的样子, 这个脚本把当前
#+ 目录下的所有文件都转换了.
#  修改这个脚本, 让它只转换以".mac"为后缀名的文件.
