#!/bin/bash
# 假设传给脚本的参数有：-d|--debug -f|--conf ConfigureFile等
while [ $# -gt 0 ]
do
  case "$1" in
    -d | --debug )
      DEBUG=1	# 有-d或--debug参数 
      ;;
    -f | --conf )
      CONFFILE="$2"
      shift
      if [ ! -f $CONFFILE ]; then
        echo "Error: Supplied file doesn't exist!"
        exit $E_CONFFILE
      fi
      ;;
  esac
  shift		# 检查剩余参数
done

exit 0
