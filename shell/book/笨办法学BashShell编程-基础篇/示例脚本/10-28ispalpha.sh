#!/bin/bash
# 使用case结构来过滤字串

SUCCESS=0
FAILURE=1

# 检查输入的第一个字符是否是字母表上的字符
isalpha ()
{
  if [ -z "$1" ] ; then
    return $FAILURE
  fi
  
  case "$1" in
    [a-zA-Z]* ) return $SUCCESS ;; # 以字母开头
    *         ) return $FAILURE ;;
  esac
}


# 测试整个字符串是否都是字母表上的字符
isalpha2 ()
{
  [ $# -eq 1 ] || return $FAILURE	# 另一种判断传递参数的作法
  
  case "$1" in
    *[!a-zA-Z]* | "" ) return $FAILURE ;; 
    *                ) return $SUCCESS ;;
  esac
}


# 测试整个字符串是否都是数字
isdigit ()
{
  [ $# -eq 1 ] || return $FAILUREd
  
  case "$1" in
    *[!0-9]* | "" ) return $FAILURE ;; 
    *             ) return $SUCCESS ;;
  esac
}

# 测试isplah()
check_var ()
{
  if isalpha "$@" ; then
    echo "\"$*\" begins with an alpha character."
    if isalpha2 "$@" ; then
      echo "\"$*\" contains only alpha characters"
    else
      echo "\"$*\" contains at least on non-alpha characters"
    fi
  else
    echo "\"$*\" begin with a non-alpha characters"
  fi
  
  echo
}

# 测试isdigit()
digit_check ()
{
  if isdigit "$@" ; then
    echo "\"$*\" contains only digit [0-9]."
  else
    echo "\"$*\" has at least on non-digit character]."
  fi
  echo
}

check_var "23skidoo"
check_var "H3llo"
check_var "-What?"
check_var "What?"
check_var "AbcDef"
check_var "12345"
check_var 

digit_check "12345"
digit_check "12e45"
digit_check "12.34"

exit 0
       
