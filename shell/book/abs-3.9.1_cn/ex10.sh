#!/bin/bash

#  小技巧:
#  如果你不能够确定一个特定的条件该如何进行判断,
#+ 那么就使用if-test结构. 

echo

echo "Testing \"0\""
if [ 0 ]      # zero
then
  echo "0 is true."
else
  echo "0 is false."
fi            # 0 为真.

echo

echo "Testing \"1\""
if [ 1 ]      # one
then
  echo "1 is true."
else
  echo "1 is false."
fi            # 1 为真.

echo

echo "Testing \"-1\""
if [ -1 ]     # 负1
then
  echo "-1 is true."
else
  echo "-1 is false."
fi            # -1 为真.

echo

echo "Testing \"NULL\""
if [ ]        # NULL (空状态)
then
  echo "NULL is true."
else
  echo "NULL is false."
fi            # NULL 为假.

echo

echo "Testing \"xyz\""
if [ xyz ]    # 字符串
then
  echo "Random string is true."
else
  echo "Random string is false."
fi            # 随便的一串字符为真.

echo

echo "Testing \"\$xyz\""
if [ $xyz ]   # 判断$xyz是否为null, 但是...
              # 这只是一个未初始化的变量.
then
  echo "Uninitialized variable is true."
else
  echo "Uninitialized variable is false."
fi            # 未定义的初始化为假.

echo

echo "Testing \"-n \$xyz\""
if [ -n "$xyz" ]            # 更加正规的条件检查.
then
  echo "Uninitialized variable is true."
else
  echo "Uninitialized variable is false."
fi            # 未初始化的变量为假.

echo


xyz=          # 初始化了, 但是赋null值.

echo "Testing \"-n \$xyz\""
if [ -n "$xyz" ]
then
  echo "Null variable is true."
else
  echo "Null variable is false."
fi            # null变量为假. 


echo


# 什么时候"false"为真?

echo "Testing \"false\""
if [ "false" ]              #  看起来"false"只不过是一个字符串而已. 
then
  echo "\"false\" is true." #+ 并且条件判断的结果为真.
else
  echo "\"false\" is false."
fi            # "false" 为真.

echo

echo "Testing \"\$false\""  # 再来一个, 未初始化的变量.
if [ "$false" ]
then
  echo "\"\$false\" is true."
else
  echo "\"\$false\" is false."
fi            # "$false" 为假.
              # 现在, 我们得到了预期的结果.

#  如果我们测试以下为初始化的变量"$true"会发生什么呢?

echo

exit 0
