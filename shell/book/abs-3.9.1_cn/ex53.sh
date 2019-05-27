#!/bin/bash
# 使用"seq"

echo

for a in `seq 80`  # or   for a in $( seq 80 )
# 与	for a in 1 2 3 4 5 ... 80   相同(少敲了好多字!).
# 也可以使用'jot'(如果系统上有的话). 
do
  echo -n "$a "
done      # 1 2 3 4 5 ... 80
# 这也是一个通过使用命令输出
# 来产生"for"循环中[list]列表的例子. 

echo; echo


COUNT=80  # 当然, 'seq'也可以使用一个可替换的参数.

for a in `seq $COUNT`  # 或者   for a in $( seq $COUNT )
do
  echo -n "$a "
done      # 1 2 3 4 5 ... 80

echo; echo

BEGIN=75
END=80

for a in `seq $BEGIN $END`
#  传给"seq"两个参数, 从第一个参数开始增长,
#+ 一直增长到第二个参数为止. 
do
  echo -n "$a "
done      # 75 76 77 78 79 80

echo; echo

BEGIN=45
INTERVAL=5
END=80

for a in `seq $BEGIN $INTERVAL $END`
#  传给"seq"三个参数, 从第一个参数开始增长, 
#+ 并以第二个参数作为增量, 
#+ 一直增长到第三个参数为止. 
do
  echo -n "$a "
done      # 45 50 55 60 65 70 75 80

echo; echo

exit 0
