#!/bin/bash
# "与列表"

if [ ! -z "$1" ] && echo "Argument #1 = $1" && [ ! -z "$2" ] && echo "Argument #2 = $2"
then
  echo "At least 2 arguments passed to script."
  # 所有连接起来的命令都返回true. 
else
  echo "Less than 2 arguments passed to script."
  # 整个命令列表中至少有一个命令返回false. 
fi  
# 注意, "if [ ! -z $1 ]"也可以, 但它是有所假定的等价物. 
#   if [ -n $1 ] 这个不行. 
#     然而, 如果加了引用就行了. 
#  if [ -n "$1" ] 这样就行了. 
#     小心!
# 最好将你要测试的变量引用起来, 这么做是非常好的习惯. 


# 下面这段代码与上面代码是等价的, 不过下面这段代码使用的是"纯粹"的if/then结构. 
if [ ! -z "$1" ]
then
  echo "Argument #1 = $1"
fi
if [ ! -z "$2" ]
then
  echo "Argument #2 = $2"
  echo "At least 2 arguments passed to script."
else
  echo "Less than 2 arguments passed to script."
fi
# 这么写的话, 行数太多了, 没有"与列表"来的精简. 


exit 0
