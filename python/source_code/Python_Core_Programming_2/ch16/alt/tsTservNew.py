#!/usr/bin/env python

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
tcpSerSock.setsockopt(SOL_SOCKET, SO_REUSEPORT, True)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
	print 'waiting for connection...'
	tcpCliSock, addr = tcpSerSock.accept()
	print '...connected from:', addr

	while True:
		data = tcpCliSock.recv(BUFSIZ)
		if not data:
			break
		print data
		data = raw_input('> ')
		if not data:
			break
		tcpCliSock.send(data)
		print "    ... waiting for reply ..."

	tcpCliSock.close()
tcpSerSock.close()
