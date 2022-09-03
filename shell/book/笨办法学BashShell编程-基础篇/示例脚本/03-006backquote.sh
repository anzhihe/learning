#!/bin/bash
# 本脚本的名称为：03-006backquote.sh
# 用于测试反引号backquote的命令替换commnad substitution功能

echo $0

script_name=`basename $0`
echo $script_name

script_name=`basename -s .sh $0`
echo $script_name
exit
