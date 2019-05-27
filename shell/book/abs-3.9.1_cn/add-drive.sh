#!/bin/bash

# 在系统上添加第二块硬盘驱动器. 
# 软件配置. 假设硬件已经安装了. 
# 来自于本书作者的一篇文章. 
# 在"Linux Gazette"的问题#38上, http://www.linuxgazette.com. 

ROOT_UID=0     # 这个脚本必须以root身份运行. 
E_NOTROOT=67   # 非root用户将会产生这个错误. 

if [ "$UID" -ne "$ROOT_UID" ]
then
  echo "Must be root to run this script."
  exit $E_NOTROOT
fi  

# 要非常谨慎小心的使用! 
# 如果某步错了, 可能会彻底摧毁你当前的文件系统. 


NEWDISK=/dev/hdb         # 假设/dev/hdb空白. 检查一下!
MOUNTPOINT=/mnt/newdisk  #或者选择其他的mount入口. 


fdisk $NEWDISK
mke2fs -cv $NEWDISK1   # 检查坏块, 并且详细输出. 
#  注意:    /dev/hdb1, *不是* /dev/hdb!
mkdir $MOUNTPOINT
chmod 777 $MOUNTPOINT  # 让所有用户都具有全部权限. 


# 现在, 测试一下...
# mount -t ext2 /dev/hdb1 /mnt/newdisk
# 尝试创建一个目录. 
# 如果运行起来了, umount它, 然后继续. 

# 最后一步:
# 将下边这行添加到/etc/fstab.
# /dev/hdb1  /mnt/newdisk  ext2  defaults  1 1

exit 0
