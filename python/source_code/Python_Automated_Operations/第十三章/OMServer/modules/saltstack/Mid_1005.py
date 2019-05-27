# -*- coding: utf-8 -*-
from Public_lib import *

#同步业务文件模块#

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
            if commonname=="nginx":
                #源文件
                source="salt://config/nginx"
                
                #目标文件
                goal="/etc/init.d/nginx"
                
                #处理后续工作
                hx="chmod u+x /etc/init.d/nginx"
            elif commonname=="haproxy":
                source="salt://config/haproxy.cfg"
                goal="/usr/local/haproxy/haproxy.cfg"
                hx="ls "+str(goal)
                
            elif commonname=="syslog":
                source="salt://config/syslog.conf"
                goal="/etc/syslog.conf"
                hx="/etc/init.d/syslog restart"

            elif commonname=="nginx_config":
                source="salt://config/nginx.conf"
                goal="/usr/local/nginx/conf/nginx.conf"
                hx="ls "+str(goal)

            elif commonname=="sysctl":
                source="salt://config/sysctl.conf"
                goal="/etc/sysctl.conf"
                hx="sysctl -p"
                
            elif commonname=="resin":
                source="salt://config/resin.conf"
                goal="/usr/java/resin-3.0.22/conf/resin.conf"
                hx="ls /usr/java/resin-3.0.22/conf/resin.conf"

            elif commonname=="resinhttpd":
                source="salt://config/httpd.sh"
                goal="/usr/java/resin-3.0.22/bin/httpd.sh"
                hx="chmod u+x /usr/java/resin-3.0.22/bin/httpd.sh"

            elif commonname=="resinjar":
                source="salt://config/resin.jar"
                goal="/usr/java/resin-3.0.22/lib/resin.jar"
                hx="ls /usr/java/resin-3.0.22/lib/resin.jar"
                
            self.Runresult=client.cmd(self.hosts,'cp.get_file',[source,goal],expr_form='list')
            if len(self.Runresult) == 0:
                return "No hosts found,请确认主机已经添加saltstack环境！"

            self.Runresult  = client.cmd(self.hosts,'cmd.run',[hx],expr_form='list')
        except Exception,e:
            return str(e)
        return self.Runresult
