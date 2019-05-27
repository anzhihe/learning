#!/bin/bash
# array-function.sh: 将数组传递到函数中与...
#                   从函数中"返回"一个数组


Pass_Array ()
{
  local passed_array   # 局部变量. 
  passed_array=( `echo "$1"` )
  echo "${passed_array[@]}"
  #  列出这个新数组中的所有元素, 
  #+ 这个新数组是在函数内声明的, 也是在函数内赋值的. 
}


original_array=( element1 element2 element3 element4 element5 )

echo
echo "original_array = ${original_array[@]}"
#                      列出原始数组的所有元素. 


# 下面是关于如何将数组传递给函数的技巧. 
# **********************************
argument=`echo ${original_array[@]}`
# **********************************
#  将原始数组中所有的元素都用空格进行分隔, 
#+ 然后合并成一个字符串, 最后赋值给一个变量. 
#
# 注意, 如果只把数组传递给函数, 那是不行的. 


# 下面是让数组作为"返回值"的技巧. 
# *****************************************
returned_array=( `Pass_Array "$argument"` )
# *****************************************
# 将函数中'echo'出来的输出赋值给数组变量. 

echo "returned_array = ${returned_array[@]}"

echo "============================================================="

#  现在, 再试一次, 
#+ 尝试一下, 在函数外面访问(列出)数组. 
Pass_Array "$argument"

# 函数自身可以列出数组, 但是...
#+ 从函数外部访问数组是被禁止的. 
echo "Passed array (within function) = ${passed_array[@]}"
# NULL值, 因为这个变量是函数内部的局部变量. 

echo

exit 0
