#!/bin/bash
# hello.sh: 显示"hello"还是"goodbye"
#+          依赖于脚本是如何被调用的. 

# 在当前目录下($PWD)为这个脚本创建一个链接:
#    ln -s hello.sh goodbye
# 现在, 通过如下两种方法来调用这个脚本:
# ./hello.sh
# ./goodbye


HELLO_CALL=65
GOODBYE_CALL=66

if [ $0 = "./goodbye" ]
then
  echo "Good-bye!"
  # 当然, 在这里你也可以添加一些其他的goodbye类型的命令.
  exit $GOODBYE_CALL
fi

echo "Hello!"
# 当然, 在这里你也可以添加一些其他的hello类型的命令.
exit $HELLO_CALL
