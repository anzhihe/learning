import os
import zipfile

newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('README.md', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()