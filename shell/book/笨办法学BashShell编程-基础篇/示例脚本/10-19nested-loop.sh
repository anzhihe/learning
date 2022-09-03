#!/bin/bash

outer=1		# 外部循环计数器
for a in 1 2 3 4 5
do
  echo "Pass $outer in outer Loop."
  echo "---------------------"
  inner=1 	# 重置内部循环计数器
  for b in 1 2 3 4 5
  do
    echo "Pass $inner in inner Loop."
    let "inner+=1"
  done

  let "outer+=1"
  echo
done

exit 0 
