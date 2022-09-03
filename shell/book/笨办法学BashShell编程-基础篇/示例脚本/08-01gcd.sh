#!/bin/bash

# 采用辗转相除法，求两个数的最大公约数

ARGS=2
E_BADARGS=65

if [ $# -ne "$ARGS" ]
then
  echo "Usage: `basename $0` first-number second-number"
  exit $E_BADARGS
fi

gcd ()
{ 
  dividend=$1
  divisor=$2
  remainder=1

  until [ "$remainder" -eq 0 ]
  do
    let "remainder = $dividend % $divisor"
    dividend=$divisor
    divisor=$remainder
  done
}

gcd $1 $2

echo ; echo "($1, $2)=$dividend"; echo 
exit 0 
