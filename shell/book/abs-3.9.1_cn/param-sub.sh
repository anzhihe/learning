#!/bin/bash
# param-sub.sh

#  一个变量是否被声明或设置,
#+ 将会影响这个变量是否使用默认值, 
#+ 即使这个变量值为空(null).

username0=
echo "username0 has been declared, but is set to null."
echo "username0 = ${username0-`whoami`}"
# 不会有输出.

echo

echo username1 has not been declared.
echo "username1 = ${username1-`whoami`}"
# 将会输出默认值.

username2=
echo "username2 has been declared, but is set to null."
echo "username2 = ${username2:-`whoami`}"
#                            ^
# 会输出, 因为:-会比-多一个条件测试.
# 可以与上边的例子比较一下.


#

# 再来一个:

variable=
# 变量已经被声明, 但是设为空值. 

echo "${variable-0}"    # (没有输出)
echo "${variable:-1}"   # 1
#               ^

unset variable

echo "${variable-2}"    # 2
echo "${variable:-3}"   # 3

exit 0
