# -*- coding: utf-8 -*-
from Public_lib import *

#查看应用配置信息模块#

class Modulehandle():
    def __init__(self,moduleid,hosts,sys_param_row):
        self.hosts = ""
        self.Runresult = ""
        self.moduleid = moduleid
        self.sys_param_array= sys_param_row
        self.hosts=target_host(hosts,"HN").split(";")

    def run(self):
        try:

            client = salt.client.LocalClient()
            commonname=str(self.sys_param_array[0])
            if commonname=="resin3.0.21":
                Runresult="/bin/cat /usr/java/resin-3.0.21/conf/resin.conf"
            elif commonname=="resin3.0.22":
                Runresult="/bin/cat /usr/java/resin-3.0.22/conf/resin.conf"
            elif commonname=="nginx":
                Runresult="/bin/cat /etc/nginx/nginx.conf"
            elif commonname=="haproxy":
                Runresult="/bin/cat /usr/local/haproxy/haproxy.cfg"
            elif commonname=="apache":
                Runresult="/bin/cat /usr/local/apache/conf/httpd.conf"
            elif commonname=="mysql":
                Runresult="/bin/cat /etc/my.cnf"
            elif commonname=="snmp":
                Runresult="/bin/cat /usr/local/etc/snmpd.conf"
            elif commonname=="lighttpd":
                Runresult="/bin/cat /usr/local/lighttpd/etc/lighttpd.conf"
            elif commonname=="squid2.5":
                Runresult="/bin/cat /usr/local/squid/etc/squid.conf"
            elif commonname=="squid2.6":
                Runresult="/bin/cat /usr/local/squid-2.6/etc/squid.conf"
            elif commonname=="firewall":
                Runresult="/bin/cat /etc/firewall.sh"
            elif commonname=="limits":
                Runresult="ulimit -n"

            self.Runresult  = client.cmd(self.hosts,'cmd.run',[Runresult],expr_form='list')
            if len(self.Runresult) == 0:
                return "No hosts found,请确认主机已经添加saltstack环境！"
        except Exception,e:
            return str(e)
        return self.Runresult
