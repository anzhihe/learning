package com.longge.springboot.sredis.service;

import java.util.concurrent.TimeUnit;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Service;

@Service
public class RepeatService {
    @Autowired
    private RedisTemplate<String, String> redisTemplate;

    /**
     * 防重复提交
     * 
     * @param key
     * @return
     */
    public boolean submit(String key) {
        boolean flag = this.redisTemplate.opsForValue().setIfAbsent(key, "1", 10, TimeUnit.SECONDS);
        if (!flag) {
            return false;
        }
        // 下面处理正常业务……
        System.out.println("开始处理提交业务……");
        return true;
    }
}
