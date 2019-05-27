#!/bin/bash
# 还是行星.

# 用行星距太阳的距离来分配行星的名字.

for planet in "Mercury 36" "Venus 67" "Earth 93"  "Mars 142" "Jupiter 483"
do
  set -- $planet  # 解析变量"planet"并且设置位置参数. 
  # "--" 将防止$planet为空, 或者是以一个破折号开头. 

  # 可能需要保存原始的位置参数, 因为它们被覆盖了.
  # 一种方法就是使用数组.
  #        original_params=("$@")

  echo "$1		$2,000,000 miles from the sun"
  #-------two  tabs---把后边的0和2连接起来
done

# (感谢, S.C., 对此问题进行的澄清.)

exit 0
