#!/bin/bash

# 备份最近一天当前目录下所有修改的文件
# 使用-的stdin、stdout，及tar+gzip的手段

# 默认的备份文件名，嵌入当前的时间
BACKUPFILE=backup-$(date +%Y-%m-%d)

# 如果没有传递参数给此脚本，则使用默认的文件名
archive=${1:-$BACKUPFILE}

tar cvf - `find . -mtime -1 -type f -print` > $archive.tar
gzip $archive.tar

# 如果当前目录中文件过多、或文件名包括空格时，有可能执行失败
# 可以考虑修改为：
# find . -mtime -1 -type f -print0 | xargs -0 tar rvf "$archive.tar"

echo "Directory $PWD backup up in archive file \"$archive.tar.gz\"."

exit 0
