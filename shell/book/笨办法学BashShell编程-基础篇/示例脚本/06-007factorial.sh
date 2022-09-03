#!/bin/bash
# 阶乘
MAX_ARG=5
E_WRONG_ARGS=65
E_RANGE_ERR=66

if [ -z "$1" ]; then
  echo "Usage: `basename $0` number"
  exit $E_WRONG_ARGS
fi

if [ "$1" -gt $MAX_ARG ]; then
  echo "Out of range (5 is maximum)."
  exit $E_RANGE_ERR
fi

fact () {
  local number=$1
  if [ "$number" -eq 0 ] ; then
    factorial=1		# 0 的阶乘为1
  else
    let "decrnum = number - 1"
    fact $decrnum	# 递归的函数调用，即自已调用自已
    let "factorial = $number * $?"
  fi
  return $factorial
}

fact $1
echo "Factorail of $1 is $?."
exit 0
