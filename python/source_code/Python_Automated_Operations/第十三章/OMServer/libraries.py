# -*- coding: utf-8 -*-
#!/usr/bin/env python

import random, base64
from hashlib import sha1

def crypt(data, key):
    """RC4 algorithm"""
    x = 0
    box = range(256)
    for i in range(256):
        x = (x + box[i] + ord(key[i % len(key)])) % 256
        box[i], box[x] = box[x], box[i]
    x = y = 0
    out = []
    for char in data:
        x = (x + 1) % 256
        y = (y + box[x]) % 256
        box[x], box[y] = box[y], box[x]
        out.append(chr(ord(char) ^ box[(box[x] + box[y]) % 256]))

    return ''.join(out)

def tencode(data, key, encode=base64.b64encode, salt_length=16):
    """RC4 encryption with random salt and final encoding"""
    salt = ''
    for n in range(salt_length):
        salt += chr(random.randrange(256))
    data = salt + crypt(data, sha1(key + salt).digest())
    if encode:
        data = encode(data)
    return data

def tdecode(data, key, decode=base64.b64decode, salt_length=16):
    """RC4 decryption of encoded data"""
    if decode:
        data = decode(data)
    salt = data[:salt_length]
    return crypt(data[salt_length:], sha1(key + salt).digest())

    
def ip2hostname(hosts,ip):
    for i in hosts.split(','):
        j=i.split('*')
        if ip in j:
            return j[1]
    
def hostname2ip(hosts,hostname):
    for i in hosts.split(','):
        j=i.split('*')
        if hostname in j:
            return j[0]
        

def func_transform(resultString,hosts):
    Response_string=""
    runstatus=""
    run_dict=resultString

    for (k,v) in run_dict.items():
        if v[0]==0:
            runstatus=u"<font color='#eeeeee'>运行状态</font> <font color='#006699'><b>成功</b></font>"
        else:
            runstatus=u"<font color='#eeeeee'>运行状态</font> <font color='red'><b>失败</b></font>"
        Response_string+=u"<font color='#eeeeee'>主机：</font><font color=#ffffff><b>"+hostname2ip(hosts.upper(),k.upper())+"</b></font><br>"+runstatus+"<br>"+str(v[1]).replace('\n','<br>')+"<br>"
        Response_string+="<table width='100%' height='15'><tbody><tr><td background='/static/images/B24.gif'></td></tr></tbody></table><br>"
    return Response_string.encode('utf-8')
    

def ansible_transform(resultString,hosts):
    Response_string=""
    results=resultString
    runstatus_ok=u"<font color='#eeeeee'>运行状态</font> <font color='#006699'><b>成功</b></font>"
    runstatus_failed=u"<font color='#eeeeee'>运行状态</font> <font color='red'><b>失败</b></font>"
    for (hostname, result) in results['contacted'].items():
        if not 'failed' in result:
            Response_string+=u"<font color='#eeeeee'>主机：</font><font color=#ffffff><b>%s</b></font><br>%s<br>%s<br><br>" % (hostname,runstatus_ok,result['stdout'].replace('\n','<br>'))
            Response_string+="<table width='100%' height='15'><tbody><tr><td background='/static/images/B24.gif'></td></tr></tbody></table><br>"
    
    for (hostname, result) in results['contacted'].items():
        if 'failed' in result:
            Response_string+=u"<font color='#eeeeee'>主机：</font><font color=#ffffff><b>%s</b></font><br>%s<br>%s<br>" % (hostname,runstatus_failed, result['msg'])
    
    for (hostname, result) in results['dark'].items():
        Response_string+= u"<font color='#eeeeee'>主机：</font><font color=#ffffff><b>%s</b></font><br>%s<br>%s<br>" % (hostname,runstatus_failed, result)

    return Response_string.encode('utf-8')
    
def saltstack_transform(resultString,hosts):
    Response_string=""
    runstatus=""
    run_dict=resultString

    for (k,v) in run_dict.items():
        if k!="":
            runstatus=u"<font color='#eeeeee'>运行状态</font> <font color='#006699'><b>成功</b></font>"
        else:
            runstatus=u"<font color='#eeeeee'>运行状态</font> <font color='red'><b>失败</b></font>"
        Response_string+=u"<font color='#eeeeee'>主机：</font><font color=#ffffff><b>"+hostname2ip(hosts.upper(),k)+"</b></font><br>"+runstatus+"<br>"+str(v).replace('\n','<br>')+"<br>"
        Response_string+="<table width='100%' height='15'><tbody><tr><td background='/static/images/B24.gif'></td></tr></tbody></table><br>"
    return Response_string.encode('utf-8')