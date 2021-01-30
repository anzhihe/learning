#coding:utf-8
'''
gevent的使用流程

from gevent import monkey; monkey.patch_all()
import gevent
import urllib2

def run_task(url):
    print 'Visit --> %s' % url
    try:
        response = urllib2.urlopen(url)
        data = response.read()
        print '%d bytes received from %s.' % (len(data), url)
    except Exception,e:
        print e
if __name__=='__main__':
    urls = ['https://github.com/','https://www.python.org/','http://www.cnblogs.com/']
    greenlets = [gevent.spawn(run_task, url) for url in urls  ]
    gevent.joinall(greenlets)
'''

'''
gevent pool对象使用

from gevent import monkey
monkey.patch_all()
import urllib2
from gevent.pool import Pool
def run_task(url):
    print 'Visit --> %s' % url
    try:
        response = urllib2.urlopen(url)
        data = response.read()
        print '%d bytes received from %s.' % (len(data), url)
    except Exception,e:
        print e
    return 'url:%s --->finish'% url

if __name__=='__main__':
    pool = Pool(2)
    urls = ['https://github.com/','https://www.python.org/','http://www.cnblogs.com/']
    results = pool.map(run_task,urls)
    print results

'''