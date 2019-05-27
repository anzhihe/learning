#!/bin/bash
# idelete.sh: 通过文件的inode号来删除文件.

#  当文件名以一个非法字符开头的时候, 这就非常有用了,
#+ 比如 ? 或 -.

ARGCOUNT=1                      # 文件名参数必须被传递到脚本中.
E_WRONGARGS=70
E_FILE_NOT_EXIST=71
E_CHANGED_MIND=72

if [ $# -ne "$ARGCOUNT" ]
then
  echo "Usage: `basename $0` filename"
  exit $E_WRONGARGS
fi  

if [ ! -e "$1" ]
then
  echo "File \""$1"\" does not exist."
  exit $E_FILE_NOT_EXIST
fi  

inum=`ls -i | grep "$1" | awk '{print $1}'`
# inum = inode 文件的(索引节点)号.
# --------------------------------------------------------
# 每个文件都有一个inode号, 这个号用来记录文件物理地址信息.
# --------------------------------------------------------

echo; echo -n "Are you absolutely sure you want to delete \"$1\" (y/n)? "
# 'rm' 命令的 '-v' 选项得询问也会出现这句话.
read answer
case "$answer" in
[nN]) echo "Changed your mind, huh?"
      exit $E_CHANGED_MIND
      ;;
*)    echo "Deleting file \"$1\".";;
esac

find . -inum $inum -exec rm {} \;
#                           ^^
#        大括号就是"find"命令
#+       用来替换文本输出的地方.
echo "File "\"$1"\" deleted!"

exit 0
