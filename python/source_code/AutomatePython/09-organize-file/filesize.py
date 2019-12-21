import os
import shutil

def search(dir, size):
    # dir exists
    if not os.path.exists(dir):
        print('Directory ' + dir + ' not exists.')

    # list all files in dir
    for dirpath, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            filesize = os.path.getsize(filepath)
            if filesize > size:
                print(str(filesize).ljust(16), filepath)
    # if filesize is bigger than size, print it's path

search('E:\\', 1024*1024*1024)