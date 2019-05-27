#!/bin/bash
# empty-array.sh

#  感谢Stephane Chazelas制作这个例子的原始版本, 
#+ 同时感谢Michael Zick对这个例子所作的扩展. 


# 空数组与包含有空元素的数组, 这两个概念不同. 

array0=( first second third )
array1=( '' )   # "array1"包含一个空元素. 
array2=( )      # 没有元素 . . . "array2"为空. 

echo
ListArray()
{
echo
echo "Elements in array0:  ${array0[@]}"
echo "Elements in array1:  ${array1[@]}"
echo "Elements in array2:  ${array2[@]}"
echo
echo "Length of first element in array0 = ${#array0}"
echo "Length of first element in array1 = ${#array1}"
echo "Length of first element in array2 = ${#array2}"
echo
echo "Number of elements in array0 = ${#array0[*]}"  # 3
echo "Number of elements in array1 = ${#array1[*]}"  # 1  (惊奇!)
echo "Number of elements in array2 = ${#array2[*]}"  # 0
}

# ===================================================================

ListArray

# 尝试扩展这些数组. 

# 添加一个元素到这个数组. 
array0=( "${array0[@]}" "new1" )
array1=( "${array1[@]}" "new1" )
array2=( "${array2[@]}" "new1" )

ListArray

# 或
array0[${#array0[*]}]="new2"
array1[${#array1[*]}]="new2"
array2[${#array2[*]}]="new2"

ListArray

# 如果你按照上边的方法对数组进行扩展的话; 数组比较象'栈' 
# 上边的操作就是'压栈' 
# 栈'高'为: 
height=${#array2[@]}
echo
echo "Stack height for array2 = $height"

# '出栈'就是: 
unset array2[${#array2[@]}-1]	#  数组从0开始索引, 
height=${#array2[@]}            #+ 这意味着第一个数组下标为0. 
echo
echo "POP"
echo "New stack height for array2 = $height"

ListArray

# 只列出数组array0的第二个和第三个元素.
from=1		# 从0开始索引. 
to=2		#
array3=( ${array0[@]:1:2} )
echo
echo "Elements in array3:  ${array3[@]}"

# 处理方式就像是字符串(字符数组). 
# 试试其他的"字符串"形式. 

# 替换: 
array4=( ${array0[@]/second/2nd} )
echo
echo "Elements in array4:  ${array4[@]}"

# 替换掉所有匹配通配符的字符串. 
array5=( ${array0[@]//new?/old} )
echo
echo "Elements in array5:  ${array5[@]}"

# 当你开始觉得对此有把握的时候 . . .
array6=( ${array0[@]#*new} )
echo # 这个可能会让你感到惊奇. 
echo "Elements in array6:  ${array6[@]}"

array7=( ${array0[@]#new1} )
echo # 数组array6之后就没有惊奇了. 
echo "Elements in array7:  ${array7[@]}"

# 看起来非常像 . . .
array8=( ${array0[@]/new1/} )
echo
echo "Elements in array8:  ${array8[@]}"

#  所以, 让我们怎么形容呢? 

#  对数组var[@]中的每个元素
#+ 进行连续的字符串操作. 
#  因此: 如果结果是长度为0的字符串, 
#+ Bash支持字符串向量操作, 
#+ 元素会在结果赋值中消失不见. 

#  一个问题, 这些字符串是强引用还是弱引用? 

zap='new*'
array9=( ${array0[@]/$zap/} )
echo
echo "Elements in array9:  ${array9[@]}"

# 当你还在考虑, 你身在Kansas州何处时 . . .
array10=( ${array0[@]#$zap} )
echo
echo "Elements in array10:  ${array10[@]}"

# 比较array7和array10. 
# 比较array8和array9. 

# 答案: 必须是弱引用. 

exit 0
