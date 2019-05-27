#!/bin/bash
# $IFS 处理空白与处理其他字符不同. 

output_args_one_per_line()
{
  for arg
  do echo "[$arg]"
  done
}

echo; echo "IFS=\" \""
echo "-------"

IFS=" "
var=" a  b c   "
output_args_one_per_line $var  # output_args_one_per_line `echo " a  b c   "`
#
# [a]
# [b]
# [c]


echo; echo "IFS=:"
echo "-----"

IFS=:
var=":a::b:c:::"               # 与上边一样, 但是用" "替换了":".
output_args_one_per_line $var
#
# []
# [a]
# []
# [b]
# [c]
# []
# []
# []

# 同样的事情也会发生在awk的"FS"域中.

# 感谢, Stephane Chazelas.

echo

exit 0
