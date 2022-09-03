#!/bin/bash
# 为变量RANDOM设置种子

MAXCOUNT=25

random_numbers ()
{
  count=0
  while [ "$count" -lt "$MAXCOUNT" ]
  do
    number=$RANDOM
    echo -n "$number "
    let "count += 1"
  done
}

# 实验1：使用1来做来种子
RANDOM=1
random_numbers
echo; echo

# 实验2：由于种子一样，所以输出结果与实验1相同 
RANDOM=1
random_numbers
echo; echo

# 实验3：种子不一样，结果不一样
RANDOM=2
random_numbers
echo; echo

# 实验4：使用脚本的进程ID来做种子
RANDOM=$$
random_numbers
echo; echo

# 实验5：更加有想象力的种子
SEED=`date +%s`
#SEED=$(head -1 /dev/urandom | od -N 1 | awk '{print $2}')
RANDOM=$SEED
random_numbers
echo; echo
