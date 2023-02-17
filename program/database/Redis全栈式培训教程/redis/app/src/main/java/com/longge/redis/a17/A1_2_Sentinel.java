
/**
 * 章节：17.1.Jedis连接Redis源码
 * 功能：Jedis连接Sentinel集群
 */
package com.longge.redis.a17;

import java.util.HashSet;
import java.util.Set;

import com.longge.redis.comm.Constants;
import com.longge.redis.comm.Utils;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPoolConfig;
import redis.clients.jedis.JedisSentinelPool;

public class A1_2_Sentinel {
    public Jedis init() {
        JedisPoolConfig poolConfig = Utils.getRedisPoolConfig();
        Set<String> sentinels = new HashSet<String>();
        sentinels.add(Constants.HOST + ":" + Constants.PORT_26378);
        sentinels.add(Constants.HOST + ":" + Constants.PORT_26379);
        sentinels.add(Constants.HOST + ":" + Constants.PORT_26380);
        try (JedisSentinelPool jspool = new JedisSentinelPool("mymaster", sentinels, poolConfig, Constants.TIME_OUT)) {
            return jspool.getResource();
        }
    }

    public static void main(String[] args) {
        A1_1_simple app = new A1_1_simple();
        Jedis jedis = app.init();
        jedis.set("a1", "val1");
        String a1 = jedis.get("a1");
        System.out.println("返回值为：" + a1);
        for (int i = 0; i < 10000; i++) {
            if (i % 100 == 0) {
                System.out.println("当前：" + i + "条");
            }
            jedis.set("a" + i, "a" + i);
        }
        jedis.close();
    }
}
