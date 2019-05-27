#!/bin/bash
# weirdvars.sh: echo出一些诡异变量.

var="'(]\\{}\$\""
echo $var        # '(]\{}$"
echo "$var"      # '(]\{}$"     和上一句没什么区别.Doesn't make a difference.

echo

IFS='\'
echo $var        # '(] {}$"     \ 字符被空白符替换了, 为什么?
echo "$var"      # '(]\{}$"

# 这个例子由Stephane Chazelas提供.

exit 0
