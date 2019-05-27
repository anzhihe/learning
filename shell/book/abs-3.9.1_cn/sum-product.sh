#!/bin/bash
# sum-product.sh
# 可以"返回"超过一个值的函数. 

sum_and_product ()   # 计算所有传递进来的参数的总和, 与总乘积. 
{
  echo $(( $1 + $2 )) $(( $1 * $2 ))
# 将每个计算出来的结果输出到stdout, 并以空格分隔. 
}

echo
echo "Enter first number "
read first

echo
echo "Enter second number "
read second
echo

retval=`sum_and_product $first $second`      # 将函数的输出赋值给变量. 
sum=`echo "$retval" | awk '{print $1}'`      # 赋值第一个域. 
product=`echo "$retval" | awk '{print $2}'`  # 赋值第二个域. 

echo "$first + $second = $sum"
echo "$first * $second = $product"
echo

exit 0
