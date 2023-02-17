/**
 * 章节：17.1.Jedis连接Redis源码
 * 功能：Jedis连接单机
 */
package com.longge.redis.a17;

import com.longge.redis.comm.Utils;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;

public class A1_1_simple {
    public Jedis init() {
        JedisPoolConfig config = Utils.getRedisPoolConfig();
        try (JedisPool jedisPool = Utils.getJedisPool(config)) {
            Jedis jedis = jedisPool.getResource();
            return jedis;
        }
    }

    public static void main(String[] args) {
        A1_1_simple app = new A1_1_simple();
        Jedis jedis = app.init();
        jedis.set("a1", "val1");
        String a1 = jedis.get("a1");
        System.out.println("返回值为：" + a1);
        jedis.close();
    }
}
