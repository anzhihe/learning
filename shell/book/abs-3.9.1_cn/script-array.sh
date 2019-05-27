#!/bin/bash
# script-array.sh: 将这个脚本的内容赋值给数组. 
# 这个脚本的灵感来自于Chris Martin的e-mail(感谢!). 

script_contents=( $(cat "$0") )  #  将这个脚本的内容($0)
                                 #+ 赋值给数组. 

for element in $(seq 0 $((${#script_contents[@]} - 1)))
  do                #  ${#script_contents[@]}
                    #+ 表示数组元素的个数. 
                    #
                    #  一个小问题:
                    #  为什么必须使用seq 0? 
                    #  用seq 1来试一下. 
  echo -n "${script_contents[$element]}"
                    # 在同一行上显示脚本中每个域的内容. 
  echo -n " -- "    # 使用 " -- " 作为域分割符. 
done

echo

exit 0

# 练习:
# -----
#  修改这个脚本, 
#+ 让这个脚本能够按照它原本的格式输出, 
#+ 连同空白, 换行, 等等. 
