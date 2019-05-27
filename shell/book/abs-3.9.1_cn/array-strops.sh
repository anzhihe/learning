#!/bin/bash
# array-strops.sh: 用于数组的字符串操作. 
# 本脚本由Michael Zick所编写. 
# 授权使用在本书中. 

#  一般来说, 任何类似于${name ... }(这种形式)的字符串操作
#+ 都能够应用于数组中的所有字符串元素, 
#+ 比如说${name[@] ... }或${name[*] ...}这两种形式. 


arrayZ=( one two three four five five )

echo

# 提取尾部的子串
echo ${arrayZ[@]:0}     # one two three four five five
                        # 所有元素. 

echo ${arrayZ[@]:1}     # two three four five five
                        # element[0]后边的所有元素. 

echo ${arrayZ[@]:1:2}   # two three
                        # 只提取element[0]后边的两个元素. 

echo "-----------------------"

#  子串删除
#  从字符串的开头删除最短的匹配, 
#+ 匹配的子串也可以是正则表达式. 

echo ${arrayZ[@]#f*r}   # one two three five five
                        # 匹配将应用于数组的所有元素. 
                        # 匹配到了"four", 并且将它删除. 

# 从字符串的开头删除最长的匹配
echo ${arrayZ[@]##t*e}  # one two four five five
                        # 匹配将应用于数组的所有元素. 
                        # 匹配到了"three", 并且将它删除. 

# 从字符串的结尾删除最短的匹配
echo ${arrayZ[@]%h*e}   # one two t four five five
                        # 匹配将应用于数组的所有元素. 
                        # 匹配到了"hree", 并且将它删除. 

# 从字符串的结尾删除最长的匹配
echo ${arrayZ[@]%%t*e}  # one two four five five
                        # 匹配将应用于数组的所有元素. 
                        # 匹配到了"three", 并且将它删除. 

echo "-----------------------"

# 子串替换

# 第一个匹配到的子串将会被替换
echo ${arrayZ[@]/fiv/XYZ}   # one two three four XYZe XYZe
                            # 匹配将应用于数组的所有元素. 

# 所有匹配到的子串都会被替换
echo ${arrayZ[@]//iv/YY}    # one two three four fYYe fYYe
                            # 匹配将应用于数组的所有元素. 

# 删除所有的匹配子串
# 如果没有指定替换字符串的话, 那就意味着'删除'
echo ${arrayZ[@]//fi/}      # one two three four ve ve
                            # 匹配将应用于数组的所有元素. 

# 替换字符串前端子串
echo ${arrayZ[@]/#fi/XY}    # one two three four XYve XYve
                            # 匹配将应用于数组的所有元素. 

# 替换字符串后端子串
echo ${arrayZ[@]/%ve/ZZ}    # one two three four fiZZ fiZZ
                            # 匹配将应用于数组的所有元素. 

echo ${arrayZ[@]/%o/XX}     # one twXX three four five five
                            # 为什么? 

echo "-----------------------"


# 在将处理后的结果发送到awk(或者其他的处理工具)之前 --
# 回忆一下:
#   $( ... )是命令替换. 
#   函数作为子进程运行. 
#   函数结果输出到stdout. 
#   用read来读取函数的stdout. 
#   使用name[@]表示法指定了一个"for-each"操作. 

newstr() {
    echo -n "!!!"
}

echo ${arrayZ[@]/%e/$(newstr)}
# on!!! two thre!!! four fiv!!! fiv!!!
# Q.E.D: 替换动作实际上是一个'赋值'. 

#  使用"For-Each"形式的
echo ${arrayZ[@]//*/$(newstr optional_arguments)}
#  现在, 如果Bash只将匹配到的子串作为$0
#+ 传递给将被调用的函数 . . .

echo

exit 0
