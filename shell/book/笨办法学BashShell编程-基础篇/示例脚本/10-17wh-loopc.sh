#!/bin/bash

# C语言网络的while循环
((LIMIT = 10))
((a = 1))

while (( a<=LIMIT ))
do
  echo -n "$a "
  ((a += 1))
done

echo
exit 0
