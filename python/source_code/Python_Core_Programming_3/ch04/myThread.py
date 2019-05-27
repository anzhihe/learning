#!/usr/bin/env python

import threading
from time import time, ctime

class MyThread(threading.Thread):
    def __init__(self, func, args, name='', verb=False):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
        self.verb = verb

    def getResult(self):
        return self.res

    def run(self):
        if self.verb:
            print 'starting', self.name, 'at:', ctime()
        self.res = self.func(*self.args)
        if self.verb:
            print self.name, 'finished at:', ctime()
