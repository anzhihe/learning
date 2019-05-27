#!/usr/bin/env python

from urllib import urlretrieve

def firstNonBlank(lines):
    for eachLine in lines:
        if not eachLine.strip():
            continue
        else:
            return eachLine

def firstLast(webpage):
    f = open(webpage)
    lines = f.readlines()
    f.close()
    print firstnonblank(lines),
    lines.reverse()
    print firstnonblank(lines),

def download(url='http://www',
            process=firstLast):
    try:
        retval = urlretrieve(url)[0]
    except IOError:
        retval = None
    if retval:		# do some processing
        process(retval)

if __name__ == '__main__':
    download()
