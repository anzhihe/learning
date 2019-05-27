#!/usr/bin/python

import sys
import func.overlord.client as fc
import xmlrpclib

module = sys.argv[1]
pythonmodulepath="/usr/lib/python2.6/site-packages/func/minion/modules/"
client = fc.Client("*")

fb = file(pythonmodulepath+module, "r").read()
data = xmlrpclib.Binary(fb)

print client.copyfile.copyfile(pythonmodulepath+ module,data)
print client.command.run("/etc/init.d/funcd restart")
