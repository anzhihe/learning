#!/bin/bash

# 每次调用$RANDOM都会返回不同的随机整数. 
# 一般范围为: 0 - 32767 (有符号的16-bit整数).

MAXCOUNT=10
count=1

echo
echo "$MAXCOUNT random numbers:"
echo "-----------------"
while [ "$count" -le $MAXCOUNT ]      # 产生10 ($MAXCOUNT)个随机整数.
do
  number=$RANDOM
  echo $number
  let "count += 1"  # 增加计数.
done
echo "-----------------"

# 如果你需要在特定范围内产生随机整数, 那么使用'modulo'(模)操作.(译者注: 事实上, 这不是一个非常好的办法. 理由见man 3 rand)
# 取模操作会返回除法的余数.

RANGE=500

echo

number=$RANDOM
let "number %= $RANGE"
#           ^^
echo "Random number less than $RANGE  ---  $number"

echo



#  如果你需要产生一个大于某个下限的随机整数.
#+ 那么建立一个test循环来丢弃所有小于此下限值的整数. 

FLOOR=200

number=0   #初始化
while [ "$number" -le $FLOOR ]
do
  number=$RANDOM
done
echo "Random number greater than $FLOOR ---  $number"
echo

   # 让我们对上边的循环尝试一个小改动, 如下:
   #       let "number = $RANDOM + $FLOOR"
   # 这将不再需要那个while循环, 并且能够运行的更快.
   # 但是, 这可能会产生一个问题, 思考一下是什么问题?



# 结合上边两个例子, 来在指定的上下限之间来产生随机数.
number=0   #initialize
while [ "$number" -le $FLOOR ]
do
  number=$RANDOM
  let "number %= $RANGE"  # 让$number依比例落在$RANGE的范围内.
done
echo "Random number between $FLOOR and $RANGE ---  $number"
echo



# 产生二元值, 就是, "true" 或 "false" 两个值.
BINARY=2
T=1
number=$RANDOM

let "number %= $BINARY"
#  注意 let "number >>= 14"    将会给出一个更好的随机分配. #(译者注: 正如man页中提到的, 更高位的随机分布更加平均)
#+ (右移14位将把所有的位全部清空, 除了第15位, 因为有符号, 第16位是符号位). #取模操作使用低位来产生随机数会相对不平均)
if [ "$number" -eq $T ]
then
  echo "TRUE"
else
  echo "FALSE"
fi  

echo


# 抛骰子.
SPOTS=6   # 模6给出的范围是0 - 5.
          # 加1会得到期望的范围1 - 6.
          # 感谢, Paulo Marcel Coelho Aragao, 对此进行的简化.
die1=0
die2=0
# 是否让SPOTS=7会比加1更好呢? 解释行或者不行的原因?

# 每次抛骰子, 都会给出均等的机会.

    let "die1 = $RANDOM % $SPOTS +1" # 抛第一次.
    let "die2 = $RANDOM % $SPOTS +1" # 抛第二次.
    #  上边的算术操作中, 哪个具有更高的优先级呢 --
    #+ 模(%) 还是加法操作(+)?


let "throw = $die1 + $die2"
echo "Throw of the dice = $throw"
echo


exit 0
