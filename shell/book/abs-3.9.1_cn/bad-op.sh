#!/bin/bash
# bad-op.sh: 尝试一下对整数使用字符串比较. 

echo
number=1

# 下面的"while循环"有两个错误: 
#+ 一个比较明显, 而另一个比较隐蔽. 

while [ "$number" < 5 ]    # 错! 应该是:  while [ "$number" -lt 5 ]
do
  echo -n "$number "
  let "number += 1"
done  
#  如果你企图运行这个错误的脚本, 那么就会得到一个错误消息: 
#+ bad-op.sh: line 10: 5: No such file or directory
#  在单中括号结构([ ])中, "<"必须被转义. 
#+ 即便如此, 比较两个整数还是错误的. 


echo "---------------------"


while [ "$number" \< 5 ]    #  1 2 3 4
do                          #
  echo -n "$number "        #  看起来*好像可以工作, 但是 . . .
  let "number += 1"         #+ 事实上是比较ASCII码, 
done                        #+ 而不是整数比较. 

echo; echo "---------------------"

# 这么做会产生问题. 比如: 

lesser=5
greater=105

if [ "$greater" \< "$lesser" ]
then
  echo "$greater is less than $lesser"
fi                          # 105 is less than 5
#  事实上, 在字符串比较中(按照ASCII码的顺序)
#+ "105"小于"5". 

echo

exit 0
