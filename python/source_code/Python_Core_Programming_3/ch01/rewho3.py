#!/usr/bin/env python

import os
import re

with os.popen('who', 'r') as f:
    for eachLine in f:
        print(re.split('\s\s+|\t', eachLine.rstrip()))
