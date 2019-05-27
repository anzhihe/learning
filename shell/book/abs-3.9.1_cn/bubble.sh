#!/bin/bash
# bubble.sh: 一种排序方式, 冒泡排序. 

# 回忆一下冒泡排序的算法. 我们在这里要实现它...

#  依靠连续的比较数组元素进行排序, 
#+ 比较两个相邻元素, 如果顺序不对, 就交换这两个元素的位置. 
#  当第一轮比较结束之后, 最"重"的元素就会被移动到最底部. 
#  当第二轮比较结束之后, 第二"重"的元素就会被移动到次底部的位置. 
#  依此类推. 
#  这意味着每轮比较不需要比较之前已经"沉淀"好的数据. 
#  因此你会注意到后边的数据在打印的时候会快一些. 


exchange()
{
  # 交换数组中的两个元素. 
  local temp=${Countries[$1]} #  临时保存
                              #+ 要交换的那个元素. 
  Countries[$1]=${Countries[$2]}
  Countries[$2]=$temp
  
  return
}  

declare -a Countries  #  声明数组, 
                      #+ 此处是可选的, 因为数组在下面被初始化. 

#  我们是否可以使用转义符(\)
#+ 来将数组元素的值放在不同的行上? 
#  可以. 

Countries=(Netherlands Ukraine Zaire Turkey Russia Yemen Syria \
Brazil Argentina Nicaragua Japan Mexico Venezuela Greece England \
Israel Peru Canada Oman Denmark Wales France Kenya \
Xanadu Qatar Liechtenstein Hungary)

# "Xanadu"虚拟出来的世外桃源. 
#+ 


clear                      # 开始之前的清屏动作. 

echo "0: ${Countries[*]}"  # 从索引0开始列出整个数组. 

number_of_elements=${#Countries[@]}
let "comparisons = $number_of_elements - 1"

count=1 # 传递数字. 

while [ "$comparisons" -gt 0 ]          # 开始外部循环
do

  index=0  # 在每轮循环开始之前, 重置索引. 

  while [ "$index" -lt "$comparisons" ] # 开始内部循环
  do
    if [ ${Countries[$index]} \> ${Countries[`expr $index + 1`]} ]
    #  如果原来的排序次序不对...
    #  回想一下, 在单括号中, 
    #+ \>是ASCII码的比较操作符. 

    #  if [[ ${Countries[$index]} > ${Countries[`expr $index + 1`]} ]]
    #+ 这样也行. 
    then
      exchange $index `expr $index + 1`  # 交换. 
    fi  
    let "index += 1"  # 或者,   index+=1   在Bash 3.1之后的版本才能这么用. 
  done # 内部循环结束

# ----------------------------------------------------------------------
# Paulo Marcel Coelho Aragao建议我们可以使用更简单的for循环. 
#
# for (( last = $number_of_elements - 1 ; last > 1 ; last-- ))
# do
#     for (( i = 0 ; i < last ; i++ ))
#     do
#         [[ "${Countries[$i]}" > "${Countries[$((i+1))]}" ]] \
#             && exchange $i $((i+1))
#     done
# done
# ----------------------------------------------------------------------
  

let "comparisons -= 1" #  因为最"重"的元素到了底部, 
                       #+ 所以每轮我们可以少做一次比较. 

echo
echo "$count: ${Countries[@]}"  # 每轮结束后, 都打印一次数组. 
echo
let "count += 1"                # 增加传递计数. 

done                            # 外部循环结束
                                # 至此, 全部完成. 

exit 0
