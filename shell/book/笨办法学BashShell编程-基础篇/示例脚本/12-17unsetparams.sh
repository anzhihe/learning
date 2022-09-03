#!/bin/bash

var1="11 22 33 44 55"

# 设置位置参数
set -- $var1

first_param=$1		# 11
second_param=$2		# 22
shift ;  shift 
remaining_param="$*"    # 33 44 55

echo "Fist parameter = $first_param"
echo "Second parameter = $second_param"
echo "Remaining parameter = $remaining_param"

# 重置所有位置参数
echo "========================="
set --

first_param=$1
second_param=$2

echo "Fist parameter = $first_param"
echo "Second parameter = $second_param"

exit 0
