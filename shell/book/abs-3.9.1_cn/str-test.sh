#!/bin/bash
#  str-test.sh: 检查null字符串和未引用的字符串,
#+ but not strings and sealing wax, not to mention cabbages and kings . . .
#+ 但不是字符串和封蜡, 也并没有提到卷心菜和国王. . . ??? (没看懂, rojy bug)

# 使用   if [ ... ]


# 如果字符串并没有被初始化, 那么它里面的值未定义.
# 这种状态被称为"null" (注意这与零值不同).

if [ -n $string1 ]    # $string1 没有被声明和初始化.
then
  echo "String \"string1\" is not null."
else  
  echo "String \"string1\" is null."
fi  
# 错误的结果.
# 显示$string1为非null, 虽然这个变量并没有被初始化.


echo


# 让我们再试一下.

if [ -n "$string1" ]  # 这次$string1被引号扩起来了. 
then
  echo "String \"string1\" is not null."
else  
  echo "String \"string1\" is null."
fi                    # 注意一定要将引用的字符放到中括号结构中!


echo


if [ $string1 ]       # 这次, 就一个$string1, 什么都不加.
then
  echo "String \"string1\" is not null."
else  
  echo "String \"string1\" is null."
fi  
# 这种情况运行的非常好.
# [ ] 测试操作符能够独立检查string是否为null.
# 然而, 使用("$string1")是一种非常好的习惯.
#
# 就像Stephane Chazelas所指出的,
#    if [ $string1 ]    只有一个参数, "]"
#    if [ "$string1" ]  有两个参数, 一个是空的"$string1", 另一个是"]" 



echo



string1=initialized

if [ $string1 ]       # 再来, 还是只有$string1, 什么都不加.
then
  echo "String \"string1\" is not null."
else  
  echo "String \"string1\" is null."
fi  
# 再来试一下, 给出了正确的结果.
# 再强调一下, 使用引用的("$string1")还是更好一些, 原因我们上边已经说过了.


string1="a = b"

if [ $string1 ]       # 再来, 还是只有$string1, 什么都不加.
then
  echo "String \"string1\" is not null."
else  
  echo "String \"string1\" is null."
fi  
# 未引用的"$string1", 这回给出了错误的结果! 

exit 0
# 也感谢Florian Wisser, 给出了上面这个"足智多谋"的例子.
