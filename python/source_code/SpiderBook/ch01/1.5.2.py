#coding:utf-8

'''
UDP服务端创建和运行

#coding:utf-8
import socket
#创建Socket，绑定指定的ip和端口
#SOCK_DGRAM指定了这个Socket的类型是UDP。绑定端口和TCP一样。
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9999))
print('Bind UDP on 9999...')
while True:
    # 直接发送数据和接收数据
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)

'''

'''
UDP 客户端的创建和运行

#coding:utf-8
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Hello', b'World']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))
s.close()

'''