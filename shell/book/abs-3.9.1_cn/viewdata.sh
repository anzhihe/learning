#!/bin/bash
# viewdata.sh
# 转换自VIEWDATA.BAT的shell脚本. 

DATAFILE=/home/bozo/datafiles/book-collection.data
ARGNO=1

# @ECHO OFF                 这个命令在这里就不需要了. 

if [ $# -lt "$ARGNO" ]    # IF !%1==! GOTO VIEWDATA
then
  less $DATAFILE          # TYPE C:\MYDIR\BOOKLIST.TXT | MORE
else
  grep "$1" $DATAFILE     # FIND "%1" C:\MYDIR\BOOKLIST.TXT
fi  

exit 0                    # :EXIT0

#  跳转, 标签, 还有其他一些小手段, 在shell脚本中就不需要了. 
#  我们可以说, 转换后的脚本比原始批处理文件好的多, 
#+ 它更短, 看起来更整洁, 更优雅. 
