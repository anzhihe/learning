
package com.longge.redis.a17;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import com.longge.redis.comm.Utils;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;

/**
 * 章节：17.9.分布式锁场景应用
 * 功能：使用Lua脚本(包含SETNX + EXPIRE两条指令)
 * 问题：锁过期释放了，业务还没执行完；锁被别的线程误删
 */
public class A9_4_lock4 extends Thread {
    private Jedis jedis = null;

    public A9_4_lock4() {
        this.jedis = this.init();

    }

    public void initData() {
        this.jedis.del("test_4");
    }

    public Jedis init() {
        JedisPoolConfig config = Utils.getRedisPoolConfig();
        JedisPool jedisPool = Utils.getJedisPool(config);
        Jedis jedis = jedisPool.getResource();
        return jedis;
    }

    /**
     * 模拟使用Lua脚本(包含SETNX + EXPIRE两条指令)
     */
    public void demo() {
        String lua_scripts = "if redis.call('setnx',KEYS[1],ARGV[1]) == 1 then" +
                " redis.call('expire',KEYS[1],ARGV[2]) return '1' else return '0' end";
        List<String> args = new ArrayList<String>();
        args.add("1");
        args.add("10");
        Object result = jedis.eval(lua_scripts, Collections.singletonList("test_4"), args);
        if (result.equals("1")) {
            System.out.println("抢锁成功");
        } else {
            System.out.println("抢锁失败");
        }
        try {
            Thread.sleep(100L);
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            if (result.equals("1")) {
                this.jedis.del("test_4");
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
        A9_4_lock4 app = new A9_4_lock4();
        app.initData();
        for (int i = 0; i < 2; i++) {
            A9_4_lock4 app1 = new A9_4_lock4();
            app1.start();
        }
        while (true) {
            Thread.sleep(1000L);
        }
    }

}
