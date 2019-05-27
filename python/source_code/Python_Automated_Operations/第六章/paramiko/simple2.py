#!/usr/bin/env python
import paramiko
import os

hostname='192.168.1.21'
username='root'
paramiko.util.log_to_file('syslogin.log')

ssh=paramiko.SSHClient()
ssh.load_system_host_keys()
privatekey = os.path.expanduser('/home/key/id_rsa')
key = paramiko.RSAKey.from_private_key_file(privatekey)

ssh.connect(hostname=hostname,username=username,pkey = key)
stdin,stdout,stderr=ssh.exec_command('free -m')
print stdout.read()
ssh.close()
