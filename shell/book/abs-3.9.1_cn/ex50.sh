#!/bin/bash

WIDTH=40                    # 设为40列宽. 

b=`ls /usr/local/bin`       # 取得文件列表...

echo $b | fmt -w $WIDTH

# 也可以使用如下方法, 作用是相同的.
#    echo $b | fold - -s -w $WIDTH
 
exit 0
