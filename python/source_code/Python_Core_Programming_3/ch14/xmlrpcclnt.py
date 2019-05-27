#!/usr/bin/env python

from math import pi
import xmlrpclib

server = xmlrpclib.ServerProxy('http://localhost:8888')
print 'Current time in seconds after epoch:', server.now_int()
print 'Current time as a string:', server.now_str()
print 'Area of circle of radius 5:', server.mul(pi, server.pow(5, 2))
stock = server.stock('goog')
print 'Latest Google stock price: %s (%s / %s) as of %s at %s' % tuple(stock)
forex = server.forex()
print 'Latest foreign exchange rate from %s: %s as of %s at %s' % tuple(forex)
forex = server.forex('eur', 'usd')
print 'Latest foreign exchange rate from %s: %s as of %s at %s' % tuple(forex)
print 'Latest Twitter status:', server.status()
#print 'Posted tweet at:', server.tweet('Latest GOOG stock price is %s)
