#!/bin/bash

E_WRONG_DIRECTORY=73

clear # 清屏.

TargetDirectory=/home/bozo/projects/GreatAmericanNovel

cd $TargetDirectory
echo "Deleting stale files in $TargetDirectory."

if [ "$PWD" != "$TargetDirectory" ]
then    # 防止偶然删错目录.
  echo "Wrong directory!"
  echo "In $PWD, rather than $TargetDirectory!"
  echo "Bailing out!"
  exit $E_WRONG_DIRECTORY
fi  

rm -rf *
rm .[A-Za-z0-9]*    # 删除点文件(译者注: 隐藏文件). 
# rm -f .[^.]* ..?*   为了删除以多个点开头的文件. 
# (shopt -s dotglob; rm -f *)   也可以.
# 感谢, S.C. 指出这点.

# 文件名可以包含ascii中0 - 255范围内的所有字符, 除了"/".
# 删除以各种诡异字符开头的文件将会作为一个练习留给大家.

# 如果必要的话, 这里预留给其他操作.

echo
echo "Done."
echo "Old files deleted in $TargetDirectory."
echo


exit 0
