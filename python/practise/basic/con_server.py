#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#connect to the server by password or key

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('127.0.0.1',22,'anzhihe','anzhihe')
stdin,stdout,stderr = ssh.exec_command('df')
print(stdout.read())
ssh.close();

'''
private_key_path = '/Users/anzhihe/.ssh/id_rsa'
key = paramiko.RSAKey.from_priavte_key_file(private_key_path)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.1.1','22','anzhihe',key)
stdin, stdout, stderr = ssh.exec_command('df')
print stdout.read()
ssh.close()
'''