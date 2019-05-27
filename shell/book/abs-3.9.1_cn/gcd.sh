#!/bin/bash
# gcd.sh: 最大公约数
#         使用Euclid的算法

#  两个整数的"最大公约数" (gcd), 
#+ 就是两个整数所能够同时整除的最大的数. 

#  Euclid算法采用连续除法. 
#  在每一次循环中,
#+ 被除数 &lt;---  除数
#+ 除数 &lt;---  余数
#+ 直到 余数 = 0.
#+ 在最后一次循环中, gcd = 被除数.
#
#  关于Euclid算法的更精彩的讨论, 可以到
#+ Jim Loy的站点, http://www.jimloy.com/number/euclids.htm.


# ------------------------------------------------------
# 参数检查
ARGS=2
E_BADARGS=65

if [ $# -ne "$ARGS" ]
then
  echo "Usage: `basename $0` first-number second-number"
  exit $E_BADARGS
fi
# ------------------------------------------------------


gcd ()
{

  dividend=$1                    #  随意赋值.
  divisor=$2                     #+ 在这里, 哪个值给的大都没关系.
                                 #  为什么没关系?

  remainder=1                    #  如果在循环中使用了未初始化的变量, 
                                 #+ 那么在第一次循环中, 
                                 #+ 它将会产生一个错误消息. 

  until [ "$remainder" -eq 0 ]
  do
    let "remainder = $dividend % $divisor"
    dividend=$divisor            # 现在使用两个最小的数来重复.
    divisor=$remainder
  done                           # Euclid的算法

}                                # Last $dividend is the gcd.


gcd $1 $2

echo; echo "GCD of $1 and $2 = $dividend"; echo


# Exercise :
# --------
#  检查传递进来的命令行参数来确保它们都是整数.
#+ 如果不是整数, 那就给出一个适当的错误消息并退出脚本.

exit 0
