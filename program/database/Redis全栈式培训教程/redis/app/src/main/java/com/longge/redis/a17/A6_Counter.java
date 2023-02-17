/**
 * 章节：17.6.计数器场景应用
 * 功能：计算器场景应用
 */
package com.longge.redis.a17;

import com.longge.redis.comm.Utils;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;

class MyThread extends Thread {
    private A6_Counter app = null;

    public MyThread() {
        this.app = new A6_Counter();
    }

    @Override
    public void run() {
        // 击点100次
        for (int i = 0; i < 100; i++) {
            this.app.clickTest();
        }
        System.out.println("执行完毕……");
    }

    @Override
    public synchronized void start() {
        super.start();
    }

}

public class A6_Counter {
    public static String key = "counter";
    private Jedis jedis = null;

    public Jedis init() {
        JedisPoolConfig config = Utils.getRedisPoolConfig();
        JedisPool jedisPool = Utils.getJedisPool(config);
        Jedis jedis = jedisPool.getResource();
        return jedis;
    }

    public A6_Counter() {
        this.jedis = this.init();
    }

    /**
     * 初始化数据
     */
    public void initData() {
        this.jedis.set(A6_Counter.key, "0");
    }

    /**
     * 模拟点击
     */
    public void clickTest() {
        this.jedis.incr(A6_Counter.key);
    }

    /**
     * 模拟查询点击数
     */
    public String getCounter() {
        return this.jedis.get(A6_Counter.key);
    }

    public static void main(String[] args) {
        A6_Counter app = new A6_Counter();
        app.initData();
        // 模拟10个用户
        for (int i = 0; i < 10; i++) {
            MyThread mythread = new MyThread();
            mythread.start();
        }
        while (true) {
            try {
                Thread.sleep(1000);
                String rtn = app.getCounter();
                System.out.println(rtn);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
