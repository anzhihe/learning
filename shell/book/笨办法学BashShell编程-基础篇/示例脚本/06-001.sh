#!/bin/bash

increment () {
  sum=`expr $1 + 1`
  return $sum
}

echo -n "The sum is "
increment 5
echo $?  $sum

echo -n "The sum is "
increment 255
echo $?  $sum

exit 0
