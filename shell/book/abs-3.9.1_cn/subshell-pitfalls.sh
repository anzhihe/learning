#!/bin/bash
# 子shell中的变量缺陷. 

outer_variable=outer
echo
echo "outer_variable = $outer_variable"
echo

(
# 开始子shell

echo "outer_variable inside subshell = $outer_variable"
inner_variable=inner  # Set
echo "inner_variable inside subshell = $inner_variable"
outer_variable=inner  # 会修改全局变量么? 
echo "outer_variable inside subshell = $outer_variable"

# 如果将变量'导出'会产生不同的结果么? 
#    export inner_variable
#    export outer_variable
# 试试看. 

# 结束子shell
)

echo
echo "inner_variable outside subshell = $inner_variable"  # 未设置. 
echo "outer_variable outside subshell = $outer_variable"  # 未修改. 
echo

exit 0

# 如果你打开第19和第20行的注释会怎样? 
# 会产生不同的结果么? (译者注: 小提示, 第18行的'导出'都加上引号了.)
