#! /bin/bash
# CopyArray.sh
#
# 这个脚本由Michael Zick所编写. 
# 已通过作者授权, 可以在本书中使用. 

#  如何"通过名字传值&通过名字返回"(译者注: 这里可以理解为C中的"数组指针", 或C++中的"数组引用")
#+ 或者"建立自己的赋值语句". 


CpArray_Mac() {

# 建立赋值命令

    echo -n 'eval '
    echo -n "$2"                    # 目的参数名
    echo -n '=( ${'
    echo -n "$1"                    # 原参数名
    echo -n '[@]} )'

# 上边这些语句会构成一条命令. 
# 这仅仅是形式上的问题. 
}

declare -f CopyArray                # 函数"指针"
CopyArray=CpArray_Mac               # 构造语句

Hype()
{

# 需要连接的数组名为$1. 
# (把这个数组与字符串"Really Rocks"结合起来, 形成一个新数组.)
# 并将结果从数组$2中返回. 

    local -a TMP
    local -a hype=( Really Rocks )

    $($CopyArray $1 TMP)
    TMP=( ${TMP[@]} ${hype[@]} )
    $($CopyArray TMP $2)
}

declare -a before=( Advanced Bash Scripting )
declare -a after

echo "Array Before = ${before[@]}"

Hype before after

echo "Array After = ${after[@]}"

# 连接的太多了? 

echo "What ${after[@]:3:2}?"

declare -a modest=( ${after[@]:2:1} ${after[@]:3:2} )
#                    ----       子串提取       ----

echo "Array Modest = ${modest[@]}"

# 'before'发生了什么变化么? 

echo "Array Before = ${before[@]}"

exit 0
