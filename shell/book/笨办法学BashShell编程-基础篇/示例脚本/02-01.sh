# 清除
# 当然要以root身份来运行这个脚本

cd /var/log
cat /dev/null > message
cat /dev/null > wtmp
echo "Logs cleaned up."
