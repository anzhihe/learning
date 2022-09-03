#!/bin/bash

echo "Line0: Why doesn't this string \n split on two line?"
echo -e "Line1: Why doesn't this string \n split on two line?"

# 测试1：有新行
echo
echo "---Test1---"
echo $"A line of text containing
a linefeed."

# 测试2：有新行
echo
echo "---Test2---"
echo "This string splits
on two lines."

# 测试3：-n也不能阻止换行
echo
echo "---Test3---"
echo -n "Another line of text containing
a linefeed"

# 测试4：分配给了变量，所以还是一行
echo
echo "---Test4---"
string1=$"Yet another line of text containing
a linefeed (maybe)."
echo $string1

exit 0
