#!/bin/bash
#
#  将当前目录下的所有文全部转换为小写. 
#                                      
#  灵感来自于John Dubois的脚本, 
#+ Chet Ramey将其转换为Bash脚本, 
#+ 然后被本书作者精简了一下. 


for filename in *                # 遍历当前目录下的所有文件. 
do                                                                         
   fname=`basename $filename`                                              
   n=`echo $fname | tr A-Z a-z`  # 将名字修改为小写. 
   if [ "$fname" != "$n" ]       # 只对那些文件名不是小写的文件进行重命名. 
   then
     mv $fname $n
   fi  
done   

exit $?


# 下边的代码将不会被执行, 因为上边的"exit". 
#-------------------------------------------#
# 删除上边的内容, 来运行下边的内容. 
                                                                
# 对于那些文件名中包含空白和新行的文件, 上边的脚本就不能工作了. 
# Stephane Chazelas因此建议使用下边的方法: 


for filename in *    # 不必非得使用basename命令, 
                     # 因为"*"不会返回任何包含"/"的文件. 
do n=`echo "$filename/" | tr '[:upper:]' '[:lower:]'`
#                             POSIX 字符集标记法.
#                    添加的斜线是为了在文件名结尾换行不会被
#                    命令替换删掉. 
   # 变量替换:
   n=${n%/}          # 从文件名中将上边添加在结尾的斜线删除掉. 
   [[ $filename == $n ]] || mv "$filename" "$n"
                     # 检查文件名是否已经是小写. 
done

exit $?
