
package com.longge.redis.a6.A2;

import com.longge.redis.comm.Utils;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;

/**
 * 章节：6.2.Redis的发布与订阅
 * 功能：发布/订阅演示
 */
public class Simple {
    public Jedis init() {
        JedisPoolConfig config = Utils.getRedisPoolConfig();
        try (JedisPool jedisPool = Utils.getJedisPool(config)) {
            Jedis jedis = jedisPool.getResource();
            return jedis;
        }
    }

    public static void main(String[] args) {
        Simple app = new Simple();
        Jedis jedis = app.init();
        SubListen subListen = new SubListen();
        jedis.subscribe(subListen, "test_channel".getBytes());
        jedis.close();
    }
}
