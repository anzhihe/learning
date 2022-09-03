#!/bin/bash
# 采用read的选项实现限时输入

TIMELIMIT=3

read -t $TIMELIMIT var1

echo

if [ -z "$var1" ]; then
  echo "Timed out, var1 still unset."
else
  echo "var1 = $var1"
fi

exit 0 
