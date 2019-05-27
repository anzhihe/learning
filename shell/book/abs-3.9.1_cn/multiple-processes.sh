#!/bin/bash
# parent.sh
# 在多处理器(SMP box)的机器里运行多进程. 
# 作者: Tedman Eng

#  我们下面要介绍两个脚本, 这是第一个, 
#+ 这两个脚本都要放到当前工作目录下. 




LIMIT=$1         # 想要启动的进程总数
NUMPROC=4        # 并发的线程数量(forks?)
PROCID=1         # 启动的进程ID
echo "My PID is $$"

function start_thread() {
        if [ $PROCID -le $LIMIT ] ; then
                ./child.sh $PROCID&
                let "PROCID++"
        else
           echo "Limit reached."
           wait
           exit
        fi
}

while [ "$NUMPROC" -gt 0 ]; do
        start_thread;
        let "NUMPROC--"
done


while true
do

trap "start_thread" SIGRTMIN

done

exit 0



# ======== 下面是第二个脚本 ========


#!/bin/bash
# child.sh
# 在SMP box上运行多进程. 
# 这个脚本会被parent.sh调用. 
# 作者: Tedman Eng

temp=$RANDOM
index=$1
shift
let "temp %= 5"
let "temp += 4"
echo "Starting $index  Time:$temp" "$@"
sleep ${temp}
echo "Ending $index"
kill -s SIGRTMIN $PPID

exit 0


# ======================= 脚本作者注 ======================= #
#  这个脚本并不是一点bug都没有. 
#  我使用limit = 500来运行这个脚本, 但是在过了开头的一两百个循环后, 
#+ 有些并发线程消失了! 
#  还不能确定这是否是由捕捉信号的冲突引起的, 或者是其他什么原因. 
#  一旦接收到捕捉的信号, 那么在下一次捕捉到来之前, 
#+ 会有一段短暂的时间来执行信号处理程序, 
#+ 在信号处理程序处理的过程中, 很有可能会丢失一个想要捕捉的信号, 因此失去一个产生子进程的机会. 

#  毫无疑问的, 肯定有人能够找出产生这个bug的原因, 
#+ 并且在将来的某个时候. . . 修正它.



# ===================================================================== #



# ----------------------------------------------------------------------#



#################################################################
# 下面的脚本是由Vernia Damiano原创. 
# 不幸的是, 它并不能正常工作. 
#################################################################

#!/bin/bash

#  要想调用这个脚本, 至少需要一个整形参数
#+ (并发的进程数). 
#  所有的其他参数都传递给要启动的进程. 


INDICE=8        # 想要启动的进程数目
TEMPO=5         # 每个进程最大的睡眠时间
E_BADARGS=65    # 如果没有参数传到脚本中, 那么就返回这个错误码. 

if [ $# -eq 0 ] # 检查一下, 至少要传递一个参数给脚本. 
then
  echo "Usage: `basename $0` number_of_processes [passed params]"
  exit $E_BADARGS
fi

NUMPROC=$1              # 并发进程数
shift
PARAMETRI=( "$@" )      # 每个进程的参数

function avvia() {
         local temp
         local index
         temp=$RANDOM
         index=$1
         shift
         let "temp %= $TEMPO"
         let "temp += 1"
         echo "Starting $index Time:$temp" "$@"
         sleep ${temp}
         echo "Ending $index"
         kill -s SIGRTMIN $$
}

function parti() {
         if [ $INDICE -gt 0 ] ; then
              avvia $INDICE "${PARAMETRI[@]}" &
                let "INDICE--"
         else
                trap : SIGRTMIN
         fi
}

trap parti SIGRTMIN

while [ "$NUMPROC" -gt 0 ]; do
         parti;
         let "NUMPROC--"
done

wait
trap - SIGRTMIN

exit $?

: &lt;&lt;SCRIPT_AUTHOR_COMMENTS
我需要使用指定的选项来运行一个程序, 
并且能够接受不同的文件, 而且要运行在一个多处理器(SMP)的机器上. 
所以我想(我也会)运行指定数目个进程, 
并且每个进程终止之后, 都要启动一个新进程. 

"wait"命令并没有提供什么帮助, 因为它需要等待一个指定的后台进程, 
或者等待*全部*的后台进程. 所以我编写了[这个]bash脚本程序来完成这个工作, 
并且使用了"trap"指令. 
  --Vernia Damiano
SCRIPT_AUTHOR_COMMENTS
