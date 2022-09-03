#!/bin/bash

# 实验1：生成10个随机整数
MAXCOUNT=10
count=1

echo "#MAXCOUNT radmom number:"
while [ "$count" -le $MAXCOUNT ]
do 
  echo $RANDOM
  let "count += 1"
done 

# 实验2：通过模操作，获得0-500之间的随机整数
RANGE=500
echo
number=$RANDOM
let "number %=RANGE"
echo "Random number less than $RANGE -- $number"

# 实验3：需要生成一个大于某个值的随机整数
FLOOR=200
number=0
while [ "$number" -le $FLOOR ]
do
  number=$RANDOM
done 
echo "Random number greater than $FLOOR -- $number"

# 实验4：对实验3改进一下，不通过循环来生成，这样效率高一些
FLOOR=200
let "number = $RANDOM + $FLOOR"
echo "Random number greater than $FLOOR -- $number"

# 实验5：结合前面的示例，获得指定上下限之间的随机整数
FLOOR=200
RANGE=500
number=0
while [ "$number" -le $FLOOR ]
do
  number=$RANDOM
  let "number %=RANGE"
done
echo "Random number between $FLOOR AND $RANGE -- $number"

# 实验6：生成true和false两个二元的值
BINARY=2
T=1
number=$RANDOM
let "number %= $BINARY"
if [ "$number" -eq $T ]; then
  echo "TRUE"
else
  echo "FALSE"
fi

# 实验7：掷两个骰子的游戏
SPOTS=6
die1=0
die2=0
let "die1 = $RANDOM % SPOTS +1"
let "die2 = $RANDOM % SPOTS +1"
let "throw = $die1 + $die2"
echo "Throw of the dice ($die1, $die2) = $throw"
exit 0 
