#!/usr/bin/python

from string import Template
s = Template('There are ${howmany} ${lang} Quotation Symbols')
print s.substitute(lang='Python', howmany=3)
print s.substitute(lang='Python')
print s.safe_substitute(lang='Python')
raw_input()
