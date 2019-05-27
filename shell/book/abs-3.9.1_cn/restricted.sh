#!/bin/bash

#  脚本开头以"#!/bin/bash -r"来调用, 
#+ 会使整个脚本在受限模式下运行. 

echo

echo "Changing directory."
cd /usr/local
echo "Now in `pwd`"
echo "Coming back home."
cd
echo "Now in `pwd`"
echo

# 非受限的模式下，所有操作都正常. 

set -r
# set --restricted    也具有相同的效果. 
echo "==> Now in restricted mode. <=="

echo
echo

echo "Attempting directory change in restricted mode."
cd ..
echo "Still in `pwd`"

echo
echo

echo "\$SHELL = $SHELL"
echo "Attempting to change shell in restricted mode."
SHELL="/bin/ash"
echo
echo "\$SHELL= $SHELL"

echo
echo

echo "Attempting to redirect output in restricted mode."
ls -l /usr/bin > bin.files
ls -l bin.files    # 尝试列出刚才创建的文件. 

echo

exit 0
