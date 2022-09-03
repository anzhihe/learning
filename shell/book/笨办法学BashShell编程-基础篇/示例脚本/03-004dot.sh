#!/bin/bash
# 点 命令测试，点命令与source命令效果相同

. 03-004dot.txt  # 加载一个数据文件
# 这与 source 03-004dot.txt  效果相同
# 03-004dot.txt 必须存在于当前的工作目录

# 下面，引用数据文件中定义的一个变量
echo D1

exit
