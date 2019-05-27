#!/bin/bash
# 使用命令替换来调用'bc'
# 并与'here document'相结合. 


var1=`bc << EOF
18.33 * 19.78
EOF
`
echo $var1       # 362.56


#  使用$( ... )这种标记法也可以. 
v1=23.53
v2=17.881
v3=83.501
v4=171.63

var2=$(bc << EOF
scale = 4
a = ( $v1 + $v2 )
b = ( $v3 * $v4 )
a * b + 15.35
EOF
)
echo $var2       # 593487.8452


var3=$(bc -l << EOF
scale = 9
s ( 1.7 )
EOF
)
# 返回弧度为1.7的正弦. 
# "-l"选项将会调用'bc'算数库. 
echo $var3       # .991664810


# 现在, 在函数中试一下...
hyp=             # 声明全局变量. 
hypotenuse ()    # 计算直角三角形的斜边. 
{
hyp=$(bc -l << EOF
scale = 9
sqrt ( $1 * $1 + $2 * $2 )
EOF
)
# 不幸的是, 不能从bash函数中返回浮点值. 
}

hypotenuse 3.68 7.31
echo "hypotenuse = $hyp"    # 8.184039344


exit 0
