
package com.longge.redis.a17;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import com.longge.redis.comm.Utils;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;
import redis.clients.jedis.params.SetParams;

/**
 * 章节：17.3.下单秒杀场景应用
 * 功能：下单秒杀场景应用
 */
public class A3_Seckill {
    public static List<String> offerList = Collections.synchronizedList(new ArrayList<String>());
    public static int secSize = 5;
    private Jedis jedis = null;

    public Jedis init() {
        JedisPoolConfig config = Utils.getRedisPoolConfig();
        JedisPool jedisPool = Utils.getJedisPool(config);
        Jedis jedis = jedisPool.getResource();
        return jedis;
    }

    public A3_Seckill() {
        this.jedis = this.init();
    }

    /**
     * 初始化商品以及开关数据
     */
    public void initList() {
        // 清除所有数据
        jedis.flushAll();
        // 设置秒杀未开始
        this.jedis.set("switch", "0");
        // 放入A4_Seckill.secSize个商品
        this.jedis.del("offer");
        for (int i = 0; i < A3_Seckill.secSize; i++) {
            this.jedis.lpush("offer", "offer_" + i);
        }
    }

    /**
     * 模拟抢购
     * 
     * @return
     */
    public String buy(String name) {
        String ifon = this.jedis.get("switch");
        if (!"1".equals(ifon)) {
            System.out.println("秒杀未开始");
            return null;
        }
        // 判断用户是否重复订购
        String ifbuy = this.jedis.get(name + "_buyed");
        if ("1".equals(ifbuy)) {
            return null;
        }
        // redis单个操作是线程安全的/原子性的,保证了商品不被重复抢
        // 大家想一下，用decr是否也能实现？
        String offer = null;
        try {
            SetParams setParam = new SetParams();
            setParam.nx();
            setParam.ex(5);
            // 防止用户争抢太频繁(5秒钟一次)
            String rtn = this.jedis.set(name, "1", setParam);
            if (null != rtn) {
                offer = this.jedis.lpop("offer");
                if (null != offer) {
                    A3_Seckill.offerList.add(name + "-" + offer);
                    this.jedis.set(name + "_buyed", "1");
                    System.out.println("秒杀成功");
                } else {
                    // System.out.println("秒杀失败");
                }
            }
        } catch (Exception ex) {
            ex.printStackTrace();
        } finally {
            // this.jedis.del(name);
        }
        return offer;
    }

    class ClientThread extends Thread {
        private String name = "";
        private A3_Seckill app = null;

        public ClientThread(String name) {
            this.name = name;
            this.app = new A3_Seckill();
        }

        @Override
        public synchronized void start() {
            super.start();
        }

        @Override
        public void run() {
            while (true) {
                try {
                    Thread.sleep(100L);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                app.buy(this.name);
            }
        }
    }

    public ClientThread create(String name) {
        ClientThread thread = new ClientThread(name);
        return thread;
    }

    public static void main(String[] args) {
        int size = 50;
        A3_Seckill app = new A3_Seckill();
        app.initList();
        ClientThread[] threads = new ClientThread[size];
        for (int i = 0; i < size; i++) {
            threads[i] = app.create("thread" + i);
        }
        for (int i = 0; i < size; i++) {
            threads[i].start();
        }
        while (true) {
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            if (A3_Seckill.offerList.size() >= A3_Seckill.secSize) {

                System.out.println(A3_Seckill.offerList);
                System.exit(0);
            }
        }
    }
}
