#!/bin/bash
# random2.sh: 产生一个范围在 0 - 1 之间的伪随机数.
# 使用了awk的rand()函数.

AWKSCRIPT=' { srand(); print rand() } '
#            Command(s) / 传递到awk中的参数
# 注意, srand()是awk中用来产生伪随机数种子的函数.


echo -n "Random number between 0 and 1 = "

echo | awk "$AWKSCRIPT"
# 如果你省去'echo', 会怎样?

exit 0


# 练习:
# -----

# 1) 使用循环结构, 打印出10个不同的随机数.
#      (提示: 在每次循环过程中, 你必须使用"srand()"函数来生成不同的种子,
#+     如果你不这么做会怎样?)

# 2) 使用整数乘法作为一个比例因子, 在10到100的范围之间,
#+   来产生随机数.

# 3) 同上边的练习#2, 但是这次产生随机整数.
