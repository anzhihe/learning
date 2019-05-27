#!/usr/bin/env python

# Usage: reloader.py dirToWatch [minDelay]
# reloader.py is Public Domain.

# Requires the development version of pyinotify
# See: http://seb.dbzteam.com/pages/pyinotify-dev.html
# Download: http://seb.dbzteam.com/pub/pyinotify.py

# Change the two settings below-

# changes to files with these extensions will trigger runCmd
reloadExtensions = ['.py', '.wsgi'] 
# command passed to os.system
runCmd = "sudo /etc/init.d/apache2 restart"

import os
import sys
import time

import pyinotify

try:
    watchDir = sys.argv[1]
except IndexError:
    print "Usage: reloader.py dirToWatch [minDelay]"
    sys.exit()

minDelay = 0.5 # minimum delay before running the command again
if len(sys.argv) > 2:
    minDelay = float(sys.argv[2])
mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE | \
     pyinotify.IN_MODIFY # watched events

lastTime = 0

wm = pyinotify.WatchManager()

class PTmp(pyinotify.ProcessEvent):
    def process_default(self, event):
        global lastTime
        print("Change in %s" % os.path.join(event.path, event.name))
        if os.path.splitext(event.name)[-1] in reloadExtensions:
            if time.time() > (lastTime + minDelay):
                print "Running " + runCmd
                os.system(runCmd)
                lastTime = time.time()
            else:
                print "Timeout not reached, not running command."

notifier = pyinotify.Notifier(wm, PTmp())

wdd = wm.add_watch(watchDir, mask, rec=True, auto_add=True)

while True:
    try:
        notifier.process_events()
        if notifier.check_events():
            notifier.read_events()
    except KeyboardInterrupt:
        notifier.stop()
        break
