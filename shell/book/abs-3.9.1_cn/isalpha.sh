#!/bin/bash
# isalpha.sh: 使用"case"结构来过滤字符串. 

SUCCESS=0
FAILURE=-1

isalpha ()  # 检查输入的 *第一个字符* 是不是字母表上的字符.
{
if [ -z "$1" ]                # 没有参数传进来?
then
  return $FAILURE
fi

case "$1" in
[a-zA-Z]*) return $SUCCESS;;  # 以一个字母开头?
*        ) return $FAILURE;;
esac
}             # 同C语言的"isalpha ()"函数比较一下. 


isalpha2 ()   # 测试 *整个字符串* 是否都是字母表上的字符.
{
  [ $# -eq 1 ] || return $FAILURE

  case $1 in
  *[!a-zA-Z]*|"") return $FAILURE;;
               *) return $SUCCESS;;
  esac
}

isdigit ()    # 测试 *整个字符串* 是否都是数字.
{             # 换句话说, 就是测试一下是否是整数变量.
  [ $# -eq 1 ] || return $FAILURE

  case $1 in
  *[!0-9]*|"") return $FAILURE;;
            *) return $SUCCESS;;
  esac
}



check_var ()  # 测试isalpha().
{
if isalpha "$@"
then
  echo "\"$*\" begins with an alpha character."
  if isalpha2 "$@"
  then        # 不需要测试第一个字符是否是non-alpha.
    echo "\"$*\" contains only alpha characters."
  else
    echo "\"$*\" contains at least one non-alpha character."
  fi  
else
  echo "\"$*\" begins with a non-alpha character."
              # 如果没有参数传递进来, 也是"non-alpha". 
fi

echo

}

digit_check ()  # 测试isdigit().
{
if isdigit "$@"
then
  echo "\"$*\" contains only digits [0 - 9]."
else
  echo "\"$*\" has at least one non-digit character."
fi

echo

}

a=23skidoo
b=H3llo
c=-What?
d=What?
e=`echo $b`   # 命令替换.
f=AbcDef
g=27234
h=27a34
i=27.34

check_var $a
check_var $b
check_var $c
check_var $d
check_var $e
check_var $f
check_var     # 没有参数传递进来, 将会发生什么?
#
digit_check $g
digit_check $h
digit_check $i


exit 0        # S.C改进了这个脚本.

# 练习:
# -----
#  编写一个'isfloat ()'函数来测试浮点数.
#  暗示: 这个函数基本上与'isdigit ()'相同,
#+ 但是要添加一些小数点部分的处理.
