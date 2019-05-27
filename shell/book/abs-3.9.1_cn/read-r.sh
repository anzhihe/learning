#!/bin/bash

echo

echo "Enter a string terminated by a \\, then press &lt;ENTER&gt;."
echo "Then, enter a second string, and again press &lt;ENTER&gt;."
read var1     # 当 read $var1 时, "\" 将会阻止产生新行. 
              #     first line \
              #     second line

echo "var1 = $var1"
#     var1 = first line second line

#  对于每个以 "\" 结尾的行, 
#+ 你都会看到一个下一行的提示符, 让你继续向var1输入内容.

echo; echo

echo "Enter another string terminated by a \\ , then press &lt;ENTER&gt;."
read -r var2  # -r 选项会让 "\" 转义.
              #     first line \

echo "var2 = $var2"
#     var2 = first line \

# 第一个 &lt;ENTER&gt; 就会结束var2变量的录入.

echo 

exit 0
