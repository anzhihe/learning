#!/bin/bash

# 间接变量引用. 
# 这种方法比较像C++中的引用特性. 


a=letter_of_alphabet
letter_of_alphabet=z

echo "a = $a"           # 直接引用. 

echo "Now a = ${!a}"    # 间接引用. 
# ${!variable}表示法比老式的"eval var1=\$$var2"表示法高级的多. 

echo

t=table_cell_3
table_cell_3=24
echo "t = ${!t}"                      # t = 24
table_cell_3=387
echo "Value of t changed to ${!t}"    # 387

#  在引用数组成员或者引用表的时候, 这种方法非常有用, 
#+ 还可以用来模拟多维数组. 
#  如果有能够索引的选项(类似于指针的算术运算)
#+ 就更好了. 可惜. 

exit 0
