# -*- coding: utf-8 -*-
from Public_lib import *

#查看应用配置信息模块#

class Modulehandle():
    def __init__(self,moduleid,hosts,sys_param_row):
        self.hosts = ""
        self.Runresult = ""
        self.moduleid = moduleid
        self.sys_param_array= sys_param_row
        self.hosts=target_host(hosts,"IP")

    def run(self):
        try:
            commonname=str(self.sys_param_array[0])
            if commonname=="resin3.0.21":
                self.command="/bin/cat /usr/java/resin-3.0.21/conf/resin.conf"
            elif commonname=="resin3.0.22":
                self.command="/bin/cat /usr/java/resin-3.0.22/conf/resin.conf"
            elif commonname=="nginx":
                self.command="/bin/cat /etc/nginx/nginx.conf"
            elif commonname=="haproxy":
                self.command="/bin/cat /usr/local/haproxy/haproxy.cfg"
            elif commonname=="apache":
                self.command="/bin/cat /usr/local/apache/conf/httpd.conf"
            elif commonname=="mysql":
                self.command="/bin/cat /etc/my.cnf"
            elif commonname=="snmp":
                self.command="/bin/cat /usr/local/etc/snmpd.conf"
            elif commonname=="lighttpd":
                self.command="/bin/cat /usr/local/lighttpd/etc/lighttpd.conf"
            elif commonname=="squid2.5":
                self.command="/bin/cat /usr/local/squid/etc/squid.conf"
            elif commonname=="squid2.6":
                self.command="/bin/cat /usr/local/squid-2.6/etc/squid.conf"
            elif commonname=="firewall":
                self.command="/bin/cat /etc/firewall.sh"
            elif commonname=="limits":
                self.command="ulimit -n"

            self.Runresult = ansible.runner.Runner(
            pattern=self.hosts, forks=forks,
            module_name="command", module_args=self.command,).run()

            if len(self.Runresult['dark']) == 0 and len(self.Runresult['contacted']) == 0:
                return "No hosts found,请确认主机已经添加ansible环境！"
        except Exception,e:
            return str(e)
        return self.Runresult
