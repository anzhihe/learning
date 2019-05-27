#!/bin/bash

filename=sys.log

cat /dev/null > $filename; echo "Creating / cleaning out file."
#  如果文件不存在的话就创建文件,
#+ 然后将这个文件清空.
#  : > filename   和   > filename 也能完成这个工作.

tail /var/log/messages > $filename  
# /var/log/messages 必须具有全局的可读权限才行. 

echo "$filename contains tail end of system log."

exit 0
