#!/bin/bash
# array-ops.sh: 更多有趣的数组用法. 


array=( zero one two three four five )
# 数组元素 0   1   2    3     4    5

echo ${array[0]}       #  0
echo ${array:0}        #  0
                       #  第一个元素的参数扩展, 
                       #+ 从位置0(#0)开始(即第一个字符). 
echo ${array:1}        #  ero
                       #  第一个元素的参数扩展, 
                       #+ 从位置1(#1)开始(即第2个字符). 

echo "--------------"

echo ${#array[0]}      #  4
                       #  第一个数组元素的长度. 
echo ${#array}         #  4
                       #  第一个数组元素的长度. 
                       #  (另一种表示形式)

echo ${#array[1]}      #  3
                       #  第二个数组元素的长度. 
                       #  Bash中的数组是从0开始索引的. 

echo ${#array[*]}      #  6
                       #  数组中的元素个数. 
echo ${#array[@]}      #  6
                       #  数组中的元素个数.

echo "--------------"

array2=( [0]="first element" [1]="second element" [3]="fourth element" )

echo ${array2[0]}      # 第一个元素
echo ${array2[1]}      # 第二个元素
echo ${array2[2]}      #
                       # 因为并没有被初始化, 所以此值为null. 
echo ${array2[3]}      # 第四个元素


exit 0
