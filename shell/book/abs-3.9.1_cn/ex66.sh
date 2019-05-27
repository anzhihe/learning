#!/bin/bash


area[11]=23
area[13]=37
area[51]=UFOs

#  数组成员不一定非得是相邻或连续的. 

#  数组的部分成员可以不被初始化. 
#  数组中允许空缺元素. 
#  实际上, 保存着稀疏数据的数组("稀疏数组")
#+ 在电子表格处理软件中是非常有用的. 


echo -n "area[11] = "
echo ${area[11]}    #  需要{大括号}. 

echo -n "area[13] = "
echo ${area[13]}

echo "Contents of area[51] are ${area[51]}."

# 没被初始化的数组成员打印为空值(null变量). 
echo -n "area[43] = "
echo ${area[43]}
echo "(area[43] unassigned)"

echo

# 两个数组元素的和被赋值给另一个数组元素
area[5]=`expr ${area[11]} + ${area[13]}`
echo "area[5] = area[11] + area[13]"
echo -n "area[5] = "
echo ${area[5]}

area[6]=`expr ${area[11]} + ${area[51]}`
echo "area[6] = area[11] + area[51]"
echo -n "area[6] = "
echo ${area[6]}
# 这里会失败, 是因为不允许整数与字符串相加. 

echo; echo; echo

# -----------------------------------------------------------------
# 另一个数组, "area2".
# 另一种给数组变量赋值的方法...
# array_name=( XXX YYY ZZZ ... )

area2=( zero one two three four )

echo -n "area2[0] = "
echo ${area2[0]}
# 阿哈, 从0开始计算数组下标(也就是数组的第一个元素为[0], 而不是[1]). 

echo -n "area2[1] = "
echo ${area2[1]}    # [1]是数组的第2个元素. 
# -----------------------------------------------------------------

echo; echo; echo

# -----------------------------------------------
# 第3个数组, "area3".
# 第3种给数组元素赋值的方法...
# array_name=([xx]=XXX [yy]=YYY ...)

area3=([17]=seventeen [24]=twenty-four)

echo -n "area3[17] = "
echo ${area3[17]}

echo -n "area3[24] = "
echo ${area3[24]}
# -----------------------------------------------

exit 0
