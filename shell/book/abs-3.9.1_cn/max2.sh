#!/bin/bash
# max2.sh: 取两个大整数中的最大值. 

#  这是前一个例子"max.sh"的修改版, 
#+ 这个版本可以比较两个大整数. 

EQUAL=0             # 如果两个值相等, 那就返回这个值. 
E_PARAM_ERR=-99999  # 没有足够多的参数传递给函数. 
#           ^^^^^^    任意超出范围的参数都可以传递进来. 

max2 ()             # "返回"两个整数中最大的那个. 
{
if [ -z "$2" ]
then
  echo $E_PARAM_ERR
  return
fi

if [ "$1" -eq "$2" ]
then
  echo $EQUAL
  return
else
  if [ "$1" -gt "$2" ]
  then
    retval=$1
  else
    retval=$2
  fi
fi

echo $retval        # 输出(到stdout), 而没有用返回值. 
                    # 为什么? 
}


return_val=$(max2 33001 33997)
#            ^^^^             函数名
#                 ^^^^^ ^^^^^ 传递进来的参数
#  这其实是命令替换的一种形式: 
#+ 可以把函数看作为一个命令, 
#+ 然后把函数的stdout赋值给变量"return_val." 


# ========================= OUTPUT ========================
if [ "$return_val" -eq "$E_PARAM_ERR" ]
  then
  echo "Error in parameters passed to comparison function!"
elif [ "$return_val" -eq "$EQUAL" ]
  then
    echo "The two numbers are equal."
else
    echo "The larger of the two numbers is $return_val."
fi
# =========================================================
  
exit 0

#  练习:
#  -----
#  1) 找到一种更优雅的方法, 
#+    来测试传递给函数的参数. 
#  2) 简化"输出"段的if/then结构. 
#  3) 重写这个脚本, 使其能够从命令行参数中获得输入. 
