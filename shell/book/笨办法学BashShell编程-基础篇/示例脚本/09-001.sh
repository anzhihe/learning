#!/bin/bash
# 代码片断

# 方法1：写日志
if [ -f /var/log/messages ]; then
  # 代码
fi

# 方法2：写日志，更优雅一些
LOGFILE=/var/log/message
if [ -f "$LOGFILE" ]; then
  # 代码
fi

