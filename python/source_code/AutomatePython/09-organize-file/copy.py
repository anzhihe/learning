import os
import sys
import shutil

def copy(suffix, src, dst):
    # Create dst directory
    if not os.path.exists(dst):
        os.mkdir(dst)

    # list all files
    try:
        for dirpath, dirnames, filenames in os.walk(src):
            #print(dirpath, dirnames, filenames)
            for filename in filenames:
                if filename.endswith('.'+suffix):
                    print(os.path.join(dirpath, filename)) 
                    # copy files with pointed suffix to dst
                    shutil.copy(os.path.join(dirpath, filename), dst)
    except shutil.SameFileError:
        print("Finished copying file.")

copy('py', '.', 'pyfiles')