#!/bin/bash
# func-cmdlinearg.sh
#  调用这个脚本, 并且带一个命令行参数. 
#+ 类似于 $0 arg1.


func ()

{
echo "$1"
}

echo "First call to function: no arg passed."
echo "See if command-line arg is seen."
func
# 不行! 命令行参数不可见. 

echo "============================================================"
echo
echo "Second call to function: command-line arg passed explicitly."
func $1
# 现在可见了! 

exit 0
