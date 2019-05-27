#!/bin/bash
# erase.sh: 在读取输入时使用"stty"来设置一个擦除字符. 

echo -n "What is your name? "
read name                      #  试试用退格键
                               #+ 来删除输入的字符. 
                               #  有什么问题? 
echo "Your name is $name."

stty erase '#'                 #  将"hashmark"(#)设置为退格字符. 
echo -n "What is your name? "
read name                      #  使用#来删除最后键入的字符. 
echo "Your name is $name."

# 警告: 即使在脚本退出后, 新的键值还是保持着这个设置. (译者: 可以使用stty erase '^?'进行恢复)

exit 0
