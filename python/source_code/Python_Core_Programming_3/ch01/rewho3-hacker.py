#!/usr/bin/env python
"hacker's corner version of rewho3.py"

from os import popen
from re import split

with popen('who', 'r') as f:
    [print(split('\s\s+|\t', eachLine.strip())) for eachLine in f]
