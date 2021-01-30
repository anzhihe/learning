#coding:utf-8
'''
创建TCP服务端

#coding:utf-8
import socket
import threading
import time
def dealClient(sock, addr):
    #第四步：接收传来的数据，并发送给对方数据
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Hello,I am server!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        print '-->>%s!' % data.decode('utf-8')
        sock.send(('Loop_Msg: %s!' % data.decode('utf-8')).encode('utf-8'))
    #第五步：关闭套接字
    sock.close()
    print('Connection from %s:%s closed.' % addr)
if __name__=="__main__":
    #第一步：创建一个基于IPv4和TCP协议的Socket
    # 套接字绑定的IP(127.0.0.1为本机ip)与端口
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 9999))
    #第二步:监听连接
    s.listen(5)
    print('Waiting for connection...')
    while True:
        # 第三步:接受一个新连接:
        sock, addr = s.accept()
        # 创建新线程来处理TCP连接:
        t = threading.Thread(target=dealClient, args=(sock, addr))
        t.start()

'''

'''
TCP客户端的创建和运行

#coding:utf-8
import socket
#初始化Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#连接目标的ip和端口
s.connect(('127.0.0.1', 9999))
# 接收消息
print('-->>'+s.recv(1024).decode('utf-8'))
# 发送消息
s.send(b'Hello,I am a client')
print('-->>'+s.recv(1024).decode('utf-8'))
s.send(b'exit')
#关闭套接字
s.close()

'''
