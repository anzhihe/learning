/**
 * 章节：17.5.排行榜场景用应用
 * 功能：直播间排序
 */
package com.longge.redis.a17;

import java.util.List;
import java.util.Random;

import com.longge.redis.comm.Utils;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;
import redis.clients.jedis.resps.Tuple;

public class A5_Zset {
    public static String key = "mems";
    private Jedis jedis = null;

    public Jedis init() {
        JedisPoolConfig config = Utils.getRedisPoolConfig();
        try (JedisPool jedisPool = Utils.getJedisPool(config)) {
            Jedis jedis = jedisPool.getResource();
            return jedis;
        }
    }

    public A5_Zset() {
        this.jedis = this.init();
        this.jedis.del(A5_Zset.key);
    }

    /**
     * 模拟某个成员为主播送红心数
     * 
     * @param key
     * @param member
     * @param increment
     */
    public void addScore(String key, String member, Double increment) {
        this.jedis.zincrby(key, increment, member);
    }

    /**
     * 模拟送红心的某个用户
     * 
     * @param start
     * @param max
     * @return
     */
    public int getRamNum(int max) {
        Random rd = new Random();
        int num1 = rd.nextInt(3);
        int num = 0;
        if (num1 == 0) {
            num = rd.nextInt(8);
        } else {
            num = rd.nextInt(max);
        }
        return num;
    }

    /**
     * 查询排行榜top10
     */
    public List<Tuple> sortMems() {
        List<Tuple> list = this.jedis.zrevrangeWithScores(A5_Zset.key, 0, 9);
        return list;
    }

    public static void main(String[] args) {
        A5_Zset app = new A5_Zset();
        // 模拟500次送红心
        for (int i = 0; i < 500; i++) {
            if (i % 10 == 0) {
                System.out.println("当前进度:" + i);
            }
            // 模拟谁送红心
            int num = app.getRamNum(100);
            // 关键代码实现，模拟某个用户送红心
            app.addScore(key, A5_Zset.key + num, Double.parseDouble("1"));
        }
        // 查询排行榜top10
        List<Tuple> list = app.sortMems();
        System.out.println(list);
    }
}
