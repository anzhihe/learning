package com.longge.springboot.jredis.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import redis.clients.jedis.JedisCluster;

@Service
public class ClusterService {
    @Autowired
    private JedisCluster jedisCluster;

    public void set(String key, String value) {
        this.jedisCluster.set(key, value);
    }

    public String get(String key) {
        return this.jedisCluster.get(key);
    }
}
