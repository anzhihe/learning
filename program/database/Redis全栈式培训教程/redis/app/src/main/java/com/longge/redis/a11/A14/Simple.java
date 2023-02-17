
package com.longge.redis.a11.A14;

import com.longge.redis.comm.Utils;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;

/**
 * 章节：11.14.事件通知
 * 功能：事件通知过期事件演示
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
        jedis.subscribe(subListen, "__keyevent@0__:expired".getBytes());
        jedis.close();
    }
}
