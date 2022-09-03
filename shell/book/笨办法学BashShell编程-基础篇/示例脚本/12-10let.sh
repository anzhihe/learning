#!/bin/bash

echo
let a=11		# 与 a=11 赋值相同
let a=a+5		# 等价于 let "a = a + 5"

echo "11 + 5 = $a "	# 16

let "a-=5"		# 等价于 let "a = a - 5"

exit 0
