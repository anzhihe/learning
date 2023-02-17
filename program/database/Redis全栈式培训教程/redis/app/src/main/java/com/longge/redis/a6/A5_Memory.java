
package com.longge.redis.a6;

import com.longge.redis.comm.Utils;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;

/**
 * 章节：6.5.Redis内存淘汰策略
 * 功能：淘汰策略演示
 */
public class A5_Memory {
    public Jedis init() {
        JedisPoolConfig config = Utils.getRedisPoolConfig();
        try (JedisPool jedisPool = Utils.getJedisPool(config)) {
            Jedis jedis = jedisPool.getResource();
            return jedis;
        }
    }

    public static void main(String[] args) {
        A5_Memory app = new A5_Memory();
        Jedis jedis = app.init();
        jedis.set("a1", "val1");
        StringBuffer sb = new StringBuffer();
        //每次key大小为4K
        for (int i = 0; i < 4096; i++) {
            sb.append("a");
        }
        for (int i = 0; i < 100000; i++) {
            jedis.set("a" + i, sb.toString() + i);
            if (i % 1000 == 0) {
                System.out.println("当前条数：" + i);
            }
        }
        jedis.close();
    }
}
