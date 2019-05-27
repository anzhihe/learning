import salt.client
client = salt.client.LocalClient()
#ret = client.cmd('SN2013-08-021', 'cp.get_file',['salt://nginx/nginx.conf','/tmp/nginx.conf','gzip=5'])
#ret = client.cmd('SN2013-08-021', 'cron.set_job',['root','*','*','*','*','*','/usr/echo'])
#ret = client.cmd('SN2013-08-021', 'cmd.run',['free -m'])
#ret = client.cmd('SN2013-08-022', 'iptables.append',['filter','INPUT','rule=\'-p tcp --sport 80 -j ACCEPT\''])
#ret = client.cmd('SN2013-08-022', 'network.ip_addrs')
#ret = client.cmd('SN2013-08-022', 'pkg.remove',['php'])
ret = client.cmd('SN2013-08-022', 'service.stop',['nginx'])
print ret

