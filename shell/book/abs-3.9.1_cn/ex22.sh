#!/bin/bash
# 列出所有的行星名称. (译者注: 现在的太阳系行星已经有了变化^_^)

for planet in Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune Pluto
do
  echo $planet  # 每个行星都被单独打印在一行上.
done

echo

for planet in "Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune Pluto"
# 所有的行星名称都打印在同一行上.
# 整个'list'都被双引号封成了一个变量. 
do
  echo $planet
done

exit 0
