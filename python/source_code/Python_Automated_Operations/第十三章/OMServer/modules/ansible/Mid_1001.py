# -*- coding: utf-8 -*-
from Public_lib import *

#查看系统日志模块#

class Modulehandle():
    def __init__(self,moduleid,hosts,sys_param_row):
        self.hosts = ""
        self.Runresult = ""
        self.moduleid = moduleid
        self.sys_param_array= sys_param_row
        self.hosts=target_host(hosts,"IP")

    def run(self):
        try:
            self.Runresult = ansible.runner.Runner(
            pattern=self.hosts, forks=forks,
            module_name="command", module_args="/usr/bin/tail -"+str(self.sys_param_array[0])+" /var/log/messages",).run()
            if len(self.Runresult['dark']) == 0 and len(self.Runresult['contacted']) == 0:
                return "No hosts found,请确认主机已经添加ansible环境！"
   
        except Exception,e:
            return str(e)
        return self.Runresult
