#!/usr/bin/env python

from CGIHTTPServer import test

if __name__ == '__main__':
    try:
        print 'Welcome to the machine...\nPress ^C once or twice to quit'
        test()
    except KeyboardInterrupt:
        print 'exiting server...'
