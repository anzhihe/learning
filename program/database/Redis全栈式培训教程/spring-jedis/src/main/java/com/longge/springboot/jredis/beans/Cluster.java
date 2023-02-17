package com.longge.springboot.jredis.beans;

import java.util.HashSet;
import java.util.Set;

import org.springframework.context.annotation.Bean;
import org.springframework.stereotype.Component;

import redis.clients.jedis.HostAndPort;
import redis.clients.jedis.JedisCluster;
import redis.clients.jedis.JedisPoolConfig;

/**
 * cluster集群对象构建
 */
@Component
public class Cluster {
    @Bean
    public JedisCluster jedisCluster(JedisPoolConfig jedisPoolConfig) {
        Set<HostAndPort> nodeSet = new HashSet<>();
        nodeSet.add(new HostAndPort("172.16.122.101", 6379));
        nodeSet.add(new HostAndPort("172.16.122.101", 6380));
        nodeSet.add(new HostAndPort("172.16.122.102", 6379));
        nodeSet.add(new HostAndPort("172.16.122.102", 6380));
        nodeSet.add(new HostAndPort("172.16.122.103", 6379));
        nodeSet.add(new HostAndPort("172.16.122.103", 6380));
        JedisCluster jedisCluster = new JedisCluster(nodeSet, 2000, jedisPoolConfig);
        return jedisCluster;
    }
}
