#!/bin/bash
# match-string.sh: 简单的字符串匹配

match_string ()
{
  MATCH=0
  NOMATCH=90
  PARAMS=2     # 此函数需要2个参数.
  BAD_PARAMS=91

  [ $# -eq $PARAMS ] || return $BAD_PARAMS

  case "$1" in
  "$2") return $MATCH;;
  *   ) return $NOMATCH;;
  esac

}  


a=one
b=two
c=three
d=two


match_string $a     # 参数个数错误.
echo $?             # 91

match_string $a $b  # 不匹配
echo $?             # 90

match_string $b $d  # 匹配
echo $?             # 0


exit 0		    
