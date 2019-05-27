#!/bin/bash
# dev-tcp.sh: 利用/dev/tcp重定向来检查Internet连接. 

# 本脚本由Troy Engel编写. 
# 经过授权在本书中使用. 
 
TCP_HOST=www.dns-diy.com   # 一个已知的对垃圾邮件友好的ISP. 
TCP_PORT=80                # 端口80是http. 
  
# 尝试连接. (有些像'ping' . . .) 
echo "HEAD / HTTP/1.0" >/dev/tcp/${TCP_HOST}/${TCP_PORT}
MYEXIT=$?

: &lt;&lt;EXPLANATION
If bash was compiled with --enable-net-redirections, it has the capability of
using a special character device for both TCP and UDP redirections. These
redirections are used identically as STDIN/STDOUT/STDERR. The device entries
are 30,36 for /dev/tcp:

  mknod /dev/tcp c 30 36

>From the bash reference:
/dev/tcp/host/port
    If host is a valid hostname or Internet address, and port is an integer
port number or service name, Bash attempts to open a TCP connection to the
corresponding socket.
EXPLANATION

   
if [ "X$MYEXIT" = "X0" ]; then
  echo "Connection successful. Exit code: $MYEXIT"
else
  echo "Connection unsuccessful. Exit code: $MYEXIT"
fi

exit $MYEXIT
