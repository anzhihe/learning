import os
import re
import sys


def getTxtFile(directory):    
    txts = []
    txtSuffix = r'\.txt$'
    txtRegex = re.compile(txtSuffix)
    for filename in os.listdir(directory):
        mo = txtRegex.search(filename)
        if mo:
            txts.append(filename)
    return txts

def find(query, directory):
    txts = getTxtFile(directory)
    print(txts)
    queryRegex = re.compile(query)
    for txt in txts:
        with open(txt) as f:
            for line in f:
                mo = queryRegex.search(line)
                if mo:
                    print(txt.ljust(20) + ": " + line, end='')

find("world", ".")
