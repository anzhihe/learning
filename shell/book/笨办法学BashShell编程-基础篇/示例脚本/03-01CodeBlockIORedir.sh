#!/bin/bash
# 大括号代码块 和 IO重定向

# 从/etc/fstab中读行

File=/etc/fstab

{
read line1
read line2
} <$File

echo "First line if $File is:"
echo "$line1"
echo 

echo "Second line if $File is:"
echo "$line2"

exit 0
