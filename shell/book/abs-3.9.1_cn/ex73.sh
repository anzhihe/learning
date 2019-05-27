#!/bin/bash
# 创建一个交换文件. 

ROOT_UID=0         # Root用户的$UID为0. 
E_WRONG_USER=65    # 不是root?

FILE=/swap
BLOCKSIZE=1024
MINBLOCKS=40
SUCCESS=0


# 这个脚本必须以root身份来运行. 
if [ "$UID" -ne "$ROOT_UID" ]
then
  echo; echo "You must be root to run this script."; echo
  exit $E_WRONG_USER
fi  
  

blocks=${1:-$MINBLOCKS}          #  如果没在命令行上指定, 
                                 #+ 默认设置为40块. 
# 上边这句等价于下面这个命令块. 
# --------------------------------------------------
# if [ -n "$1" ]
# then
#   blocks=$1
# else
#   blocks=$MINBLOCKS
# fi
# --------------------------------------------------


if [ "$blocks" -lt $MINBLOCKS ]
then
  blocks=$MINBLOCKS              # 至少要有40块. 
fi  


echo "Creating swap file of size $blocks blocks (KB)."
dd if=/dev/zero of=$FILE bs=$BLOCKSIZE count=$blocks  # 用零填充文件. 

mkswap $FILE $blocks             # 将其指定为交换文件(译者注: 或称为交换分区). 
swapon $FILE                     # 激活交换文件. 

echo "Swap file created and activated."

exit $SUCCESS
