/**
 * 章节：17.1.Jedis连接Redis源码
 * 功能：Jedis连接Cluster
 */
package com.longge.redis.a9;

import java.util.HashSet;
import java.util.Set;

import com.longge.redis.comm.Constants;

import redis.clients.jedis.ConnectionPoolConfig;
import redis.clients.jedis.HostAndPort;
import redis.clients.jedis.JedisCluster;

public class A6_Cluster {
    public JedisCluster init() {
        Set<HostAndPort> jedisClusterNodes = new HashSet<HostAndPort>();
        jedisClusterNodes.add(new HostAndPort(Constants.HOST, Constants.PORT_6381));
        jedisClusterNodes.add(new HostAndPort(Constants.HOST, Constants.PORT_6382));
        jedisClusterNodes.add(new HostAndPort(Constants.HOST, Constants.PORT_6383));
        jedisClusterNodes.add(new HostAndPort(Constants.HOST, Constants.PORT_6384));
        jedisClusterNodes.add(new HostAndPort(Constants.HOST, Constants.PORT_6385));
        jedisClusterNodes.add(new HostAndPort(Constants.HOST, Constants.PORT_6386));
        ConnectionPoolConfig cpc = new ConnectionPoolConfig();
        cpc.setMaxTotal(50);
        cpc.setMinIdle(1);
        cpc.setTestOnBorrow(true);
        JedisCluster jedisCluster = new JedisCluster(jedisClusterNodes, Constants.TIME_OUT, Constants.SO_TIMEOUT, cpc);
        return jedisCluster;
    }

    public static void main(String[] args) {
        A6_Cluster app = new A6_Cluster();
        JedisCluster jedisCluster = app.init();
        for (int i = 0; i < 1000; i++) {
            jedisCluster.set("a" + i, "a" + i);
            if (i % 100 == 0) {
                System.out.println("当前数量:" + i);
            }
        }
        System.out.println("初始数据完成");
        jedisCluster.close();
    }
}
