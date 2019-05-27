#!/bin/bash
# 从/etc/fstab中读行.

File=/etc/fstab

{
read line1
read line2
} < $File

echo "First line in $File is:"
echo "$line1"
echo
echo "Second line in $File is:"
echo "$line2"

exit 0

# 现在, 你怎么分析每行的分割域?
# 小提示: 使用awk.
