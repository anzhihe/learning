#!/bin/bash
# monthlypmt.sh: 计算按月偿还贷款的数量. 


#  这份代码是一份修改版本, 原始版本在"mcalc"(贷款计算)包中, 
#+ 这个包的作者是Jeff Schmidt和Mendel Cooper(本书作者). 
#   http://www.ibiblio.org/pub/Linux/apps/financial/mcalc-1.6.tar.gz  [15k]

echo
echo "Given the principal, interest rate, and term of a mortgage,"
echo "calculate the monthly payment."

bottom=1.0

echo
echo -n "Enter principal (no commas) "
read principal
echo -n "Enter interest rate (percent) "  # 如果是12%, 那就键入"12", 而不是".12". 
read interest_r
echo -n "Enter term (months) "
read term


 interest_r=$(echo "scale=9; $interest_r/100.0" | bc) # 转换成小数. 
                 # "scale"指定了有效数字的个数.
  

 interest_rate=$(echo "scale=9; $interest_r/12 + 1.0" | bc)
 

 top=$(echo "scale=9; $principal*$interest_rate^$term" | bc)

 echo; echo "Please be patient. This may take a while."

 let "months = $term - 1"
# ==================================================================== 
 for ((x=$months; x > 0; x--))
 do
   bot=$(echo "scale=9; $interest_rate^$x" | bc)
   bottom=$(echo "scale=9; $bottom+$bot" | bc)
#  bottom = $(($bottom + $bot"))
 done
# ==================================================================== 

# -------------------------------------------------------------------- 
#  Rick Boivie给出了一个对上边循环的修改方案, 
#+ 这个修改更加有效率, 将会节省大概2/3的时间. 

# for ((x=1; x <= $months; x++))
# do
#   bottom=$(echo "scale=9; $bottom * $interest_rate + 1" | bc)
# done


#  然后他又想出了一个更加有效率的版本, 
#+ 将会节省95%的时间! 

# bottom=`{
#     echo "scale=9; bottom=$bottom; interest_rate=$interest_rate"
#     for ((x=1; x <= $months; x++))
#     do
#          echo 'bottom = bottom * interest_rate + 1'
#     done
#     echo 'bottom'
#     } | bc`       # 在命令替换中嵌入一个'for循环'. 
# --------------------------------------------------------------------------
#  另一方面, Frank Wang建议: 
#  bottom=$(echo "scale=9; ($interest_rate^$term-1)/($interest_rate-1)" | bc)

#  因为 . . .
#  在循环后边的算法
#+ 事实上是一个等比数列的求和公式. 
#  求和公式是 e0(1-q^n)/(1-q), 
#+ e0是第一个元素, q=e(n+1)/e(n), 
#+ n是元素数量.
# --------------------------------------------------------------------------


 # let "payment = $top/$bottom"
 payment=$(echo "scale=2; $top/$bottom" | bc)
 # 使用2位有效数字来表示美元和美分. 
 
 echo
 echo "monthly payment = \$$payment"  # 在总和的前边显示美元符号. 
 echo


 exit 0


 # 练习: 
 #   1) 处理输入允许本金总数中的逗号. 
 #   2) 处理输入允许按照百分号和小数点的形式输入利率. 
 #   3) 如果你真正想好好编写这个脚本, 
 #      那么就扩展这个脚本让它能够打印出完整的分期付款表. 
