#!/bin/bash
# unalias.sh

shopt -s expand_aliases  # 启用别名扩展. 

alias llm='ls -al | more'
llm

echo

unalias llm              # 删除别名.
llm
# 产生错误信息, 因为'llm'已经不再有效了. 

exit 0
