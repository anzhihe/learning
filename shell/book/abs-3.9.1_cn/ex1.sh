# 清除
# 当然要使用root身份来运行这个脚本.

cd /var/log
cat /dev/null > messages
cat /dev/null > wtmp
echo "Logs cleaned up."
