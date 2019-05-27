#!/usr/bin/env python

import SocketServer
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)

class MyRequestHandler(SocketServer.StreamRequestHandler):
    def handle(self):
        print '...connected from:', self.client_address
        self.wfile.write('[%s] %s\n' % (
            ctime(), self.rfile.readline().strip())
        )

tcpSerSock = SocketServer.TCPServer(ADDR, MyRequestHandler)
print 'waiting for connection...'
tcpSerSock.serve_forever()
