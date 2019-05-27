#!/bin/sh

# -->  本书作者所做的注释全部以"# -->"开头. 

# --> 这是由Miquel van Smoorenburg所编写的
# --> 'rc'脚本包的一部分, &lt;miquels@drinkel.nl.mugnet.org>.

# --> 这个特殊的脚本看起来是Red Hat/FC专用的, 
# --> (在其它的发行版中可能不会出现). 

#  停止所有正在运行的不必要的服务
#+ (不会有多少, 所以这是个合理性检查)

for i in /var/lock/subsys/*; do
        # --> 标准的for/in循环, 但是由于"do"在同一行上, 
        # --> 所以必须添加";". 
        # 检查脚本是否在那里. 
        [ ! -f $i ] && continue
        # --> 这是一种使用"与列表"的聪明方法, 等价于: 
        # --> if [ ! -f "$i" ]; then continue

        # 取得子系统的名字. 
        subsys=${i#/var/lock/subsys/}
        # --> 匹配变量名, 在这里就是文件名. 
        # --> 与subsys=`basename $i`完全等价. 
	
        # -->  从锁定文件名中获得
        # -->+ (如果那里有锁定文件的话, 
        # -->+ 那就证明进程正在运行). 
        # -->  参考一下上边所讲的"锁定文件"的内容. 


        # 终止子系统. 
        if [ -f /etc/rc.d/init.d/$subsys.init ]; then
           /etc/rc.d/init.d/$subsys.init stop
        else
           /etc/rc.d/init.d/$subsys stop
        # -->  挂起运行的作业和幽灵进程. 
        # -->  注意"stop"只是一个位置参数, 
        # -->+ 并不是shell内建命令. 
        fi
done
