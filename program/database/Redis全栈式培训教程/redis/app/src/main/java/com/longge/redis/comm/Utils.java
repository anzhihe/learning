package com.longge.redis.comm;

import java.time.Duration;

import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;

public class Utils {
    public static JedisPool jedisPool = null;
    public static JedisPoolConfig config = null;

    public static synchronized JedisPoolConfig getRedisPoolConfig() {
        if (null == config) {
            config = new JedisPoolConfig();
            config.setMaxTotal(100);
            config.setMaxIdle(1);
            // config.setMaxWaitMillis(1000 * 100);
            config.setMaxWait(Duration.ofMillis(1000 * 10));
            config.setTestOnBorrow(true);
        }
        return config;
    }

    public static synchronized JedisPool getJedisPool(JedisPoolConfig config) {
        if (null == jedisPool) {
            jedisPool = new JedisPool(config, Constants.HOST, Constants.PORT_6379, Constants.TIME_OUT);
        }
        return jedisPool;
    }
}
