#!/bin/bash
# subshell.sh

echo

echo "Subshell level OUTSIDE subshell = $BASH_SUBSHELL"
# Bash, 版本3, 添加了这个新的           $BASH_SUBSHELL 变量. 
echo

outer_variable=Outer

(
echo "Subshell level INSIDE subshell = $BASH_SUBSHELL"
inner_variable=Inner

echo "From subshell, \"inner_variable\" = $inner_variable"
echo "From subshell, \"outer\" = $outer_variable"
)

echo
echo "Subshell level OUTSIDE subshell = $BASH_SUBSHELL"
echo

if [ -z "$inner_variable" ]
then
  echo "inner_variable undefined in main body of shell"
else
  echo "inner_variable defined in main body of shell"
fi

echo "From main body of shell, \"inner_variable\" = $inner_variable"
#  $inner_variable将被作为未初始化的变量, 被显示出来, 
#+ 这是因为变量是在子shell里定义的"局部变量". 
#  还有补救的办法么? 

echo

exit 0
