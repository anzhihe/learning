#!/usr/bin/env python

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
udpSerSock.setsockopt(SOL_SOCKET, SO_REUSEPORT, True)
udpSerSock.bind(ADDR)

while True:
    print 'waiting for message...'
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto('[%s] %s' % (
        ctime(), data), addr)
    print '...received from and returned to:', addr

udpSerSock.close()
