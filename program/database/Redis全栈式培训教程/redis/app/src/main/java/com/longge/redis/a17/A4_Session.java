
package com.longge.redis.a17;

import java.util.HashMap;
import java.util.Map;

import com.longge.redis.comm.Utils;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;

/**
 * 章节：17.4.共享会话场景应用
 * 功能：共享会话
 */
public class A4_Session {
    private Jedis jedis = null;
    private Map<String, String> sessionMap = new HashMap<String, String>();

    public Jedis init() {
        JedisPoolConfig config = Utils.getRedisPoolConfig();
        JedisPool jedisPool = Utils.getJedisPool(config);
        Jedis jedis = jedisPool.getResource();
        return jedis;

    }

    public A4_Session() {
        this.jedis = this.init();
    }

    /**
     * 模拟从Redis取Session
     */
    public String get(String key) {
        return this.jedis.get(key);
    }

    public void set(String key, String val) {
        this.jedis.set(key, val);
        this.jedis.expire(key, 100);
    }

    /**
     * 模拟Session过程
     * 
     * @param key
     * @return
     */

    public String getSession(String key) {
        // 优先从本地取
        if (this.sessionMap.containsKey(key)) {
            System.out.println("从本地取会话：" + key);
            return this.sessionMap.get(key);
        }
        // 取不到再从Redis取
        String session = this.get(key);
        // 两者均没有取到，则认为是新话
        if (null == session || "".equals(session)) {
            // 产生会话
            this.sessionMap.put(key, key);
            // 同时同步至redis
            this.set(key, key);
            System.out.println("产生新会话：" + key);
        }
        // 从Redis取得会话后要入本地
        else {
            System.out.println("从Redis取会话：" + key);
            this.sessionMap.put(key, key);
        }
        return this.sessionMap.get(key);
    }

    public static void main(String[] args) {
        A4_Session app = new A4_Session();
        // 模拟100次请求(10个用户)
        for (int i = 0; i < 100; i++) {
            app.getSession("session_" + (i % 10));
        }
    }
}
