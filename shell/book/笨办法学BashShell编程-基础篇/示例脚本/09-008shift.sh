#!/bin/bash
# 使09-008shift.sh 1 2 3 4 5 来执行这个脚本

echo "$@"	# 1 2 3 4 5

shift
echo "$@"	# 2 3 4 5

shift
echo "$@"	# 3 4 5

shift
echo "$@"	# 4 5

exit 0
