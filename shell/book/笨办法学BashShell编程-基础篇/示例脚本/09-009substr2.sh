#!/bin/bash
# 从不同方面方法获得符合条件的子字符串

stringZ=abcABC123ABCabc

# 方向1 从头部开始
echo `expr match "$stringZ" '\(.[b-c]*[A-Z]..[0-9]\)' `	# abcABC1
echo `expr "$stringZ" : '\(.[b-c]*[A-Z]..[0-9]\)' `	# abcABC1
echo `expr "$stringZ" : '\(.......\)' `			# abcABC1

# 方向2 从尾部开始
echo `expr match "$stringZ" '.*\([A-C][A-C][A-C][a-c]*\)' `	# ABCabc
echo `expr "$stringZ" : '.*\(......\)' `			# ABCabc
exit 0
