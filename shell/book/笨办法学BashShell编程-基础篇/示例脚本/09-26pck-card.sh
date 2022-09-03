#!/bin/bash
# 去掉大小王，然后随机取一张。什么花色，什么点数？
# 采用从数组中取得随机元素的方法

Suites="Clubs
Diamonds
Hearts
Spaders"

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

suite=($Suites)			# 保存到新数组中
denomination=($Denominations)

num_suites=${#suite[*]}		# 获得数组中的元素的个数
num_denominations=${#denomination[*]}

# echo $num_suites		# 4
# echo $num_denominations	# 13 
# echo ${suite[0]}		# Clubs
# echo ${denomination[0]}	# 2

i=$RANDOM%num_denominations
j=$RANDOM%num_suites

echo "${denomination[$i]} of ${suite[$j]}"

exit 0 
