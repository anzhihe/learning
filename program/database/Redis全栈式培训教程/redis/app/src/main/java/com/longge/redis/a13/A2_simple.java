package com.longge.redis.a13;

import com.longge.redis.comm.Utils;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;
import redis.clients.jedis.Pipeline;

/**
 * 章节：13.2 resp方式造数据程序
 * 功能：造数据程序
 */
public class A2_simple {
    public Jedis init() {
        JedisPoolConfig config = Utils.getRedisPoolConfig();
        try (JedisPool jedisPool = Utils.getJedisPool(config)) {
            Jedis jedis = jedisPool.getResource();
            return jedis;
        }
    }

    public static void main(String[] args) {
        A2_simple app = new A2_simple();
        Jedis jedis = app.init();
        int start = 0;
        for (int j = 0; j < 2; j++) {
            int index = start + 10000;
            Pipeline p = jedis.pipelined();
            for (; start < index; start++) {
                p.set("a" + start, "a" + start);
            }
            p.sync();
            p.close();
            System.out.println("处理条数：" + (start + 1));
        }
        jedis.close();
    }
}
