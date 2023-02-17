package com.longge.springboot.jredis.beans;

import java.time.Duration;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.stereotype.Component;

import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;

/**
 * 单点对象构建
 */
@Component
public class Simple {
    @Value("${jedis.simple.host}")
    private String host;
    @Value("${jedis.simple.password}")
    private String password;
    @Value("${jedis.simple.port}")
    private int port;
    @Value("${jedis.simple.timeout}")
    private int timeout;
    @Value("${jedis.simple.maxTotal}")
    private int maxActive;
    @Value("${jedis.simple.maxIdle}")
    private int maxIdle;
    @Value("${jedis.simple.minIdle}")
    private int minIdle;
    @Value("${jedis.simple.maxWaitMillis}")
    private long maxWaitMillis;
    @Value("${jedis.simple.testOnBorrow}")
    private boolean testOnBorrow;

    @Bean
    public JedisPoolConfig jedisPoolConfig() {
        JedisPoolConfig jedisPoolConfig = new JedisPoolConfig();
        jedisPoolConfig.setMaxTotal(maxActive);
        jedisPoolConfig.setMaxIdle(maxIdle);
        jedisPoolConfig.setMinIdle(minIdle);
        jedisPoolConfig.setMaxWait(Duration.ofMillis(maxWaitMillis));
        jedisPoolConfig.setTestOnBorrow(testOnBorrow);
        return jedisPoolConfig;
    }

    @Bean
    public JedisPool jedisPool(JedisPoolConfig jedisPoolConfig) {
        return new JedisPool(jedisPoolConfig, host, port, timeout);
    }
}
