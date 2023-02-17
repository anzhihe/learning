package com.longge.redis.a17;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;

import java.util.UUID;

import com.longge.redis.comm.Utils;

import redis.clients.jedis.JedisPoolConfig;

/**
 * 章节：17.8.请求限流场景
 * 功能：请求限流场景-滑动窗口算法
 */
public class A8_2_Limit2 {
    private Jedis jedis = null;
    public static String limit2 = "limit2";
    public static long speed = 1;

    public Jedis init() {
        JedisPoolConfig config = Utils.getRedisPoolConfig();
        try (JedisPool jedisPool = Utils.getJedisPool(config)) {
            Jedis jedis = jedisPool.getResource();
            return jedis;
        }
    }

    public A8_2_Limit2() {
        this.jedis = this.init();
    }

    /**
     * 模拟请求
     * 
     * @throws InterruptedException
     */
    public void request() throws InterruptedException {
        long timestamp = System.currentTimeMillis();
        // 计算滑动窗口类的数量
        long sum = this.jedis.zcount(A8_2_Limit2.limit2, timestamp - 1000L, timestamp);
        if (sum >= A8_2_Limit2.speed) {
            System.out.println("请求限流");
            Thread.sleep(200L);
        } else {
            this.jedis.zadd(A8_2_Limit2.limit2, timestamp, UUID.randomUUID().toString());
            System.out.println("正常请求");
        }
        // 随机删除，防止zset数量太多
        if (timestamp % 10 == 0) {
            this.jedis.zremrangeByScore(A8_2_Limit2.limit2, timestamp - 1000 * 3600 * 24, timestamp - 1000 * 10);
        }
    }

    public static void main(String[] args) throws InterruptedException {
        A8_2_Limit2 app = new A8_2_Limit2();
        for (int i = 0; i < 1000; i++) {
            try {
                app.request();
                Thread.sleep(100L);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
