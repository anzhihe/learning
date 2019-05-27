#!/bin/bash

#  这个脚本的目的是删除当前目录下的某些文件, 
#+ 这些文件特指那些文件名包含空格的文件. 
#  但是不能如我们所愿的那样工作. 
#  为什么? 


badname=`ls | grep ' '`

# 试试这个: 
# echo "$badname"

rm "$badname"

exit 0
