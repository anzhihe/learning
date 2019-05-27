#!/bin/bash
# 练习'date'命令

echo "The number of days since the year's beginning is `date +%j`."
# 需要在调用格式的前边加上一个'+'号.
# %j用来给出今天是本年度的第几天. 

echo "The number of seconds elapsed since 01/01/1970 is `date +%s`."
#  %s将产生从"UNIX 元年"到现在为止的秒数,
#+ 但是这东西现在还有用么?

prefix=temp
suffix=$(date +%s)  # 'date'命令的"+%s"选项是GNU特性.
filename=$prefix.$suffix
echo $filename
#  这是一种非常好的产生"唯一"临时文件的办法,
#+ 甚至比使用$$都强.

# 如果想了解'date'命令的更多选项, 请查阅这个命令的man页.

exit 0
