#!/bin/bash
# sieve.sh (ex68.sh)

# 埃拉托色尼素数筛子
# 找素数的经典算法. 

#  在同等数值的范围内, 
#+ 这个脚本运行的速度比C版本慢的多. 

LOWER_LIMIT=1       # 从1开始. 
UPPER_LIMIT=1000    # 到1000. 
# (如果你时间很多的话 . . . 你可以将这个数值调的很高.)

PRIME=1
NON_PRIME=0

let SPLIT=UPPER_LIMIT/2
# 优化: 
# 只需要测试中间到最大的值(为什么?). 
# (译者注: 这个变量在脚本正文并没有被使用, 仅仅在107行之后的优化部分才使用.)

declare -a Primes
# Primes[]是个数组. 


initialize ()
{
# 初始化数组. 

i=$LOWER_LIMIT
until [ "$i" -gt "$UPPER_LIMIT" ]
do
  Primes[i]=$PRIME
  let "i += 1"
done
#  假定所有数组成员都是需要检查的(素数)
#+ 直到检查完成. 
}

print_primes ()
{
# 打印出所有数组Primes[]中被标记为素数的元素. 

i=$LOWER_LIMIT

until [ "$i" -gt "$UPPER_LIMIT" ]
do

  if [ "${Primes[i]}" -eq "$PRIME" ]
  then
    printf "%8d" $i
    # 每个数字打印前先打印8个空格, 在偶数列才打印. 
  fi
  
  let "i += 1"
  
done

}

sift () # 查出非素数. 
{

let i=$LOWER_LIMIT+1
# 我们都知道1是素数, 所以我们从2开始. 
# (译者注: 从2开始并不是由于1是素数, 而是因为要去掉以后每个数的倍数, 感谢网友KevinChen.)
until [ "$i" -gt "$UPPER_LIMIT" ]
do

if [ "${Primes[i]}" -eq "$PRIME" ]
# 不要处理已经过滤过的数字(被标识为非素数).
then

  t=$i

  while [ "$t" -le "$UPPER_LIMIT" ]
  do
    let "t += $i "
    Primes[t]=$NON_PRIME
    # 标识为非素数. 
  done

fi  

  let "i += 1"
done  


}


# ==============================================
# main ()
# 继续调用函数. 
initialize
sift
print_primes
# 这里就是被称为结构化编程的东西. 
# ==============================================

echo

exit 0



# -------------------------------------------------------- #
# 因为前面的'exit'语句, 所以后边的代码不会运行. 

#  下边的代码, 是由Stephane Chazelas所编写的埃拉托色尼素数筛子的改进版本, 
#+ 这个版本可以运行的快一些. 

# 必须在命令行上指定参数(这个参数就是: 寻找素数的限制范围). 

UPPER_LIMIT=$1                  # 来自于命令行. 
let SPLIT=UPPER_LIMIT/2         # 从中间值到最大值. 

Primes=( '' $(seq $UPPER_LIMIT) )

i=1
until (( ( i += 1 ) > SPLIT ))  # 仅需要从中间值检查. 
do
  if [[ -n $Primes[i] ]]
  then
    t=$i
    until (( ( t += i ) > UPPER_LIMIT ))
    do
      Primes[t]=
    done
  fi  
done  
echo ${Primes[*]}

exit 0
