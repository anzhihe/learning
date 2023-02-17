/**
 * 章节：17.2.热点数据加速DB
 * 功能：热点加速
 */
package com.longge.redis.a17;

import com.longge.redis.comm.Utils;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;
import redis.clients.jedis.params.SetParams;

public class A2_Cache {
    private Jedis jedis = null;

    public Jedis init() {
        JedisPoolConfig config = Utils.getRedisPoolConfig();
        try (JedisPool jedisPool = Utils.getJedisPool(config)) {
            Jedis jedis = jedisPool.getResource();
            return jedis;
        }
    }

    public A2_Cache() {
        this.jedis = this.init();
    }

    /**
     * 模拟数据库返回
     * 
     * @param key
     * @return
     */
    public String getFromDb(String key) {
        return key + "-value";
    }

    /**
     * 从缓存取值
     * 
     * @param key
     * @return
     */
    public String get(String key) {
        return this.jedis.get(key);
    }

    /**
     * 更新缓存
     * 
     * @param key
     * @param val
     */
    public void set(String key, String val) {
        SetParams setParam = new SetParams();
        setParam.ex(10);
        this.jedis.set(key, val, setParam);
    }

    public static void main(String[] args) {
        A2_Cache app = new A2_Cache();
        String key = "key1";
        String rtn = app.get(key);
        if (null == rtn || "".equals(rtn)) {
            System.out.println("缓存未命中");
            rtn = app.getFromDb(key);
            if (null != rtn || !"".equals(rtn)) {
                app.set(key, rtn);
                System.out.println("更新缓存");
            }
            // 否则业务上不存在
        } else {
            System.out.println("缓存命中");
        }

    }
}
