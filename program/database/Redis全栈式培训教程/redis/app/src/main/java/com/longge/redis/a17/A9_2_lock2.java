
package com.longge.redis.a17;

import com.longge.redis.comm.Utils;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;

/**
 * 章节：17.9.分布式锁场景应用
 * 功能：SETNX + value值是(系统时间+过期时间)
 * 问题：锁的时间会被其它线程覆盖, 有误差
 */
public class A9_2_lock2 {
    private Jedis jedis = null;

    public A9_2_lock2() {
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
     * 模拟SETNX + value值是(系统时间+过期时间)
     */
    public void demo() {
        long expireTime = 1000 * 10L;
        long expires = System.currentTimeMillis() + expireTime; // 系统时间+设置的过期时间
        String expiresStr = String.valueOf(expires);

        // 如果当前锁不存在，返回加锁成功
        if (jedis.setnx("test_2", expiresStr) == 1) {
            System.out.println("抢锁成功");
            return;
        }
        // 如果锁已经存在，需进一步判断锁过期时间
        String currentValueStr = jedis.get("test_2");
        // 如果获取到的过期时间<系统当前时间，表示已经过期
        if (currentValueStr != null && Long.parseLong(currentValueStr) < System.currentTimeMillis()) {
            // 取出老值，并设定新值，这里会产生多线程的覆盖问题
            String oldValueStr = jedis.getSet("test_2", expiresStr);
            // 在多线程时，永远只有一个线程能判断成功
            if (oldValueStr != null && oldValueStr.equals(currentValueStr)) {
                System.out.println("抢锁成功");
            } else {
                System.out.println("抢锁失败");
            }
        } else {
            System.out.println("抢锁失败");
        }

    }

    public static void main(String[] args) throws InterruptedException {
        A9_2_lock2 app = new A9_2_lock2();
        while (true) {
            Thread.sleep(1000L);
            app.demo();
        }
    }

}
