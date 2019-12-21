import os
import zipfile

os.chdir('E:\\')
exampleZip = zipfile.ZipFile('mupdf-1.9a-windows.zip')
print(exampleZip.namelist())

spamInfo = exampleZip.getinfo('mupdf-1.9a-windows/COPYING.txt')
print(spamInfo.file_size)
print(spamInfo.compress_size)

print('Compressed file is %sx smaller!', (round(spamInfo.file_size/spamInfo.compress_size, 2)))
# exampleZip.extractall()
exampleZip.close()
