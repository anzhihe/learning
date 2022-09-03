#!/bin/bash
# 监控指定文件系统已使用空间的脚本

# 判断传递过来的参数
if [[ -z "$1" ]]; then
  echo "Missing parameter! Systax: ./`basename $0` mount_point/disk"
  exit 3
else
  MOUNT_POINT=$1
fi

#used_space=`df -h / | grep -v Filesystem | awk '{print $5}' | sed 's/%//g'`
used_space=`df -h ${MOUNT_POINT} | grep -v Filesystem | awk '{print $5}' | sed 's/%//g'`

case $used_space in 
[1-84]*)
  echo "OK - $used_space% of disk space used."
  exit 0
  ;;
[85]*)
  echo "WARNING  - $used_space% of disk space used."
  exit 1
  ;;
[86-100]*)
  echo "CRITICAL - $used_space% of disk space used."
  exit 2
  ;;
*)
  echo "UNKNOWN - $used_space% of disk space used."
  exit 3
  ;;
esac
