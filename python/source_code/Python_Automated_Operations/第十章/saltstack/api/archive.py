def tar(options, tarfile, cwd=None, template=None, *sources):
    print "options:",options
    print "tarfile",tarfile
    print "cwd",cwd
    print "template",template
    print "sources",sources

tar('tar','/tmp/test.tar.gz','/tmp')
