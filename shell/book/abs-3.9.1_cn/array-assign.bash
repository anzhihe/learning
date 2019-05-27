#! /bin/bash
# array-assign.bash

#  数组操作是Bash所特有的, 
#+ 所以才使用".bash"作为脚本扩展名. 

# Copyright (c) Michael S. Zick, 2003, All rights reserved.
# License: Unrestricted reuse in any form, for any purpose.
# Version: $ID$
#
# 说明与注释由William Park所添加. 

#  基于Stephane Chazelas所提供的
#+ 出现在本书中的一个例子. 

# 'times'命令的输出格式: 
# User CPU &lt;space&gt; System CPU
# User CPU of dead children &lt;space&gt; System CPU of dead children

#  Bash有两种方法, 
#+ 可以将一个数组的所有元素都赋值给一个新的数组变量. 
#  在2.04, 2.05a和2.05b版本的Bash中, 
#+ 这两种方法都会丢弃数组中的"空引用"(null值)元素. 
#  另一种给数组赋值的方法将会被添加到新版本的Bash中, 
#+ 这种方法采用[subscript]=value形式, 来维护数组下标与元素值之间的关系. 

#  可以使用内部命令来构造一个大数组, 
#+ 当然, 构造一个包含上千元素数组的其他方法
#+ 也能很好的完成任务. 

declare -a bigOne=( /dev/* )
echo
echo 'Conditions: Unquoted, default IFS, All-Elements-Of'
echo "Number of elements in array is ${#bigOne[@]}"

# set -vx



echo
echo '- - testing: =( ${array[@]} ) - -'
times
declare -a bigTwo=( ${bigOne[@]} )
#                 ^              ^
times

echo
echo '- - testing: =${array[@]} - -'
times
declare -a bigThree=${bigOne[@]}
# 这次没用括号. 
times

#  正如Stephane Chazelas所指出的, 通过比较, 
#+ 可以了解到第二种格式的赋值比第三或第四种形式更快. 
#
#  William Park解释: 
#+ 数组bigTwo是作为一个单个字符串被赋值的, 
#+ 而数组bigThree, 则是一个元素一个元素进行的赋值. 
#  所以, 实质上是: 
#                   bigTwo=( [0]="... ... ..." )
#                   bigThree=( [0]="..." [1]="..." [2]="..." ... )


#  在本书的例子中, 我还是会继续使用第一种形式, 
#+ 因为我认为这种形式更有利于将问题阐述清楚. 

#  在我所使用的例子中, 在其中复用的部分, 
#+ 还是使用了第二种形式, 那是因为这种形式更快. 

# MSZ: 很抱歉早先的疏忽(译者: 应是指本书的老版本). 


#  注意事项:
#  ---------
#  31行和43行的"declare -a"语句其实不是必需的, 
#+ 因为Array=( ... )形式
#+ 只能用于数组赋值. 
#  然而, 如果省略这些声明的话, 
#+ 会导致脚本后边的相关操作变慢. 
#  试一下, 看看发生了什么. 

exit 0
