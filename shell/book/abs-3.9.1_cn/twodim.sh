#!/bin/bash
# twodim.sh: 模拟一个二维数组. 

# 一维数组由单行组成. 
# 二维数组由连续的多行组成. 

Rows=5
Columns=5
# 5 X 5 的数组.

declare -a alpha     # char alpha [Rows] [Columns];
                     # 没必要声明. 为什么?

load_alpha ()
{
local rc=0
local index

for i in A B C D E F G H I J K L M N O P Q R S T U V W X Y
do     # 你可以随你的心意, 使用任意符号. 
  local row=`expr $rc / $Columns`
  local column=`expr $rc % $Rows`
  let "index = $row * $Rows + $column"
  alpha[$index]=$i
# alpha[$row][$column]
  let "rc += 1"
done  

#  更简单的方法: 
#+   declare -a alpha=( A B C D E F G H I J K L M N O P Q R S T U V W X Y )
#+ 但是如果写的话, 就缺乏二维数组的"风味"了. 
}

print_alpha ()
{
local row=0
local index

echo

while [ "$row" -lt "$Rows" ]   #  以"行序为主"进行打印: 
do                             #+ 行号不变(外层循环),
                               #+ 列号进行增长. (译者注: 就是按行打印)
  local column=0

  echo -n "       "            #  按照行方向打印"正方形"数组. 

  while [ "$column" -lt "$Columns" ]
  do
    let "index = $row * $Rows + $column"
    echo -n "${alpha[index]} "  # alpha[$row][$column]
    let "column += 1"
  done

  let "row += 1"
  echo

done  

# 更简单的等价写法为: 
#     echo ${alpha[*]} | xargs -n $Columns

echo
}

filter ()     # 过滤掉负的数组下标. 
{

echo -n "  "  # 产生倾斜. 
              # 解释一下, 这是怎么做到的. 

if [[ "$1" -ge 0 &&  "$1" -lt "$Rows" && "$2" -ge 0 && "$2" -lt "$Columns" ]]
then
    let "index = $1 * $Rows + $2"
    # 现在, 按照旋转方向进行打印. 
    echo -n " ${alpha[index]}"
    #           alpha[$row][$column]
fi    

}
  



rotate ()  #  将数组旋转45度 --
{          #+ 从左下角进行"平衡". 
local row
local column

for (( row = Rows; row > -Rows; row-- ))
  do       # 反向步进数组, 为什么? 

  for (( column = 0; column < Columns; column++ ))
  do

    if [ "$row" -ge 0 ]
    then
      let "t1 = $column - $row"
      let "t2 = $column"
    else
      let "t1 = $column"
      let "t2 = $column + $row"
    fi  

    filter $t1 $t2   # 将负的数组下标过滤出来. 
                     # 如果你不做这一步, 将会怎样? 
  done

  echo; echo

done 

#  数组旋转的灵感来源于Herbert Mayer所著的
#+ "Advanced C Programming on the IBM PC"的例子(第143-146页)
#+ (参见参考书目). 
#  由此可见, C语言能够做到的好多事情, 
#+ 用shell脚本一样能够做到. 

}


#--------------- 现在, 让我们开始吧. ------------#
load_alpha     # 加载数组. 
print_alpha    # 打印数组.   
rotate         # 逆时钟旋转45度打印. 
#-----------------------------------------------------#

exit 0

# 这是有点做作, 不是那么优雅. 

# 练习:
# -----
# 1)  重新实现数组加载和打印函数, 
#     让其更直观, 可读性更强. 
#
# 2)  详细地描述旋转函数的原理. 
#     提示: 思考一下倒序索引数组的实现. 
#
# 3)  重写这个脚本, 扩展它, 让不仅仅能够支持非正方形的数组. 
#     比如6 X 4的数组. 
#     尝试一下, 在数组旋转时, 做到最小"失真". 
