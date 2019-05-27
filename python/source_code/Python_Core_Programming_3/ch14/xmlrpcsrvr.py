#!/usr/bin/env python

import SimpleXMLRPCServer
import csv
import operator
import time
import urllib2
import twapi # twapi.py from the previous chapter

server = SimpleXMLRPCServer.SimpleXMLRPCServer(("localhost", 8888))
server.register_introspection_functions()

FUNCs = ('add', 'sub', 'mul', 'div', 'mod')
for f in FUNCs:
    server.register_function(getattr(operator, f))
server.register_function(pow)

class SpecialServices(object):
    def now_int(self):
        return time.time()

    def now_str(self):
        return time.ctime()

    def timestamp(self, s):
        return '[%s] %s' % (time.ctime(), s)

    def stock(self, s):
        url = 'http://quote.yahoo.com/d/quotes.csv?s=%s&f=l1c1p2d1t1'
        u = urllib2.urlopen(url % s)
        res = csv.reader(u).next()
        u.close()
        return res

    def forex(self, s='usd', t='eur'):
        url = 'http://quote.yahoo.com/d/quotes.csv?s=%s%s=X&f=nl1d1t1'
        u = urllib2.urlopen(url % (s, t))
        res = csv.reader(u).next()
        u.close()
        return res

    def status(self):
        t = twapi.Twitter('twython')
        res = t.verify_credentials()
        status = twapi.ResultsWrapper(res.status)
        return status.text

    def tweet(self, s):
        t = twapi.Twitter('twython')
        res = t.update_status(s)
        return res.created_at

server.register_instance(SpecialServices())

try:
    print 'Welcome to PotpourriServ v0.1\n(Use ^C to exit)'
    server.serve_forever()
except KeyboardInterrupt:
    print 'Exiting'
