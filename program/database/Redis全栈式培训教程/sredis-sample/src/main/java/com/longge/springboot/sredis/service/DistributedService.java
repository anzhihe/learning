package com.longge.springboot.sredis.service;

import java.util.concurrent.atomic.AtomicInteger;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Service;

@Service
public class DistributedService {
    @Autowired
    private RedisTemplate<String, String> redisTemplate;
    // 可采用zk或者配置文件生成
    public static String nodeid = "1";
    public static long timestamp1 = -1;
    public static AtomicInteger int16 = new AtomicInteger(0);
    public static long timestamp2 = -1;

    /**
     * 模拟分布式ID
     * 
     * @param key
     * @return
     */
    public long newid(String key) {
        long id = this.redisTemplate.opsForValue().increment(key);
        return id;
    }

    /**
     * 分布式ID算法1,tps=1000(龙哥算法)
     * 
     * @param key
     * @return
     * @throws InterruptedException
     */
    public synchronized String lnewid(String key) throws InterruptedException {
        long ctimestamp = System.currentTimeMillis();
        if (ctimestamp == timestamp1) {
            Thread.sleep(1);
        }
        timestamp1 = ctimestamp;
        return nodeid + ctimestamp;
    }

    /**
     * 分布式ID算法2,tps=10000(龙哥算法)
     * 
     * @return
     */
    public static synchronized String getSeq16() {
        long timestamp = System.currentTimeMillis();
        int i16 = int16.incrementAndGet();
        if (i16 == 10 && timestamp == timestamp2) {
            i16 = 0;
            int16.set(0);
            try {
                Thread.sleep(1L);
                timestamp = System.currentTimeMillis();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        timestamp2 = timestamp;
        return nodeid + timestamp + i16;
    }
}
