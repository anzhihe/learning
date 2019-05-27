#!/bin/bash
# cannon.sh: Approximating PI by firing cannonballs.

# 这事实上是一个"Monte Carlo"蒙特卡洛模拟的非常简单的实例:
#+ 蒙特卡洛模拟是一种由现实事件抽象出来的数学模型,
#+ 由于要使用随机抽样统计来估算数学函数, 所以使用伪随机数来模拟真正的随机数.

#  想象有一个完美的正方形土地, 边长为10000个单位.
#  在这块土地的中间有一个完美的圆形湖,
#+ 这个湖的直径是10000个单位.
#  这块土地的绝大多数面积都是水, 当然只有4个角上有一些土地.
#  (可以把这个湖想象成为这个正方形的内接圆.)
#
#  我们将使用老式的大炮和铁炮弹
#+ 向这块正方形的土地上开炮.
#  所有的炮弹都会击中这块正方形土地的某个地方.
#+ 或者是打到湖上, 或者是打到4个角的土地上.
#  因为这个湖占据了这个区域大部分地方,
#+ 所以大部分的炮弹都会"扑通"一声落到水里.
#  而只有很少的炮弹会"砰"的一声落到4个
#+ 角的土地上.
#
#  如果我们发出的炮弹足够随机的落到这块正方形区域中的话,
#+ 那么落到水里的炮弹与打出炮弹总数的比率,
#+ 大概非常接近于PI/4.
#
#  原因是所有的炮弹事实上都
#+ 打在了这个土地的右上角,
#+ 也就是, 笛卡尔坐标系的第一象限.
#  (之前的解释只是一个简化.)
#
#  理论上来说, 如果打出的炮弹越多, 就越接近这个数字.
#  然而, 对于shell 脚本来说一定会做些让步的,
#+ 因为它肯定不能和那些内建就支持浮点运算的编译语言相比.
#  当然就会降低精度.


DIMENSION=10000  # 这块土地的边长.
                 # 这也是所产生随机整数的上限.
                                                                         
MAXSHOTS=1000    # 开炮次数.
                 # 10000或更多次的话, 效果应该更好, 但有点太浪费时间了.
PMULTIPLIER=4.0  # 接近于PI的比例因子.

get_random ()
{
SEED=$(head -1 /dev/urandom | od -N 1 | awk '{ print $2 }')
RANDOM=$SEED                                  #  来自于"seeding-random.sh"
                                              #+ 的例子脚本.
let "rnum = $RANDOM % $DIMENSION"             #  范围小于10000.
echo $rnum
}

distance=        # 声明全局变量.
hypotenuse ()    # 从"alt-bc.sh"例子来的,
{                # 计算直角三角形的斜边的函数.
distance=$(bc -l << EOF
scale = 0
sqrt ( $1 * $1 + $2 * $2 )
EOF
)
#  设置 "scale" 为 0 , 好让结果四舍五入为整数值,
#+ 这也是这个脚本中必须折中的一个地方.
#  不幸的是, 这将降低模拟的精度.
}


# main() {

# 初始化变量. 
shots=0
splashes=0
thuds=0
Pi=0

while [ "$shots" -lt  "$MAXSHOTS" ]           # 主循环.
do                                                                      
                                                                        
  xCoord=$(get_random)                        # 取得随机的 X 与 Y 坐标.
  yCoord=$(get_random)                                                  
  hypotenuse $xCoord $yCoord                  #  直角三角形斜边 =
                                              #+ distance.
  ((shots++))                                                           
                                                                        
  printf "#%4d   " $shots                                               
  printf "Xc = %4d  " $xCoord                                           
  printf "Yc = %4d  " $yCoord                                           
  printf "Distance = %5d  " $distance         #  到湖中心的
                                              #+ 距离 --
                                              #  起始坐标点 --
                                              #+  (0,0).

  if [ "$distance" -le "$DIMENSION" ]
  then
    echo -n "SPLASH!  "
    ((splashes++))
  else
    echo -n "THUD!    "
    ((thuds++))
  fi

  Pi=$(echo "scale=9; $PMULTIPLIER*$splashes/$shots" | bc)
  # 将比例乘以4.0.
  echo -n "PI ~ $Pi"
  echo

done

echo
echo "After $shots shots, PI looks like approximately $Pi."
# 如果不太准的话, 那么就提高一下运行的次数. . .
# 可能是由于运行错误和随机数随机程度不高造成的.
echo

# }

exit 0

#  要想知道一个shell脚本到底适不适合对计算应用进行模拟的话?
#+ (一种需要对复杂度和精度都有要求的计算应用).
#
#  一般至少需要两个判断条件.
#  1) 作为一种概念的验证: 来显示它可以做到. 
#  2) 在使用真正的编译语言来实现一个算法之前, 
#+    使用脚本来测试和验证这个算法. 
