#!/bin/bash
# 快速获得系统信息的脚本

# 检查互联网连接
ping -c 1 www.baidu.com &> /dev/null && echo "Internet: Connected" || echo "Internet: Disconnected"

# OS类型
os=$(uname -o) 	# -o, --operating-system   print the operating system
echo "Operating System Type : " $os

# 操作系统发行名称与版本号
# 这个版本比较粗糙，在CentOS 7写的，没有针对其它发行版本做适配
echo -n "OS Name : "    $(cat /etc/os-release | grep "^NAME=" | cut -f 2 -d\")
echo -n "OS Version : " $(cat /etc/os-release | grep "^VERSION=" | cut -f 2 -d\")

# 架构
echo "Architecture : " $(uname -m)

# 内核
echo "Kernel Release: " $(uname -r)

# 架构
echo "Architecture : " $(uname -r)

# 主机名 
echo "Hostname : " $HOSTNAME

# 内部IP地址
echo "Internal IP : " $(hostname -I)

# 外部IP地址  使用ipecho.net的IP Echo Service，有时这个网站会打不开 :)
echo "External IP : " $(curl -s ipecho.net/plain; echo)

# DNS 
echo "Name Server : " $(cat /etc/resolv.conf | grep nameserver | awk '{print $2}')

# 当前登录的用户
echo "Logged In users: " 
who

# 内存与SWAP 
echo "Ram Usages : " 
free -h | grep -v "Swap"
echo "Swap Usages : "
free -h | grep -v "Mem"

# 磁盘空间
echo "Disk Uages :"
df -h | grep 'FileSystem\|^/dev/*'

# 平衡负荷 
echo "Load Average : " $(top -n 1 -b | grep "load average:" | awk '{print $10 $11 $12}')

# 运行时间 
echo "System Uptime Days (HH:MM) : " $(uptime | awk '{print $3 $4}' | cut -f1 -d,)
