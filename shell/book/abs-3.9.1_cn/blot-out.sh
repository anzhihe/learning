#!/bin/bash
# blot-out.sh: 删除一个文件"所有"的记录. 

#  这个脚本会使用随机字节交替的覆盖目标文件, 
#+ 并且在最终删除这个文件之前清零.
#  这么做之后, 即使你通过传统手段来检查磁盘扇区
#+ 也不能把文件原始数据重新恢复.

PASSES=7         #  破坏文件的次数. 
                 #  提高这个数字会减慢脚本运行的速度, 
                 #+ 尤其是对尺寸比较大的目标文件进行操作的时候. 
BLOCKSIZE=1      #  带有/dev/urandom的I/O需要单位块尺寸, 
                 #+ 否则你可能会获得奇怪的结果. 
E_BADARGS=70     #  不同的错误退出码. 
E_NOT_FOUND=71
E_CHANGED_MIND=72

if [ -z "$1" ]   # 没指定文件名. 
then
  echo "Usage: `basename $0` filename"
  exit $E_BADARGS
fi

file=$1

if [ ! -e "$file" ]
then
  echo "File \"$file\" not found."
  exit $E_NOT_FOUND
fi  

echo; echo -n "Are you absolutely sure you want to blot out \"$file\" (y/n)? "
read answer
case "$answer" in
[nN]) echo "Changed your mind, huh?"
      exit $E_CHANGED_MIND
      ;;
*)    echo "Blotting out file \"$file\".";;
esac


flength=$(ls -l "$file" | awk '{print $5}')  # 5是文件长度. 
pass_count=1

chmod u+w "$file"   # 允许覆盖/删除这个文件. 

echo

while [ "$pass_count" -le "$PASSES" ]
do
  echo "Pass #$pass_count"
  sync         # 刷新buffers.
  dd if=/dev/urandom of=$file bs=$BLOCKSIZE count=$flength
               # 使用随机字节进行填充. 
  sync         # 再次刷新buffer. 
  dd if=/dev/zero of=$file bs=$BLOCKSIZE count=$flength
               # 用0填充. 
  sync         # 再次刷新buffer. 
  let "pass_count += 1"
  echo
done  


rm -f $file    # 最后, 删除这个已经被破坏得不成样子的文件.
sync           # 最后一次刷新buffer.

echo "File \"$file\" blotted out and deleted."; echo


exit 0

#  这是一种真正安全的删除文件的办法,
#+ 但是效率比较低, 运行比较慢.
#  GNU文件工具包中的"shred"命令,
#+ 也可以完成相同的工作, 不过更有效率.
                                                            
#  使用普通的方法是不可能重新恢复这个文件了.
#  然而 . . .
#+ 这个简单的例子是不能够抵抗
#+ 那些经验丰富并且正规的分析.
                                                            
#  这个脚本可能不会很好的运行在日志文件系统上(JFS).
#  练习 (很难): 像它做的那样修正这个问题.



#  Tom Vier的文件删除包可以更加彻底的删除文件, 
#+ 比这个例子厉害的多. 
#     http://www.ibiblio.org/pub/Linux/utils/file/wipe-2.0.0.tar.bz2

#  如果想对安全删除文件这一论题进行深入的分析,
#+ 可以参见Peter Gutmann的网页,
#+     "Secure Deletion of Data From Magnetic and Solid-State Memory".
#       http://www.cs.auckland.ac.nz/~pgut001/pubs/secure_del.html
