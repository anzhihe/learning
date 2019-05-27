#!/bin/bash
# arrow-detect.sh: 检测方向键, 和一些非打印字符的按键.
# 感谢, Sandro Magi, 告诉了我们怎么做到这点.

# --------------------------------------------
# 按键所产生的字符编码.
arrowup='\[A'
arrowdown='\[B'
arrowrt='\[C'
arrowleft='\[D'
insert='\[2'
delete='\[3'
# --------------------------------------------

SUCCESS=0
OTHER=65

echo -n "Press a key...  "
# 如果不是上边列表所列出的按键, 可能还是需要按回车. (译者注: 因为一般按键是一个字符)
read -n3 key                      # 读取3个字符.

echo -n "$key" | grep "$arrowup"  # 检查输入字符是否匹配.
if [ "$?" -eq $SUCCESS ]
then
  echo "Up-arrow key pressed."
  exit $SUCCESS
fi

echo -n "$key" | grep "$arrowdown"
if [ "$?" -eq $SUCCESS ]
then
  echo "Down-arrow key pressed."
  exit $SUCCESS
fi

echo -n "$key" | grep "$arrowrt"
if [ "$?" -eq $SUCCESS ]
then
  echo "Right-arrow key pressed."
  exit $SUCCESS
fi

echo -n "$key" | grep "$arrowleft"
if [ "$?" -eq $SUCCESS ]
then
  echo "Left-arrow key pressed."
  exit $SUCCESS
fi

echo -n "$key" | grep "$insert"
if [ "$?" -eq $SUCCESS ]
then
  echo "\"Insert\" key pressed."
  exit $SUCCESS
fi

echo -n "$key" | grep "$delete"
if [ "$?" -eq $SUCCESS ]
then
  echo "\"Delete\" key pressed."
  exit $SUCCESS
fi


echo " Some other key pressed."

exit $OTHER

#  练习:
#  -----
#  1) 使用'case'结构来代替'if'结构, 
#+    这样可以简化这个脚本.
#  2) 添加 "Home", "End", "PgUp", 和 "PgDn" 这些按键的检查.
