#!/bin/bash
# patt-matching.sh

# 使用# ## % %%来进行参数替换操作的模式匹配. parameter substitution operators.

var1=abcd12345abc6789
pattern1=a*c  # *(通配符)匹配a - c之间的任意字符.

echo
echo "var1 = $var1"           # abcd12345abc6789
echo "var1 = ${var1}"         # abcd12345abc6789
                              # (另一种形式)
echo "Number of characters in ${var1} = ${#var1}"
echo

echo "pattern1 = $pattern1"   # a*c  (匹配'a'到'c'之间的任意字符)
echo "--------------"
echo '${var1#$pattern1}  =' "${var1#$pattern1}"    #         d12345abc6789
# 最短的可能匹配, 去掉abcd12345abc6789的前3个字符.
#                     |-|               ^^^^^
echo '${var1##$pattern1} =' "${var1##$pattern1}"   #                  6789
# 最长的可能匹配, 去掉abcd12345abc6789的前12个字符
#                     |----------|      ^^^^^^

echo; echo; echo

pattern2=b*9            # 匹配'b'到'9'之间的任意字符
echo "var1 = $var1"     # 还是abcd12345abc6789
echo
echo "pattern2 = $pattern2"
echo "--------------"
echo '${var1%pattern2}  =' "${var1%$pattern2}"     #     abcd12345a
# 最短的可能匹配, 去掉abcd12345abc6789的最后6个字符
#                               |----|  ^^^^^^^
echo '${var1%%pattern2} =' "${var1%%$pattern2}"    #     a
# 最长的可能匹配, 去掉abcd12345abc6789的最后12个字符
#                      |-------------|  ^^^^^^^^

# 牢记, #和##是从字符串左边开始, 并且去掉左边的字符串, 
#       %和%%从字符串的右边开始, 并且去掉右边的字符串. 
# (译者注: 有个好记的方法, 那就是察看键盘顺序, 记住#在%的左边. ^_^)
echo

exit 0
