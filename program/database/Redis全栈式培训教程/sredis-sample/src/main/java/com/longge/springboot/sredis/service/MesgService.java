package com.longge.springboot.sredis.service;

import java.util.Random;
import java.util.concurrent.TimeUnit;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Service;

/**
 * 短信验证码服务
 */
@Service
public class MesgService {
    @Autowired
    private RedisTemplate<String, String> redisTemplate;

    /**
     * 模拟生成短信验证码
     * 
     * @param key
     * @return
     */
    public String sendMsg(String key) {
        Random rd = new Random();
        rd.nextInt(10);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 6; i++) {
            int ran = rd.nextInt(10);
            sb.append(ran);
        }
        // 把随机码放入redis(具有时效性)
        this.redisTemplate.opsForValue().set(key, sb.toString(), 300, TimeUnit.SECONDS);
        return sb.toString();
    }

    /**
     * 短信校验
     * 
     * @param key
     * @param value
     * @return
     */
    public boolean checkMsg(String key, String value) {
        String cvalue = this.redisTemplate.opsForValue().getAndDelete(key);
        if (null != value && value.equals(cvalue)) {
            return true;
        }
        return false;
    }
}
