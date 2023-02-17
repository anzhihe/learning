
package com.longge.redis.a17;

import com.longge.redis.comm.Utils;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;

/**
 * 章节：17.9.分布式锁场景应用
 * 功能：SETNX + EXPIRE
 * 问题：有可能选成锁不释放问题
 */
public class A9_1_lock1 {
    private Jedis jedis = null;

    public A9_1_lock1() {
        this.jedis = this.init();
    }

    public Jedis init() {
        JedisPoolConfig config = Utils.getRedisPoolConfig();
        try (JedisPool jedisPool = Utils.getJedisPool(config)) {
            Jedis jedis = jedisPool.getResource();
            return jedis;
        }
    }

    /**
     * 模拟setnx+expire
     */
    public void demo() {
        // 先抢锁,这里的Key我们可以理解为业务上需要竞争的资源
        if (this.jedis.setnx("test_1", "1") == 1) {
            // 当在这一步执行前出现问题时,可能这个锁就永远不会释放了
            this.jedis.expire("test_1", 10);
            System.out.println("抢锁成功");
        } else {
            System.out.println("抢锁失败");
        }
    }

    public static void main(String[] args) throws InterruptedException {
        A9_1_lock1 app = new A9_1_lock1();
        while (true) {
            Thread.sleep(1000L);
            app.demo();
        }
    }

}
