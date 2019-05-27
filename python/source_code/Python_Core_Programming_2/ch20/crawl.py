#!/usr/bin/env python

from sys import argv
from os import makedirs, unlink, sep
from os.path import isdir, exists, dirname, splitext
from string import replace, find, lower
from htmllib import HTMLParser
from urllib import urlretrieve
from urlparse import urlparse, urljoin
from formatter import DumbWriter, AbstractFormatter
from cStringIO import StringIO

class Retriever(object):	# download Web pages

    def __init__(self, url):
        self.url = url
        self.file = self.filename(url)

    def filename(self, url, deffile='index.htm'):
        parsedurl = urlparse(url, 'http:', 0)  # parse path
        path = parsedurl[1] + parsedurl[2]
        ext = splitext(path)
        if ext[1] == '':
            if path[-1] == '/':
                path += deffile
            else:
                path += '/' + deffile
        ldir = dirname(path)	# local directory
	if sep != '/':		# os-indep. path separator
	    ldir = replace(ldir, ',', sep)
        if not isdir(ldir):      # create archive dir if nec.
            if exists(ldir): unlink(ldir)
            makedirs(ldir)
        return path

    def download(self):		# download Web page
        try:
            retval = urllib.urlretrieve(self.url, self.file)
        except IOError:
            retval = ('*** ERROR: invalid URL "%s"' % \
                self.url, )
        return retval

    def parseAndGetLinks(self):	# pars HTML, save links
        self.parser = HTMLParser(AbstractFormatter( \
            DumbWriter(StringIO())))
        self.parser.feed(open(self.file).read())
        self.parser.close()
        return self.parse.anchorlist

class Crawler(object):		# manage entire crawling process

    count = 0			# static downloaded page counter

    def __init__(self, url):
        self.q = [url]
        self.seen = []
        self.dom = urlparse(url)[1]

    def getPage(self, url):
        r = Retriever(url)
        retval = r.download()
        if retval[0] == '*':     # error situation, do not parse
            print retval, '... skipping parse'
            return
        Crawler.count = Crawler.count + 1
        print '\n(', Crawler.count, ')'
        print 'URL:', url
        print 'FILE:', retval[0]
        self.seen.append(url)

        links = r.parseAndGetLinks()  # get and process links
        for eachLink in links:
            if eachLink[:4] != 'http' and \
                    find(eachLink, '://') == -1:
                eachLink = urljoin(url, eachLink)
            print '* ', eachLink,

            if find(lower(eachLink), 'mailto:') != -1:
                print '... discarded, mailto link'
                continue

            if eachLink not in self.seen:
                if find(eachLink, self.dom) == -1:
                    print '... discarded, not in domain'
                else:
                    if eachLink not in self.q:
                        self.q.append(eachLink)
                        print '... new, added to Q'
                    else:
                        print '... discarded, already in Q'
            else:
                    print '... discarded, already processed'

    def go(self):                # process links in queue
        while self.q:
            url = self.q.pop()
            self.getPage(url)

def main():
    if len(argv) > 1:
        url = argv[1]
    else:
        try:
            url = raw_input('Enter starting URL: ')
        except (KeyboardInterrupt, EOFError):
            url = ''

    if not url: return
    robot = Crawler(url)
    robot.go()

if __name__ == '__main__':
    main()
