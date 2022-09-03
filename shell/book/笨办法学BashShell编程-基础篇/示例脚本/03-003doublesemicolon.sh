#!/bin/bash
# 双分号 double semicolon 示例

variable='abc'

case "$variable" in
abc) echo "\$variable = abc";;
xyz) echo "\$variable = xyz";;
esac
