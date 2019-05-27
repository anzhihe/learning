#!/bin/bash
# pick-card.sh

# 这是一个从数组中取出随机元素的一个例子.


# 抽取一张牌, 任何一张.

Suites="Clubs
Diamonds
Hearts
Spades"

Denominations="2
3
4
5
6
7
8
9
10
Jack
Queen
King
Ace"

# 注意变量的多行展开.


suite=($Suites)                # 读入一个数组.
denomination=($Denominations)

num_suites=${#suite[*]}        # 计算有多少个数组元素.
num_denominations=${#denomination[*]}

echo -n "${denomination[$((RANDOM%num_denominations))]} of "
echo ${suite[$((RANDOM%num_suites))]}


# $bozo sh pick-cards.sh
# Jack of Clubs


# 感谢, "jipe," 指出$RANDOM的这个用法.
exit 0
