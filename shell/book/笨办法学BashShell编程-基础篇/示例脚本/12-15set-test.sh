#!/bin/bash

# 需要给本脚本传递三个参数

echo "Positional parameters before set \`uname -a\` :"
echo "Commnad-line argument #1 = $1"
echo "Commnad-line argument #2 = $2"
echo "Commnad-line argument #3 = $3"

set `uname -a`

echo

echo "Positional parameters after set \`uname -a\` :"
echo "Fileld #1 of 'uname -a'  = $1"
echo "Fileld #2 of 'uname -a'  = $2"
echo "Fileld #3 of 'uname -a'  = $3"

exit 0
