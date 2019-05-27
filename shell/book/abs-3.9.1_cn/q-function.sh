#!/bin/bash

# Douglas Hofstadter的声名狼藉的序列"Q-series":

# Q(1) = Q(2) = 1
# Q(n) = Q(n - Q(n-1)) + Q(n - Q(n-2)), 当n&gt;2时

# 这是一个令人感到陌生的, 没有规律的"乱序"整数序列. 
# 序列的头20项, 如下所示: 
# 1 1 2 3 3 4 5 5 6 6 6 8 8 8 10 9 10 11 11 12 

#  请参考相关书籍, Hofstadter的, "_Goedel, Escher, Bach: An Eternal Golden Braid_",
#+ 第137页. 


LIMIT=100     # 需要计算的数列长度. 
LINEWIDTH=20  # 每行打印的个数. 

Q[1]=1        # 数列的头两项都为1. 
Q[2]=1

echo
echo "Q-series [$LIMIT terms]:"
echo -n "${Q[1]} "             # 输出数列头两项. 
echo -n "${Q[2]} "

for ((n=3; n <= $LIMIT; n++))  # C风格的循环条件. 
do   # Q[n] = Q[n - Q[n-1]] + Q[n - Q[n-2]]  当n&gt;2时
#  需要将表达式拆开, 分步计算, 
#+ 因为Bash不能够很好的处理复杂数组的算术运算. 

  let "n1 = $n - 1"        # n-1
  let "n2 = $n - 2"        # n-2
  
  t0=`expr $n - ${Q[n1]}`  # n - Q[n-1]
  t1=`expr $n - ${Q[n2]}`  # n - Q[n-2]
  
  T0=${Q[t0]}              # Q[n - Q[n-1]]
  T1=${Q[t1]}              # Q[n - Q[n-2]]

Q[n]=`expr $T0 + $T1`      # Q[n - Q[n-1]] + Q[n - Q[n-2]]
echo -n "${Q[n]} "

if [ `expr $n % $LINEWIDTH` -eq 0 ]    # 格式化输出. 
then   #      ^ 取模操作
  echo # 把每行都拆为20个数字的小块. 
fi

done

echo

exit 0

# 这是Q-series的一个迭代实现. 
# 更直接明了的实现是使用递归, 请读者作为练习完成. 
# 警告: 使用递归的方法来计算这个数列的话, 会花费非常长的时间. 
