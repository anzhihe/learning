#!/usr/bin/env python
#coding:utf-8
import sys
import socket
import fcntl
import struct
import logging
from config import *
import urllib,httplib
socket.setdefaulttimeout(Connect_TimeOut)

logging.basicConfig(level=logging.DEBUG,
            format='%(asctime)s [%(levelname)s] %(message)s',
            filename=sys.path[0]+'/omsys.log',
            filemode='a')

if len(sys.argv)<6:
    logging.error('History not configured in /etc/profile!')
    sys.exit()

def get_local_ip(ethname):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        addr = fcntl.ioctl(sock.fileno(), 0x8915, struct.pack('256s', ethname))
        return socket.inet_ntoa( addr[20:24] )
    except Exception,e:
        logging.error('get localhost IP address error:'+str(e))
        return "127.0.0.1"

def pull_history(http_get_param=""):
    try:
        http_client =httplib.HTTPConnection(OMServer_address, 80, timeout=Connect_TimeOut)
        http_client.request("GET", http_get_param)
        response =http_client.getresponse()

        if response.status != 200:       
            logging.error('response http status error:'+str(response.status))
            sys.exit()

        http_content=response.read().strip()
        if http_content != "OK":       
            logging.error('response http content error:'+str(http_content))
            sys.exit()

    except Exception, e:
        logging.error('connection django-cgi server error:'+str(e))
        sys.exit()
    finally:
        if http_client:
            http_client.close()
        else:
            logging.error('connection django-cgi server unknown error.')
            sys.exit()


Sysip = get_local_ip(Net_driver)
SysUser = sys.argv[2]
History_Id = sys.argv[1]
History_date = sys.argv[3]
History_time = sys.argv[4]
History_command = ""

for i in range(5, len(sys.argv)):
    History_command+= sys.argv[i]+" "

s= "/omaudit/omaudit_pull/?history_id="+History_Id+"&history_ip="+Sysip+"&history_user="+SysUser+"&history_datetime="+History_date+urllib.quote(" ")+History_time+"&history_command="+urllib.quote(History_command.strip())

pull_history(s)