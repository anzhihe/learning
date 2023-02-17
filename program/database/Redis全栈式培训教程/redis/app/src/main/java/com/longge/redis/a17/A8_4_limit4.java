/**
 * 章节：17.8.请求限流场景
 * 功能：请求限流场景-令牌桶算法
 */
package com.longge.redis.a17;

import com.longge.redis.comm.Utils;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;

class MyThread4 extends Thread {
    private Jedis jedis = null;

    public MyThread4(A8_4_limit4 app) {
        this.jedis = app.init();
    }

    @Override
    public void run() {
        int i = 0;
        while (true) {
            try {
                Thread.sleep(1000L);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            // 定时往里面放令牌
            this.jedis.lpush(A8_4_limit4.key, "1");
            // 防止令牌太多……
            if (i % 10 == 0) {
                this.jedis.ltrim(A8_4_limit4.key, 0, 10);
                i = 0;
            }
        }
    }

    @Override
    public synchronized void start() {
        super.start();
    }
}

public class A8_4_limit4 {
    public static String key = "limit4";
    private Jedis jedis = null;

    public Jedis init() {
        JedisPoolConfig config = Utils.getRedisPoolConfig();
        JedisPool jedisPool = Utils.getJedisPool(config);
        Jedis jedis = jedisPool.getResource();
        return jedis;

    }

    public A8_4_limit4() {
        this.jedis = this.init();
    }

    public void request() {
        String token = this.jedis.lpop(A8_4_limit4.key);
        if (null == token) {
            System.out.println("请求限流");
        } else {
            System.out.println("正常请求");
        }
    }

    public static void main(String[] args) throws InterruptedException {
        A8_4_limit4 app = new A8_4_limit4();
        new MyThread4(app).start();
        while (true) {
            Thread.sleep(800L);
            app.request();
        }
    }
}
