#! /bin/bash
# array-append.bash

# Copyright (c) Michael S. Zick, 2003, All rights reserved.
# License: Unrestricted reuse in any form, for any purpose.
# Version: $ID$
#
# 在格式上, 由M.C做了一些修改. 


# 数组操作是Bash特有的属性. 
# 传统的UNIX /bin/sh缺乏类似的功能. 


#  将这个脚本的输出通过管道传递给'more', 
#+ 这么做的目的是防止输出的内容超过终端能够显示的范围. 


# 依次使用下标. 
declare -a array1=( zero1 one1 two1 )
# 数组中存在空缺的元素([1]未定义). 
declare -a array2=( [0]=zero2 [2]=two2 [3]=three2 )

echo
echo '- Confirm that the array is really subscript sparse. -'
echo "Number of elements: 4"        # 仅仅为了演示, 所以就写死了. 
for (( i = 0 ; i < 4 ; i++ ))
do
    echo "Element [$i]: ${array2[$i]}"
done
# 也可以参考一个更通用的例子, basics-reviewed.bash. 


declare -a dest

# 将两个数组合并(附加)到第3个数组. 
echo
echo 'Conditions: Unquoted, default IFS, All-Elements-Of operator'
echo '- Undefined elements not present, subscripts not maintained. -'
# # 那些未定义的元素不会出现; 组合时会丢弃这些元素. 

dest=( ${array1[@]} ${array2[@]} )
# dest=${array1[@]}${array2[@]}     # 令人奇怪的结果, 或许是个bug. 

# 现在, 打印结果. 
echo
echo '- - Testing Array Append - -'
cnt=${#dest[@]}

echo "Number of elements: $cnt"
for (( i = 0 ; i < cnt ; i++ ))
do
    echo "Element [$i]: ${dest[$i]}"
done

# 将数组赋值给一个数组中的元素(两次). 
dest[0]=${array1[@]}
dest[1]=${array2[@]}

# 打印结果. 
echo
echo '- - Testing modified array - -'
cnt=${#dest[@]}

echo "Number of elements: $cnt"
for (( i = 0 ; i < cnt ; i++ ))
do
    echo "Element [$i]: ${dest[$i]}"
done

# 检查第二个元素的修改状况. 
echo
echo '- - Reassign and list second element - -'

declare -a subArray=${dest[1]}
cnt=${#subArray[@]}

echo "Number of elements: $cnt"
for (( i = 0 ; i < cnt ; i++ ))
do
    echo "Element [$i]: ${subArray[$i]}"
done

#  如果你使用'=${ ... }'形式
#+ 将一个数组赋值到另一个数组的一个元素中, 
#+ 那么这个数组的所有元素都会被转换为一个字符串, 
#+ 这个字符串中的每个数组元素都以空格进行分隔(其实是IFS的第一个字符). 

# 如果原来数组中的所有元素都不包含空白符 . . .
# 如果原来的数组下标都是连续的 . . .
# 那么我们就可以将原来的数组进行恢复. 

# 从修改过的第二个元素中, 将原来的数组恢复出来. 
echo
echo '- - Listing restored element - -'

declare -a subArray=( ${dest[1]} )
cnt=${#subArray[@]}

echo "Number of elements: $cnt"
for (( i = 0 ; i < cnt ; i++ ))
do
    echo "Element [$i]: ${subArray[$i]}"
done
echo '- - Do not depend on this behavior. - -'
echo '- - This behavior is subject to change - -'
echo '- - in versions of Bash newer than version 2.05b - -'

# MSZ: 抱歉, 之前混淆了一些要点(译者注: 指的是本书以前的版本). 

exit 0
