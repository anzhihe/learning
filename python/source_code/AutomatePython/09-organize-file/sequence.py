import os
import shutil
import re

def sequence(dir, prefix):
    # dir exists
    if not os.path.exists(dir):
        print('Directory not exists.')
        return

    # list all file and get the number of files with prefix
    filenum = 0
    filelist = []
    for file in os.listdir(dir):
        if file.startswith(prefix):
            filenum += 1
            filelist.append(file)
    filelist.sort()
    
    #  rename file
    print(filelist)
    for i in range(filenum):
        srcfile = os.path.join(dir, filelist[i])
        dstfile = os.path.join(dir, prefix + '%03d'%(i+1) + '.txt')
        if srcfile != dstfile:
            print(srcfile, dstfile)
            shutil.move(srcfile, dstfile)

sequence('demo', 'spam')