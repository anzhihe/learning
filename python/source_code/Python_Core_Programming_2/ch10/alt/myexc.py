#!/usr/bin/env python
'''
$Id$

myexc.py -- "my exceptions" demo which highlights user-created
    exceptions.  NOTE:  this example does not currently work with
    JPython as neither the errno nor tempfile modules have been
    implemented, and also, the socket module is incomplete.
'''

# import all our needed modules
import os, socket, errno, types, tempfile

# create our a new NetworkError exception, derived from IOError
class NetworkError(IOError):
    pass

# create our a new FileError exception, derived from IOError
class FileError(IOError):
    pass

# updArgs --> tuple
def updArgs(args, newarg=None):
    '''updArgs(args, newarg=None) -- if instance, grab each exception
        instance argument and place them in a list; otherwise, just
        convert given args sequence to a list for mutability; add
        newarg if necessary; then convert the whole thing to a tuple.'''

    if isinstance(args, IOError):
        myargs = []
	myargs.extend([arg for arg in args])
    else:
        myargs = list(args)

    if newarg:
        myargs.append(newarg)

    return tuple(myargs)


# fileArgs --> tuple
def fileArgs(fn, mode, args):
    '''fileArgs(fn, mode, args) -- similar to updArgs() except made
        specifically for files; creates small permission string and
        formats error to be similar to other IOError exceptions.'''

    if args[0] == errno.EACCES and \
            'access' in dir(os):
        perms = ''
        permd = { 'r': os.R_OK, 'w': os.W_OK, \
                    'x': os.X_OK }
        pkeys = permd.keys()
        pkeys.sort()
        pkeys.reverse()

        for eachPerm in 'rwx':
            if os.access(fn, permd[eachPerm]):
                perms = perms + eachPerm
            else:
                perms = perms + '-'

        if isinstance(args, IOError):
            myargs = []
	    myargs.extend([arg for arg in args])
        else:
            myargs = list(args)

        myargs[1] = "'%s' %s (perms: '%s')" % \
                    (mode, myargs[1], perms)

        myargs.append(args.filename)

    else:
        myargs = args

    return tuple(myargs)

# myconnect() --> None (raises exception on error)
def myconnect(sock, host, port):
    '''myconnect(sock, host, port) -- attempt to make a network connection
    with the given socket and host-port pair; raises our new NetworkError
    exception and collates error number and reason.'''

    try:
        sock.connect(host, port)

    except socket.error, args:
        myargs = updArgs(args)        # convert inst to tuple
        if len(myargs) == 1:        # no #s on some errors
            myargs = (errno.ENXIO, myargs[0])

        raise NetworkError, \
            updArgs(myargs, host + ':' + str(port))


# myopen() --> file object
def myopen(fn, mode='r'):
    '''myopen(fn, mode) -- wrapper around the open() built-in function
    such that we raise our new FileError exception on an error situation
    and collate a set of FileError exception arguments to pass to the user'''

    try:
        fo = open(fn, mode)

    except IOError, args:
        raise FileError, fileArgs(fn, mode, args)

    return fo


# testfile() --> None
def testfile():
    '''testfile() -- runs the file tester, setting a variety of test files
    which should generate FileError exceptions'''

    fn = tempfile.mktemp()
    f = open(fn, 'w')
    f.close()

    for eachTest in ((0, 'r'), (0100, 'r'), (0400, 'w'), (0500, 'w')):
        try:
            os.chmod(fn, eachTest[0])
            f = myopen(fn, eachTest[1])

        except FileError, args:
            print "%s: %s" % \
                    (args.__class__.__name__, args)
        else:
            print fn, "opened ok... perms ignored"
            f.close()

    os.chmod(fn, 0777)
    os.unlink(fn)


# testnet() --> None
def testnet():
    '''testfile() -- runs the network tester, making various connections
    which should generate NetworkError exceptions'''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    for eachHost in (YOUR HOSTS HERE):
        try:
            myconnect(s, eachHost, 80)
        except NetworkError, args:
            print "%s: %s" % (args.__class__.__name__, args)
        else:
            print "network connection successful to", `eachHost`
            s.close()


# run tests if invoked as a script
if __name__ == '__main__':
    testfile()
    testnet()
