#!/usr/bin/env python
'''
$Id$

ospathex.py -- OS path example

    This script test drives many of the operating system module file
    and file path functions.  The temporary directory is chosen by
    the tempfile module.  If that does not exist, then there is a
    limited set of directory names that are hard-coded as part of
    this application.  Please add one for your system if this script
    cannot find a temporary directory for you.
'''

import os        # operating system module (import real OS module, i.e., posix, nt, etc.)

def testOSmod(tmpdir):
    'testOSmod(tmpdir) -- test the "os" module with given temporary directory'

    # set working directory
    wd = os.path.join(tmpdir, 'example')

    # create and display test subdirectory name
    print '*** creating example directory...'
    os.mkdir(wd)
    print '*** new working directory:'
    print wd

    # display test subdirectory listing
    print '*** working directory listing:'
    print os.listdir(wd)

    # create test file and show updated directory listing
    print '*** creating test file...'
    testfile = os.path.join(wd, 'test')
    file = open(testfile, 'w')
    file.write('foo\n')
    file.write('bar\n')
    file.close()
    print '*** updated directory listing:'
    print os.listdir(wd)

    # test file rename using os.rename()
    print "*** renaming 'test' to 'filetest.txt'"
    newtestfile = os.path.join(wd, 'filetest.txt')
    os.rename(testfile, newtestfile)
    print '*** updated directory listing:'
    print os.listdir(wd)

    # test file pathname component join function (os.path.join())
    # (join directory name and only file [our test file] in directory)
    path = os.path.join(wd, os.listdir(wd)[0])
    print '*** full file pathname:'
    print path

    # test file pathname split and extension split
    print '*** (pathname, basename) == '
    print os.path.split(path)
    print '*** (filename, extension) == '
    print os.path.splitext(os.path.basename(path))

    # display test file contents
    print '*** displaying file contents:'
    file = open(path)
    allLines = file.readlines()
    file.close()
    for eachLine in allLines:
        print eachLine,

    # remove test file, show updated directory listing
    print '*** deleting test file'
    os.remove(path)
    print '*** updated directory listing:'
    print os.listdir(wd)

    # delete test directory
    print '*** deleting test directory'
    os.rmdir(wd)
    print '*** DONE'


def main():
    'main() -- look for temporary directory and run test'

    # look for a temporary directory; try tempfile module first
    try:
        from tempfile import gettempdir
        tmpdir = gettempdir()

    # if tempfile not available, try a few selected directories
    except:
        for tmpdir in ('/tmp', 'c:/windows/temp'):
            if os.path.isdir(tmpdir):
                break

        # otherwise no temporary directory found
        else:
            print 'no temp directory available'
            return

    testOSmod(tmpdir)


# run main() if invoked as script
if __name__ == '__main__':
    main()
