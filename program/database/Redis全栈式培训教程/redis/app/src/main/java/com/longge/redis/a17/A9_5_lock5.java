package com.longge.redis.a17;

import java.util.Collections;

import com.longge.redis.comm.Utils;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;
import redis.clients.jedis.params.SetParams;

/**
 * 章节：17.9.分布式锁场景应用
 * 功能：SET EX PX NX + 校验唯一随机值,再释放锁
 * 问题：锁过期释放，业务没执行完
 */
public class A9_5_lock5 extends Thread {
    private Jedis jedis = null;

    public A9_5_lock5() {
        this.jedis = this.init();
    }

    public void initData() {
        this.jedis.del("test_5");
    }

    public Jedis init() {
        JedisPoolConfig config = Utils.getRedisPoolConfig();
        try (JedisPool jedisPool = Utils.getJedisPool(config)) {
            Jedis jedis = jedisPool.getResource();
            return jedis;
        }
    }

    /**
     * 模拟SET EX PX NX + 校验唯一随机值,再释放锁
     */
    public void demo() {
        SetParams params = new SetParams();
        params.nx();
        params.ex(10);
        String timestamp = System.currentTimeMillis() + "";
        String rtn = jedis.set("test_5", timestamp, params);
        try {
            if ("OK".equals(rtn)) {
                System.out.println("抢锁成功");
            } else {
                System.out.println("抢锁失败");
                return;
            }
            // 这里模拟业务处理
            Thread.sleep(100L);
        } catch (Exception ex) {
            ex.printStackTrace();
        } finally {
            if ("OK".equals(rtn)) {
                this.jedis.eval(
                        "if redis.call('get',KEYS[1]) == ARGV[1] then return redis.call('del',KEYS[1]) else return 0 end;",
                        Collections.singletonList("test_5"), Collections.singletonList(timestamp));
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
        A9_5_lock5 app = new A9_5_lock5();
        app.initData();
        for (int i = 0; i < 5; i++) {
            A9_5_lock5 thread = new A9_5_lock5();
            thread.start();
        }
        while (true) {
            Thread.sleep(1000L);
        }
    }

}
