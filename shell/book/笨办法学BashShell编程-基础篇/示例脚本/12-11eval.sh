#!/bin/bash

# 练习1：基本使用
y=`eval ls /tmp -l`
echo $y
echo
echo "$y"

echo; echo

# 练习2：获得版本信息中的主版本号和次版本号
version=3.4
echo "version = $version"

eval major=${version/./;minor=}
# 将. 替换为 ;minor= 也就是 3;minor=4
# 这相当于执行 major=3;minor=4

echo "Major: $major, Minor: $minor"

exit 0
