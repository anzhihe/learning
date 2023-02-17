package com.longge.springboot.sredis.service;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Service;

@Service
public class FriendService {
    @Autowired
    private RedisTemplate<String, String> redisTemplate;

    /**
     * 模拟求共同好友
     * 
     * @return
     */
    public Set<String> inter() {
        // 用户A信息
        List<String> alist = new ArrayList<String>();
        for (int i = 0; i < 10; i++) {
            alist.add("id_" + i);
        }

        // 用户B信息
        List<String> blist = new ArrayList<String>();
        for (int i = 6; i < 18; i++) {
            blist.add("id_" + i);
        }
        String[] array = new String[alist.size()];
        array = alist.toArray(array);
        this.redisTemplate.opsForSet().add("user_a", array);
        String[] barray = new String[blist.size()];
        barray = blist.toArray(barray);
        this.redisTemplate.opsForSet().add("user_b", barray);
        // 求共同好友
        Set<String> sets = this.redisTemplate.opsForSet().intersect("user_a", "user_b");
        return sets;
    }
}
