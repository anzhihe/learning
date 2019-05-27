#!/bin/bash
# spam-lookup.sh: 查找滥用的连接来报告垃圾邮件发送者.
# 感谢Michael Zick.
                                                      
# 检查命令行参数.
ARGCOUNT=1
E_WRONGARGS=65
if [ $# -ne "$ARGCOUNT" ]
then
  echo "Usage: `basename $0` domain-name"
  exit $E_WRONGARGS
fi


dig +short $1.contacts.abuse.net -c in -t txt
# 也试试:
#     dig +nssearch $1
#     尽量找到"可信赖的名字服务器"并且显示SOA记录.
                                                               
# 下边这句也可以:
#     whois -h whois.abuse.net $1
#           ^^ ^^^^^^^^^^^^^^^  指定主机.
#     使用这个命令也可以查找多个垃圾邮件发送者, 比如:"
#     whois -h whois.abuse.net $spamdomain1 $spamdomain2 . . .
                                                               
                                                               
#  练习:
#  -----
#  扩展这个脚本的功能,
#+ 让它可以自动发送e-mail来通知
#+ 需要对此负责的ISP的联系地址.
#  暗示: 使用"mail"命令.

exit $?

# spam-lookup.sh chinatietong.com
#                一个已知的垃圾邮件域. (译者: 中国铁通 . . .)

# "crnet_mgr@chinatietong.com"
# "crnet_tec@chinatietong.com"
# "postmaster@chinatietong.com"


#  如果想找到这个脚本的一个更详尽的版本,
#+ 请访问SpamViz的主页, http://www.spamviz.net/index.html.
