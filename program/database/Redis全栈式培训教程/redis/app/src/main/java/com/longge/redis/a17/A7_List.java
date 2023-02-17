package com.longge.redis.a17;

import java.util.List;
import java.util.Random;
import java.util.concurrent.atomic.AtomicInteger;

import com.longge.redis.comm.Utils;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;

/**
 * 章节：17.7.最新消息场景应用
 * 功能：最新消息场景应用
 */
class MyThread1 extends Thread {
    public static AtomicInteger index = new AtomicInteger(0);
    private A7_List app;

    public MyThread1() {
        this.app = new A7_List();
    }

    @Override
    public void run() {
        Random rd = new Random();
        while (true) {
            try {
                Thread.sleep(rd.nextInt(5) * 1000 + 1);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            // 模拟回帖
            this.app.addMessage("回帖:" + (index.incrementAndGet()));
        }
    }

    @Override
    public synchronized void start() {
        super.start();
    }

}

public class A7_List {
    private Jedis jedis = null;
    public static String key = "list";

    public Jedis init() {
        JedisPoolConfig config = Utils.getRedisPoolConfig();
        JedisPool jedisPool = Utils.getJedisPool(config);
        Jedis jedis = jedisPool.getResource();
        return jedis;
    }

    public A7_List() {
        this.jedis = this.init();
    }

    public void initData() {
        this.jedis.del(A7_List.key);
        this.jedis.lpush(A7_List.key, "回帖:0");
        this.jedis.ltrim(key, 0, 10);
    }

    /**
     * 模拟回帖
     * 
     * @param msg
     */
    public void addMessage(String msg) {
        this.jedis.lpush(A7_List.key, msg);
    }

    /**
     * 获取最新回帖列表
     * 
     * @return
     */
    public List<String> getMessage() {
        return this.jedis.lrange(A7_List.key, 0, 10);
    }

    public static void main(String[] args) {
        A7_List app = new A7_List();
        app.initData();
        for (int i = 0; i < 5; i++) {
            MyThread1 mythread = new MyThread1();
            mythread.start();
        }
        while (true) {
            List<String> list = app.getMessage();
            System.out.println("当前回帖:" + list);
            try {
                Thread.sleep(1000L);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
