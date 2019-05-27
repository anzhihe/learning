#!/bin/bash

echo

let a=11            # 与 'a=11' 相同
let a=a+5           # 等价于 let "a = a + 5"
                    # (双引号和空格是这句话更具可读性.)
echo "11 + 5 = $a"  # 16

let "a <<= 3"       # 等价于 let "a = a << 3"
echo "\"\$a\" (=16) left-shifted 3 places = $a"
                    # 128

let "a /= 4"        # 等价于 let "a = a / 4"
echo "128 / 4 = $a" # 32

let "a -= 5"        # 等价于 let "a = a - 5"
echo "32 - 5 = $a"  # 27

let "a *=  10"      # 等价于 let "a = a * 10"
echo "27 * 10 = $a" # 270

let "a %= 8"        # 等价于 let "a = a % 8"
echo "270 modulo 8 = $a  (270 / 8 = 33, remainder $a)"
                    # 6

echo

exit 0
