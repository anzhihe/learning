#!/bin/bash

match_string ()
{
  MATCH=0
  NOMATCH=90
  PARAMS=2	# 此函数需要2个参数
  BAD_PARAMS=091

  [ $# -eq $PARAMS ] || return $BAD_PARAMS

  case "$1" in
    "$2" ) return $MATCH ;;
    *    ) return $NOMATCH ;;
  esac
}

a=one
b=two
c=three
d=two

match_string $a; echo $?	# 参数个数错误 91

match_string $a $b; echo $?	# 不匹配 90

match_string $b $d; echo $?	# 匹配 0

exit 0
