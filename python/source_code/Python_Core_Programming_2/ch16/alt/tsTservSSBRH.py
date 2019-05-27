#!/usr/bin/env python

from SocketServer import BaseRequestHandler as BRH, TCPServer as TCP
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

class MyRequestHandler(BRH):
	def handle(self):
		print '...connected from:', self.client_address
		self.request.send('[%s] %s' % (ctime(),
		    self.request.recv(BUFSIZ)))

tcpServ = TCP(ADDR, MyRequestHandler)
tcpServ.allow_reuse_address = True
print 'waiting for connection...'
tcpServ.serve_forever()
