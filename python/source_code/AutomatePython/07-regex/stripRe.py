import re

def stripRe(s):
    #stripRe = re.compile(r'^\s+\(.*\)\s+$')
    stripRegex = re.compile(r'^\s+(.*)\s+$')
    mo = stripRegex.search(s)
    return mo.group(1)


strTest = '   hello world    '
print(strTest)
print(stripRe(strTest))