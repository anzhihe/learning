#!/bin/bash
# 练习 getopts 和 OPTIND
# 在Bill Gradwohl的建议下, 这个脚本于 10/09/03 被修改.


# 在这里我们将学习如何使用 'getopts' 来处理脚本的命令行参数.
# 参数被作为"选项"(标志)来解析, 并且对选项分配参数. 

# 试一下, 使用如下方法来调用这个脚本
# 'scriptname -mn'
# 'scriptname -oq qOption' (qOption 可以是任意的哪怕有些诡异字符的字符串.)
# 'scriptname -qXXX -r'
#
# 'scriptname -qr'    - 意外的结果, "r" 将被看成是选项 "q" 的参数.
# 'scriptname -q -r'  - 意外的结果, 同上.
# 'scriptname -mnop -mnop'  - 意外的结果
# (OPTIND在选项刚传递进来的地方是不可靠的). 
# (译者注: 也就是说OPTIND只是一个参数指针, 指向下一个参数的位置.
#  比如:	-mnop 在mno处理的位置OPTION都为1, 而到p的处理就变成2, 
#			-m -n -o 在m的时候OPTION为2, 而n为3, o为4,
#			也就是说它总指向下一个位置). 
#
#  如果选项需要一个参数的话("flag:"), 那么它将获取
#+ 命令行上紧挨在它后边的任何字符.

NO_ARGS=0 
E_OPTERROR=65

if [ $# -eq "$NO_ARGS" ]  # 不带命令行参数就调用脚本?
then
  echo "Usage: `basename $0` options (-mnopqrs)"
  exit $E_OPTERROR        # 如果没有参数传递进来, 那么就退出脚本, 并且解释此脚本的用法.
fi  
# 用法: scriptname -options
# 注意: 必须使用破折号 (-) 


while getopts ":mnopq:rs" Option
do
  case $Option in
    m     ) echo "Scenario #1: option -m-   [OPTIND=${OPTIND}]";;
    n | o ) echo "Scenario #2: option -$Option-   [OPTIND=${OPTIND}]";;
    p     ) echo "Scenario #3: option -p-   [OPTIND=${OPTIND}]";;
    q     ) echo "Scenario #4: option -q-\
 with argument \"$OPTARG\"   [OPTIND=${OPTIND}]";;
    #  注意, 选项'q'必须分配一个参数, 
    #+ 否则, 默认将失败.
    r | s ) echo "Scenario #5: option -$Option-";;
    *     ) echo "Unimplemented option chosen.";;   # 默认情况的处理
  esac
done

shift $(($OPTIND - 1))
#  (译者注: shift命令是可以带参数的, 参数就是移动的个数)
#  将参数指针减1, 这样它将指向下一个参数.
#  $1 现在引用的是命令行上的第一个非选项参数,
#+ 如果有一个这样的参数存在的话.

exit 0

#   就像 Bill Gradwohl 所描述的,
#  "getopts机制允许指定一个参数, 
#+ 但是scriptname -mnop -mnop就是一种比较特殊的情况, 
#+ 因为在使用OPTIND的时候, 没有可靠的方法来区分到底传递进来了什么东西."
