#!/bin/bash
# length.sh

E_NO_ARGS=65

if [ $# -eq 0 ]  # 这个演示脚本必须有命令行参数.
then
  echo "Please invoke this script with one or more command-line arguments."
  exit $E_NO_ARGS
fi  

var01=abcdEFGH28ij
echo "var01 = ${var01}"
echo "Length of var01 = ${#var01}"
# 现在, 让我们试试在变量中嵌入一个空格.
var02="abcd EFGH28ij"
echo "var02 = ${var02}"
echo "Length of var02 = ${#var02}"

echo "Number of command-line arguments passed to script = ${#@}"
echo "Number of command-line arguments passed to script = ${#*}"

exit 0
