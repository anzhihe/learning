#!/bin/bash

variable="one two three four five"

set -- $variable
# 将位置参数的内容设为变量"$variable"的内容.

first_param=$1
second_param=$2
shift; shift        # 将最前面的两个位置参数移除.
remaining_params="$*"

echo
echo "first parameter = $first_param"             # one
echo "second parameter = $second_param"           # two
echo "remaining parameters = $remaining_params"   # three four five

echo; echo

# 再来一次.
set -- $variable
first_param=$1
second_param=$2
echo "first parameter = $first_param"             # one
echo "second parameter = $second_param"           # two

# ======================================================

set --
# 如果没指定变量,那么将会unset所有的位置参数.

first_param=$1
second_param=$2
echo "first parameter = $first_param"             # (null value)
echo "second parameter = $second_param"           # (null value)

exit 0
