#!/bin/bash
# seeding-random.sh: 设置RANDOM变量作为种子.

MAXCOUNT=25       # 决定产生多少个随机数.

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

echo; echo

RANDOM=1          # 为随机数的产生来设置RANDOM种子.
random_numbers

echo; echo

RANDOM=1          # 设置同样的种子...
random_numbers    # ...将会和上边产生的随机序列相同.
                  #
                  # 复制一个相同的"随机"序列在什么情况下有用呢?

echo; echo

RANDOM=2          # 在试一次, 但是这次使用不同的种子...
random_numbers    # 这次将得到一个不同的随机序列.

echo; echo

# RANDOM=$$  使用脚本的进程ID来作为产生随机数的种子.
# 从 'time' 或 'date' 命令中取得RANDOM作为种子也是常用的做法.

# 一个很有想象力的方法...
SEED=$(head -1 /dev/urandom | od -N 1 | awk '{ print $2 }')
#  首先从/dev/urandom(系统伪随机设备文件)中取出一行,
#+ 然后将这个可打印行转换为8进制数, 使用"od"命令来转换.
#+ 最后使用"awk"来获得一个数,
#+ 这个数将作为产生随机数的种子.
RANDOM=$SEED
random_numbers

echo; echo

exit 0
