#!/bin/bash
# "Reading" 变量.

echo -n "Enter the value of variable 'var1': "
# -n 选项, 阻止换行.

read var1
# 注意: 在var1前面没有'$', 因为变量正在被设置. 

echo "var1 = $var1"


echo

# 一个单独的'read'语句可以设置多个变量. 
echo -n "Enter the values of variables 'var2' and 'var3' (separated by a space or tab): "
read var2 var3
echo "var2 = $var2      var3 = $var3"
# 如果你只输入了一个值, 那么其他的变量还是处于未设置状态(null). 

exit 0
