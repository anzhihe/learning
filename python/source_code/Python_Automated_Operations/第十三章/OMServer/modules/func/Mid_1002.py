# -*- coding: utf-8 -*-
from Public_lib import *

#查看最新登录模块#

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
            self.Runresult =client.command.run("/usr/bin/tail -"+str(self.sys_param_array[0])+" /var/log/secure")
        except Exception,e:
            return str(e)
        return self.Runresult
