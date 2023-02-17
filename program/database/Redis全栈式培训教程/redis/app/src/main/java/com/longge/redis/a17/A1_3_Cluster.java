/**
 * 章节：17.1.Jedis连接Redis源码
 * 功能：Jedis连接Cluster
 */
package com.longge.redis.a17;

import java.util.HashSet;
import java.util.Set;

import com.longge.redis.comm.Constants;

import redis.clients.jedis.ConnectionPoolConfig;
import redis.clients.jedis.HostAndPort;
import redis.clients.jedis.JedisCluster;

public class A1_3_Cluster {
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
        A1_3_Cluster app = new A1_3_Cluster();
        JedisCluster jedisCluster = app.init();
        jedisCluster.set("a1", "val1");
        String a1 = jedisCluster.get("a1");
        System.out.println("返回值为：" + a1);
        jedisCluster.close();
    }
}
