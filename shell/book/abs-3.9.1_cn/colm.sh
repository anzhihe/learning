#!/bin/bash
# 这是"column" man页中的一个例子, 作者对这个例子做了很小的修改. 


(printf "PERMISSIONS LINKS OWNER GROUP SIZE MONTH DAY HH:MM PROG-NAME\n" \
; ls -l | sed 1d) | column -t

#  管道中的"sed 1d"删除输出的第一行, 
#+ 第一行将是"total        N", 
#+ 其中"N"是"ls -l"找到的文件总数. 
                                                   
# "column"中的-t选项用来转化为易于打印的表形式. 

exit 0
