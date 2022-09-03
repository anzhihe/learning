#!/bin/bash
# 练习：显示时间和日期, 列出所有登陆的用户, 系统的运行时间. 
# 并将上述信息保存到一个log file中

LOG_FILE=/tmp/02-lab1.log

date
w
uptime

echo "" >> $LOG_FILE
date >> $LOG_FILE
w >> $LOG_FILE
uptime >> $LOG_FILE
