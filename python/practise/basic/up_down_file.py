#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#Upload & Download files by password or key

import os,sys
import paramiko

t = paramiko.Transport(('192.168.1.1',22))
t.connect(username='anzhihe',password='anzhihe')
sftp = paramiko.SFTPClient.from_transport(t)
# sftp.put('/tmp/test','/tmp/test')
sftp.get('/tmp/test','/tmp/test2')
t.close



'''
private_key_path = '/Users/anzhihe/.ssh/id_rsa'
key = paramiko.RSAKey.from_priavte_key_file(private_key_path)

t = paramiko.Transport(('192.168.1.1',22))
t.connect(username='anzhihe',pkey=key)
sftp = paramiko.SFTPClient.from_transport(t)
# sftp.put('/tmp/test','/tmp/test')
sftp.get('/tmp/test','/tmp/test2')
t.close
'''