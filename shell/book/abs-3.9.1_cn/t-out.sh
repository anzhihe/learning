#!/bin/bash
# t-out.sh
# 从"syngin seven"的建议中得到的灵感 (感谢).


TIMELIMIT=4         # 4秒

read -t $TIMELIMIT variable <&1
#                           ^^^
#  在这个例子中, 对于Bash 1.x和2.x就需要"<&1"了,
#  但是Bash 3.x就不需要.

echo

if [ -z "$variable" ]  # 值为null?
then
  echo "Timed out, variable still unset."
else  
  echo "variable = $variable"
fi  

exit 0
