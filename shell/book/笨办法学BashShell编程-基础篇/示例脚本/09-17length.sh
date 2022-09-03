#!/bin/bash
# 变量的长度

E_NO_ARGS=65

if [ $# -eq 0 ] ; then
  echo "Please invoke this script with one or nore commnad-lin arguments."
fi

var01=abc123
echo "var01 = ${var01}"
echo "Length of var01 = ${#var01}"

var02="abc123 ABC"
echo "var02 = ${var02}"
echo "Length of var02 = ${#var02}"

echo "Number of command-line arguments passwd to script = ${#@}"
echo "Number of command-line arguments passwd to script = ${#*}"

exit 0 
