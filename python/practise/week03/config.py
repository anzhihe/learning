#!/usr/bin/env python
# coding: utf8

port = 8888
server = 'default'
servername = 'cmdb'
access_log = '/var/log/cmdb.log'
home = '/home/kk/www'
proxy_port = 9999

rh = open('D:\\python\\study\\week03\\nignx.tpl')
nginx_conf = rh.read().format(port=port, server=server, servername=servername, access_log=access_log, home=home, proxy_port=proxy_port)
rh.close()

handler = open('cmdb.conf', 'w')
handler.write(nginx_conf)
handler.close()