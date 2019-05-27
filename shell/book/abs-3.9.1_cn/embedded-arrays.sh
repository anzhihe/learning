#!/bin/bash
# embedded-arrays.sh
# 嵌套数组和间接引用. 

# 本脚本由Dennis Leeuw编写. 
# 经过授权, 在本书中使用. 
# 本书作者做了少许修改. 


ARRAY1=(
        VAR1_1=value11
        VAR1_2=value12
        VAR1_3=value13
)

ARRAY2=(
        VARIABLE="test"
        STRING="VAR1=value1 VAR2=value2 VAR3=value3"
        ARRAY21=${ARRAY1[*]}
)       # 将ARRAY1嵌套到这个数组中. 

function print () {
        OLD_IFS="$IFS"
        IFS=$'\n'       #  这么做是为了每行
                        #+ 只打印一个数组元素.
        TEST1="ARRAY2[*]"
        local ${!TEST1} # 删除这一行, 看看会发生什么? 
        #  间接引用. 
	#  这使得$TEST1
	#+ 只能够在函数内被访问. 


        #  让我们看看还能干点什么. 
        echo
        echo "\$TEST1 = $TEST1"       #  仅仅是变量名字. 
        echo; echo
        echo "{\$TEST1} = ${!TEST1}"  #  变量内容. 
                                      #  这就是
                                      #+ 间接引用的作用. 
        echo
        echo "-------------------------------------------"; echo
        echo


        # 打印变量
        echo "Variable VARIABLE: $VARIABLE"
	
        # 打印一个字符串元素
        IFS="$OLD_IFS"
        TEST2="STRING[*]"
        local ${!TEST2}      # 间接引用(同上). 
        echo "String element VAR2: $VAR2 from STRING"

        # 打印一个数组元素
        TEST2="ARRAY21[*]"
        local ${!TEST2}      # 间接引用(同上). 
        echo "Array element VAR1_1: $VAR1_1 from ARRAY21"
}

print
echo

exit 0

#   脚本作者注, 
#+ "你可以很容易的将其扩展成一个能创建hash的Bash脚本." 
#   (难) 留给读者的练习: 实现它. 
