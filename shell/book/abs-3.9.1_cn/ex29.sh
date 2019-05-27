#!/bin/bash
# 测试字符串范围.

echo; echo "Hit a key, then hit return."
read Keypress

case "$Keypress" in
  [[:lower:]]   ) echo "Lowercase letter";;
  [[:upper:]]   ) echo "Uppercase letter";;
  [0-9]         ) echo "Digit";;
  *             ) echo "Punctuation, whitespace, or other";;
esac      #  允许字符串的范围出现在[中括号]中,
          #+ 或者出现在POSIX风格的[[双中括号中.

#  在这个例子的第一个版本中,
#+ 测试大写和小写字符串的工作使用的是
#+ [a-z] 和 [A-Z].
#  这种用法在某些特定场合的或某些Linux发行版中不能够正常工作.
#  POSIX 的风格更具可移植性.
#  感谢Frank Wang指出了这点.

#  练习:
#  -----
#  就像这个脚本所表现出来的, 它只允许单次的按键, 然后就结束了.
#  修改这个脚本, 让它能够接受重复输入,
#+ 报告每次按键, 并且只有在"X"被键入时才结束. 
#  暗示: 将这些代码都用"while"循环圈起来. 

exit 0
