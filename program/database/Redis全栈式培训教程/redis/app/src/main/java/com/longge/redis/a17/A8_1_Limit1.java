package com.longge.redis.a17;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;

import com.longge.redis.comm.Utils;

import redis.clients.jedis.JedisPoolConfig;
import redis.clients.jedis.params.SetParams;

/**
 * 章节：17.8.请求限流场景
 * 功能：请求限流场景-计数器算法
 */
public class A8_1_Limit1 {
    private Jedis jedis = null;
    public static String limit1 = "limit1";
    public static long speed = 1;

    public Jedis init() {
        JedisPoolConfig config = Utils.getRedisPoolConfig();
        try (JedisPool jedisPool = Utils.getJedisPool(config)) {
            Jedis jedis = jedisPool.getResource();
            return jedis;
        }
    }

    public A8_1_Limit1() {
        this.jedis = this.init();
    }

    /**
     * 模拟请求
     * 
     * @throws InterruptedException
     */
    public void request() throws InterruptedException {
        SetParams setParam = new SetParams();
        setParam.nx();
        setParam.ex(1);
        // 如果key不存在，则将key过期时间设为1秒，并且值为0
        String val = this.jedis.set(A8_1_Limit1.limit1, "0", setParam);
        if ("OK".equals(val)) {
            System.out.println("正常请求");
        }
        // 如果存在则将计数器+1
        else {
            // 假设有2个人同时进行,如果这时候key刚好失效
            long num = this.jedis.incr(A8_1_Limit1.limit1);
            if (num > A8_1_Limit1.speed) {
                System.out.println("请求被限制");
                Thread.sleep(500L);
            } else {
                System.out.println("正常请求");
            }
            // 防止key永久生效
            if (this.jedis.ttl(A8_1_Limit1.limit1) < 0) {
                this.jedis.expire(A8_1_Limit1.limit1, 1);
            }
        }
    }

    public static void main(String[] args) throws InterruptedException {
        A8_1_Limit1 app = new A8_1_Limit1();
        for (int i = 0; i < 1000; i++) {
            app.request();
            try {
                Thread.sleep(200L);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
