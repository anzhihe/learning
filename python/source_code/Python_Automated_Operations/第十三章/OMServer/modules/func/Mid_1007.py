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
            if commonname=="resin":
                self.command="/etc/init.d/resin restart"
            elif commonname=="nginx":
                self.command="/etc/init.d/nginx restart"
            elif commonname=="haproxy":
                self.command="/etc/init.d/haproxy restart"
            elif commonname=="apache":
                self.command="/etc/init.d/httpd restart"
            elif commonname=="mysql":
                self.command="/etc/init.d/mysql restart"
            elif commonname=="lighttpd":
                self.command="/etc/init.d/lighttpd restart"
            self.Runresult=client.command.run(self.command)

        except Exception,e:
            return str(e)
        return self.Runresult
