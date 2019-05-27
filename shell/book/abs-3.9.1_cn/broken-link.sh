#!/bin/bash
# broken-link.sh
# 由Lee bigelow所编写 &lt;ligelowbee@yahoo.com&gt;
# 已经争得作者的授权引用在本书中.

#一个纯粹的shell脚本用来找出那些断掉的符号链接文件并且输出它们所指向的文件.
#以便于它们可以把输出提供给xargs来进行处理 :)
#比如. broken-link.sh /somedir /someotherdir|xargs rm
#
#下边的方法, 不管怎么说, 都是一种更好的办法:
#
#find "somedir" -type l -print0|\
#xargs -r0 file|\
#grep "broken symbolic"|
#sed -e 's/^\|: *broken symbolic.*$/"/g'
#
#但这不是一个纯粹的bash脚本, 最起码现在不是.
#注意: 谨防在/proc文件系统和任何死循环链接中使用!
##############################################################


#如果没有参数被传递到脚本中, 那么就使用
#当前目录. 否则就是用传递进来的参数作为目录
#来搜索.
####################
[ $# -eq 0 ] && directorys=`pwd` || directorys=$@

#编写函数linkchk用来检查传递进来的目录或文件是否是链接, 
#并判断这些文件或目录是否存在. 然后打印它们所指向的文件.
#如果传递进来的元素包含子目录, 
#那么把子目录也放到linkcheck函数中处理, 这样就达到了递归的目的.
##########
linkchk () {
    for element in $1/*; do
    [ -h "$element" -a ! -e "$element" ] && echo \"$element\"
    [ -d "$element" ] && linkchk $element
    # 当然, '-h'用来测试符号链接, '-d'用来测试目录.
    done
}

#把每个传递到脚本的参数都送到linkchk函数中进行处理, 
#检查是否有可用目录. 如果没有, 那么就打印错误消息和
#使用信息.
################
for directory in $directorys; do
    if [ -d $directory ]
	then linkchk $directory
	else 
	    echo "$directory is not a directory"
	    echo "Usage: $0 dir1 dir2 ..."
    fi
done

exit 0
