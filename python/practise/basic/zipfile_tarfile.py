#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# zip压缩
# import zipfile

# z = zipfile.ZipFile('/tmp/test.zip','w')
# z.write('/tmp/a')
# z.write('/tmp/b')
# z.close()

# zip解压
# z = zipfile.ZipFile('/tmp/test.zip','r')
# z.extractall()
# z.close()


# tar压缩
import tarfile

# tar = tarfile.open('/tmp/test.tar','w')
# tar.add('/tmp/a')
# tar.add('/tmp/b')
# tar.close()

# tar解压
tar = tarfile.open('/tmp/test.tar','r')
tar.extractall()
tar.close()