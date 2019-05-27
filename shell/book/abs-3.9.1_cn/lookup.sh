#!/bin/bash
# lookup: 对指定数据文件中的每个单词都做一遍字典查询. 

file=words.data  # 指定的要搜索的数据文件. 

echo

while [ "$word" != end ]  # 数据文件中最后一个单词. 
do
  read word      # 从数据文件中读, 因为在循环的后边重定向了. 
  look $word > /dev/null  # 不想将字典文件中的行显示出来.
  lookup=$?      # 'look'命令的退出状态. 

  if [ "$lookup" -eq 0 ]
  then
    echo "\"$word\" is valid."
  else
    echo "\"$word\" is invalid."
  fi  

done <"$file"    # 将stdin重定向到$file, 所以"reads"来自于$file.

echo

exit 0

# ----------------------------------------------------------------
# 下边的代码行将不会执行, 因为上边已经有"exit"命令了.


# Stephane Chazelas建议使用下边更简洁的方法:

while read word && [[ $word != end ]]
do if look "$word" > /dev/null
   then echo "\"$word\" is valid."
   else echo "\"$word\" is invalid."
   fi
done <"$file"

exit 0
