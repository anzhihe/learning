# -*- coding: utf-8 -*-
from Public_lib import *

#查看系统版本模块#

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
            self.Runresult =client.command.run("/usr/bin/head -n 1 /etc/issue")
        except Exception,e:
            return str(e)
        return self.Runresult
