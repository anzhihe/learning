/**
 * 章节：17.8.请求限流场景
 * 功能：请求限流场景-漏桶算法
 */
package com.longge.redis.a17;

import com.longge.redis.comm.Utils;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;
import redis.clients.jedis.params.SetParams;

class MyThread2 extends Thread {
    private Jedis jedis = null;

    public MyThread2() {
        this.jedis = new A8_3_Limit3().init();
    }

    @Override
    public void run() {
        // 通过Redis用于控制服务端的全局匀速消费
        while (true) {
            SetParams setParam = new SetParams();
            setParam.nx();
            setParam.ex(1);
            String val = this.jedis.set("limit3", "1", setParam);
            if ("OK".equals(val)) {
                this.jedis.lpop("mylist");
                // 这里处理我们的业务[每秒钟处理一次]
                System.out.println("每秒钟一次");

            }
            try {
                Thread.sleep(100L);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    @Override
    public synchronized void start() {
        super.start();
    }

}

public class A8_3_Limit3 {
    private Jedis jedis = null;

    public Jedis init() {
        JedisPoolConfig config = Utils.getRedisPoolConfig();
        JedisPool jedisPool = Utils.getJedisPool(config);
        Jedis jedis = jedisPool.getResource();
        return jedis;
    }

    public void initData() {
        this.jedis.del("mylist");
    }

    public A8_3_Limit3() {
        this.jedis = this.init();
    }

    /**
     * 模拟客户端请求,确保桶容量操作的原子性
     */
    public void request() {
        // 注意这一段脚本是一个单线程、原子性运行的
        String script = "local len=redis.call('llen','mylist');if (len<5) then redis.call('lpush','mylist','1');return '1' end;return '0'";
        Object rtn = this.jedis.eval(script);
        if ("1".equals(rtn)) {
            System.out.println("正常请求");
        } else {
            System.out.println("请求限流");
        }
    }

    public static void main(String[] args) {
        A8_3_Limit3 app = new A8_3_Limit3();
        app.initData();
        for (int i = 0; i < 3; i++) {
            MyThread2 mythread = new MyThread2();
            mythread.start();
        }
        while (true) {
            try {
                Thread.sleep(500L);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            app.request();
        }
    }
}
