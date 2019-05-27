#!/bin/bash
# revposparams.sh: 反转位置参数.
# 本脚本由Dan Jacobson所编写, 本书作者做了一些格式上的修正.


set a\ b c d\ e;
#     ^      ^     转义的空格
#       ^ ^        未转义的空格
OIFS=$IFS; IFS=:;
#              ^   保存旧的IFS, 然后设置新的IFS.

echo

until [ $# -eq 0 ]
do          #      步进位置参数.
  echo "### k0 = "$k""     # 步进之前
  k=$1:$k;  #      将每个位置参数都附加在循环变量的后边.
#     ^
  echo "### k = "$k""      # 步进之后
  echo
  shift;
done

set $k  #  设置一个新的位置参数.
echo -
echo $# #  察看位置参数的个数.
echo -
echo

for i   #  省略 "in list" 结构, 
        #+ 为位置参数设置变量 -- i --.
do
  echo $i  # 显示新的位置参数.
done

IFS=$OIFS  # 恢复 IFS.

#  问题:
#  是否有必要设置新的IFS, 内部域分隔符,
#+ 才能够让这个脚本正常运行? (译者注: 当然有必要.)
#  如果你没设置新的IFS, 会发生什么? 试一下.
#  并且, 在第17行, 为什么新的IFS要使用 -- 一个冒号 -- ,
#+ 来将位置参数附加到循环变量中?
#  这么做的目的是什么?

exit 0

$ ./revposparams.sh

### k0 = 
### k = a b

### k0 = a b
### k = c a b

### k0 = c a b
### k = d e c a b

-
3
-

d e
c
a b
