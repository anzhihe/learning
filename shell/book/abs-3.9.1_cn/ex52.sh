#!/bin/bash
# 在当前目录下用Uudecode解码所有用uuencode编码的文件. 

lines=35        # 允许读头部的35行(范围很宽). 

for File in *   # 测试所有$PWD下的文件. 
do
  search1=`head -$lines $File | grep begin | wc -w`
  search2=`tail -$lines $File | grep end | wc -w`
  #  用Uuencode编码过的文件在文件开始的地方都有个"begin", 
  #+ 在文件结尾的地方都有"end".
  if [ "$search1" -gt 0 ]
  then
    if [ "$search2" -gt 0 ]
    then
      echo "uudecoding - $File -"
      uudecode $File
    fi  
  fi
done  

#  小心不要让这个脚本运行自己, 
#+ 因为它也会把自身也认为是一个经过uuencode编码过的文件, 
#+ 这都是因为这个脚本自身也包含"begin"和"end". 

#  练习:
#  -----
#  修改这个脚本, 让它可以检查一个新闻组的每个文件, 
#+ 并且如果下一个没找到的话就跳过. 

exit 0
