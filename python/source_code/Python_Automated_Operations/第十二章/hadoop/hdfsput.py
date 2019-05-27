import subprocess
import sys
import datetime
webid="web1"
currdate=datetime.datetime.now().strftime('%Y%m%d')
logspath="/data/logs/"+currdate+"/access.log"
logname="access.log."+webid

try:
    subprocess.Popen(["/usr/local/hadoop-1.2.1/bin/hadoop", "dfs", "-mkdir", "hdfs://192.168.1.20:9000/user/root/website.com/"+currdate], stdout=subprocess.PIPE)
except Exception,e:
   pass
putinfo=subprocess.Popen(["/usr/local/hadoop-1.2.1/bin/hadoop", "dfs", "-put", logspath, "hdfs://192.168.1.20:9000/user/root/website.com/"+currdate+"/"+logname], stdout=subprocess.PIPE)

for line in putinfo.stdout:
    print line
