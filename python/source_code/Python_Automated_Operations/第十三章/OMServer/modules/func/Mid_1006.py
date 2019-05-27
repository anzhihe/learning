# -*- coding: utf-8 -*-
from Public_lib import *

#查看应用配置信息模块#

class Modulehandle():
    def __init__(self,moduleid,hosts,sys_param_row):
        self.hosts = ""
        self.Runresult = ""
        self.moduleid = moduleid
        self.sys_param_array= sys_param_row
        self.hosts=target_host(hosts,"HN")

    def run(self):
        try:
            client = fc.Overlord(self.hosts)
            commonname=str(self.sys_param_array[0])
            if commonname=="resin3.0.21":
                self.Runresult=client.command.run("/bin/cat /usr/java/resin-3.0.21/conf/resin.conf")
            elif commonname=="resin3.0.22":
                self.Runresult=client.command.run("/bin/cat /usr/java/resin-3.0.22/conf/resin.conf")
            elif commonname=="nginx":
                self.Runresult=client.command.run("/bin/cat /etc/nginx/nginx.conf")
            elif commonname=="haproxy":
                self.Runresult=client.command.run("/bin/cat /usr/local/haproxy/haproxy.cfg")
            elif commonname=="apache":
                self.Runresult=client.command.run("/bin/cat /usr/local/apache/conf/httpd.conf")
            elif commonname=="mysql":
                self.Runresult=client.command.run("/bin/cat /etc/my.cnf")
            elif commonname=="snmp":
                self.Runresult=client.command.run("/bin/cat /usr/local/etc/snmpd.conf")
            elif commonname=="lighttpd":
                self.Runresult=client.command.run("/bin/cat /usr/local/lighttpd/etc/lighttpd.conf")
            elif commonname=="squid2.5":
                self.Runresult=client.command.run("/bin/cat /usr/local/squid/etc/squid.conf")
            elif commonname=="squid2.6":
                self.Runresult=client.command.run("/bin/cat /usr/local/squid-2.6/etc/squid.conf")
            elif commonname=="firewall":
                self.Runresult=client.command.run("/bin/cat /etc/firewall.sh")
            elif commonname=="limits":
                self.Runresult=client.command.run("ulimit -n")
        except Exception,e:
            return str(e)
        return self.Runresult
