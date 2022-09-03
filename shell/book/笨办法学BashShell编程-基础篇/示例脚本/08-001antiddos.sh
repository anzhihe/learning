#!/bin/bash
# 参考：http://www.linuxjournal.com/content/back-dead-simple-bash-complex-ddos
# 通过lsof的输出允许并发的连接数，当连接数大于特定值，将其IP加入iptables规则中进行阻断
# lsof -ni | grep nginx | grep -iv listen | awk '{print $9}' | cut -d : -f 2 | sort | uniq | sed s/"http->"//

while [ 1 ] ;
do
  # 获取所有连接和连接尝试的列表，并生成uniq IP列表并遍历列表
  for ip in `lsof -ni | grep nginx | grep -iv listen | awk '{print $9}' | cut -d : -f 2 | sort | uniq | sed s/"http->"//`
  do
    # 查找此特定IP地址的连接数
    noconns=`lsof -ni | grep $ip | wc -l`;
    echo $ip : $noconns ;

    if [ "$noconns" -gt "50" ] ;  then
      # 如果建立的连接数超过50
      # 写日志
      # echo `date` "$ip has $noconns connections.  Total connections to prod spider:  `lsof -ni | grep nginx | grep -iv listen | wc -l`" >> /var/log/Ddos/Ddos.log

      # 添加一个iptablesi规则，对后续的任何数据包的重置
      iptables -I INPUT -s $ip -p tcp -j REJECT --reject-with tcp-reset
    fi
  done
  sleep 60
done
exit 0
