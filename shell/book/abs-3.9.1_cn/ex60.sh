#!/bin/bash
# 函数和参数

DEFAULT=default                             # 默认参数值. 

func2 () {
   if [ -z "$1" ]                           # 第一个参数是否长度为零? 
   then
     echo "-Parameter #1 is zero length.-"  # 或者没有参数被传递进来. 
   else
     echo "-Param #1 is \"$1\".-"
   fi

   variable=${1-$DEFAULT}                   #  这里的参数替换
   echo "variable = $variable"              #+ 表示什么? 
                                            #  ---------------------------
                                            #  为了区分没有参数的情况, 
                                            #+ 和只有一个null参数的情况. 

   if [ "$2" ]
   then
     echo "-Parameter #2 is \"$2\".-"
   fi

   return 0
}

echo
   
echo "Nothing passed."   
func2                          # 不带参数调用
echo


echo "Zero-length parameter passed."
func2 ""                       # 使用0长度的参数进行调用
echo

echo "Null parameter passed."
func2 "$uninitialized_param"   # 使用未初始化的参数进行调用
echo

echo "One parameter passed."   
func2 first           # 带一个参数调用
echo

echo "Two parameters passed."   
func2 first second    # 带两个参数调用
echo

echo "\"\" \"second\" passed."
func2 "" second       # 带两个参数调用, 
echo                  # 第一个参数长度为0, 第二个参数是由ASCII码组成的字符串. 

exit 0
