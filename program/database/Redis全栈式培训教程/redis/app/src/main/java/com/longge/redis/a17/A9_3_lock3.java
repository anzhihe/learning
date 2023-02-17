
package com.longge.redis.a17;

import com.longge.redis.comm.Utils;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;
import redis.clients.jedis.params.SetParams;

/**
 * 章节：17.9.分布式锁场景应用
 * 功能：SET的扩展命令（SET EX PX NX）
 * 问题：锁过期释放了，业务还没执行完；锁被别的线程误删
 */
public class A9_3_lock3 extends Thread {
    private Jedis jedis = null;

    public A9_3_lock3() {
        this.jedis = this.init();
    }

    public Jedis init() {
        JedisPoolConfig config = Utils.getRedisPoolConfig();
        JedisPool jedisPool = Utils.getJedisPool(config);
        Jedis jedis = jedisPool.getResource();
        return jedis;
    }

    public void initData() {
        this.jedis.del("test_3");
    }

    /**
     * 模拟SET的扩展命令（SET EX PX NX）
     */
    public void demo() {
        SetParams params = new SetParams();
        params.nx();
        params.ex(10);
        String rtn = jedis.set("test_3", "1", params);
        try {
            if ("OK".equals(rtn)) {
                System.out.println("抢锁成功");
                // 业务处理 
            } else {
                System.out.println("抢锁失败");
            }
            Thread.sleep(100L);
        } catch (Exception ex) {
            ex.printStackTrace();
        } finally {
            if ("OK".equals(rtn)) {
                this.jedis.del("test_3");
            }
        }

    }

    @Override
    public void run() {
        while (true) {
            try {
                Thread.sleep(1000L);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            this.demo();
        }
    }

    @Override
    public synchronized void start() {
        super.start();
    }

    public static void main(String[] args) throws InterruptedException {
        A9_3_lock3 app = new A9_3_lock3();
        app.initData();
        for (int i = 0; i < 2; i++) {
            A9_3_lock3 app1 = new A9_3_lock3();
            app1.start();
        }
        while (true) {
            Thread.sleep(1000L);
        }
    }

}
