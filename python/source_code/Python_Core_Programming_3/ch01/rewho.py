#!/usr/bin/env python

import os
import re

f = os.popen('who', 'r')
for eachLine in f:
    print re.split('\s\s+|\t', eachLine.rstrip())
f.close()
