#!/bin/bash

a=24
b=47

# 1、而且 && 
if [ "$a" -eq 24 ] && [ "$b" -eq 47 ]
then
  echo "Test #1 succeeds."
else
  echo "Test #1 fails."
fi

# 如果这样写，会出错
# if [ "$a" -eq 24 && "$b" -eq 47 ]
# 如果这样写，没有问题
# if [[ "$a" -eq 24 && "$b" -eq 47 ]]

# 2、或者 ||
if [ "$a" -eq 88 ] || [ "$b" -eq 47 ]
then
  echo "Test #2 succeeds."
else
  echo "Test #2 fails."
fi

# 3、而且 -a 
if [ "$a" -eq 24 -a "$b" -eq 47 ]
then
  echo "Test #3 succeeds."
else
  echo "Test #3 fails."
fi

# 4、或者 -o 
if [ "$a" -eq 88 -o "$b" -eq 47 ]
then
  echo "Test #4 succeeds."
else
  echo "Test #4 fails."
fi

# 5、字符串比较， 而且 && 
a=aaaa
b=bbbb
if [ "$a" = aaaa ] && [ "$b" = bbbb ]
then
  echo "Test #5 succeeds."
else
  echo "Test #5 fails."
fi

exit 0
