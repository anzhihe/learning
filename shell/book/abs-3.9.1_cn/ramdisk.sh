#!/bin/bash
# ramdisk.sh

#  一个"ramdisk"就是系统RAM内存中的一部分, 
#+ 只不过它被当作文件系统来操作. 
#  它的优点是访问速度非常快(读/写时间快). 
#  缺点: 易失性, 当机器重启或关机时, 会丢失数组. 
#+                而且会减少系统可用的RAM. 
#
#  那么ramdisk有什么用呢? 
#  保存一个大数据集, 比如保存表格或字典. 
#+ 这样的话, 可以增加查询速度, 因为访问内存比访问硬盘快得多. 


E_NON_ROOT_USER=70             # 必须以root身份来运行. 
ROOTUSER_NAME=root

MOUNTPT=/mnt/ramdisk
SIZE=2000                      # 2K个块(可以进行适当的修改)
BLOCKSIZE=1024                 # 每块的大小为1K(1024字节)
DEVICE=/dev/ram0               # 第一个ram设备

username=`id -nu`
if [ "$username" != "$ROOTUSER_NAME" ]
then
  echo "Must be root to run \"`basename $0`\"."
  exit $E_NON_ROOT_USER
fi

if [ ! -d "$MOUNTPT" ]         #  测试挂载点是否已经存在, 
then                           #+ 如果做了这个判断的话, 当脚本运行多次的时候, 
  mkdir $MOUNTPT               #+ 就不会报错了. (译者注: 主要是为了避免多次创建目录.)
fi

dd if=/dev/zero of=$DEVICE count=$SIZE bs=$BLOCKSIZE  # 把RAM设备的内容用0填充. 
                                                      # 为什么必须这么做? 
mke2fs $DEVICE                 # 在RAM上创建一个ext2文件系统. 
mount $DEVICE $MOUNTPT         # 挂载上. 
chmod 777 $MOUNTPT             # 使一般用户也可以访问这个ramdisk. 
                               # 然而, 只能使用root身份来卸载它. 

echo "\"$MOUNTPT\" now available for use."
# 现在ramdisk就可以访问了, 即使是普通用户也可以访问. 

#  小心, ramdisk存在易失性, 
#+ 如果重启或关机的话, 保存的内容就会消失. 
#  所以, 还是要将你想保存的文件, 保存到常规磁盘目录下. 

# 重启之后, 运行这个脚本, 将会再次建立一个ramdisk. 
# 如果你仅仅重新加载/mnt/ramdisk, 而没有运行其他步骤的话, 那就不会正常工作. 

#  如果对这个脚本进行适当的改进, 就可以将其放入/etc/rc.d/rc.local中, 
#+ 这样, 在系统启动的时候就会自动建立一个ramdisk. 
#  这么做非常适合于那些对速度要求很高的数据库服务器. 

exit 0
