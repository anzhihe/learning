
package com.longge.redis.a6;

import com.longge.redis.comm.Utils;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;
import redis.clients.jedis.Pipeline;

/**
 * 章节：6.1.Redis中的管道原理
 * 功能：管道演示
 */
public class A1_Pipline {
    public Jedis init() {
        JedisPoolConfig config = Utils.getRedisPoolConfig();
        try (JedisPool jedisPool = Utils.getJedisPool(config)) {
            Jedis jedis = jedisPool.getResource();
            return jedis;
        }
    }

    public static void main(String[] args) {
        A1_Pipline app = new A1_Pipline();
        Jedis jedis = app.init();
        // 管道开始
        Pipeline p = jedis.pipelined();
        for (int i = 0; i < 100000; i++) {
            p.set("a" + i, "a" + i);
        }
        p.sync();
        p.close();
        jedis.close();
    }
}
