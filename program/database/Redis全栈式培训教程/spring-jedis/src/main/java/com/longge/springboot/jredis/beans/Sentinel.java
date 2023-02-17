package com.longge.springboot.jredis.beans;

import java.util.HashSet;
import java.util.Set;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.stereotype.Component;

import redis.clients.jedis.JedisPoolConfig;
import redis.clients.jedis.JedisSentinelPool;

/**
 * 哨兵对象构建
 */
@Component
public class Sentinel {
    @Value("${jedis.sentinel.host1}")
    private String host1;
    @Value("${jedis.sentinel.host2}")
    private String host2;
    @Value("${jedis.sentinel.host3}")
    private String host3;

    @Bean
    public JedisSentinelPool jedisSentinel(JedisPoolConfig jedisPoolConfig) {
        Set<String> sentinels = new HashSet<String>();
        sentinels.add(this.host1);
        sentinels.add(this.host2);
        sentinels.add(this.host3);
        JedisSentinelPool jspool = new JedisSentinelPool("mymaster", sentinels, jedisPoolConfig, 10000);
        return jspool;
    }
}
