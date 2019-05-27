#!/bin/bash
# resistor-inventory.sh
# 使用间接变量引用的简单数据库应用. 

# ============================================================== #
# 数据

B1723_value=470                                   # 欧姆
B1723_powerdissip=.25                             # 瓦特
B1723_colorcode="yellow-violet-brown"             # 颜色
B1723_loc=173                                     # 位置
B1723_inventory=78                                # 数量

B1724_value=1000
B1724_powerdissip=.25
B1724_colorcode="brown-black-red"
B1724_loc=24N
B1724_inventory=243

B1725_value=10000
B1725_powerdissip=.25
B1725_colorcode="brown-black-orange"
B1725_loc=24N
B1725_inventory=89

# ============================================================== #


echo

PS3='Enter catalog number: '

echo

select catalog_number in "B1723" "B1724" "B1725"
do
  Inv=${catalog_number}_inventory
  Val=${catalog_number}_value
  Pdissip=${catalog_number}_powerdissip
  Loc=${catalog_number}_loc
  Ccode=${catalog_number}_colorcode

  echo
  echo "Catalog number $catalog_number:"
  echo "There are ${!Inv} of [${!Val} ohm / ${!Pdissip} watt] resistors in stock."
  echo "These are located in bin # ${!Loc}."
  echo "Their color code is \"${!Ccode}\"."

  break
done

echo; echo

# 练习:
# -----
# 1) 重写脚本, 使其从外部文件读取数据. 
# 2) 重写脚本, 
#+   用数组来代替间接变量引用, 
#    因为使用数组更简单, 更易懂. 


# 注:
# ---
#  除了最简单的数据库应用, 事实上, Shell脚本本身并不适合于数据库应用. 
#+ 因为它太依赖于工作环境和机器的运算能力. 
#  更好的办法还是使用支持数据结构的本地语言, 
#+ 比如C++或者Java(或者甚至可以是Perl). 

exit 0
