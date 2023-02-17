package com.longge.springboot.sredis.rest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RequestMapping(value = "/test")
@RestController
public class TestController {
    @Autowired
    private RedisTemplate<String, Object> redisTemplate;

    @RequestMapping(value = "/set/{key}/{value}")
    public String set(@PathVariable String key, @PathVariable String value) {
        this.redisTemplate.opsForValue().set(key, value);
        return this.redisTemplate.opsForValue().get(key).toString();
    }
}
