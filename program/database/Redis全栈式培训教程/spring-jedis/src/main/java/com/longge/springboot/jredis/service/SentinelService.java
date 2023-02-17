package com.longge.springboot.jredis.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisSentinelPool;

@Service
public class SentinelService {
    @Autowired
    private JedisSentinelPool sentinelPool;

    public Jedis getJedis() {
        return sentinelPool.getResource();
    }

    public void closeJedis(Jedis jedis) {
        if (null != jedis) {
            jedis.close();
        }
    }

    public void set(String key, String value) {
        Jedis jedis = null;
        try {
            jedis = sentinelPool.getResource();
            jedis.set(key, value);
        } finally {
            if (null != jedis) {
                jedis.close();
            }
        }
    }

    public String get(String key) {
        Jedis jedis = null;
        try {
            jedis = sentinelPool.getResource();
            return jedis.get(key);
        } finally {
            if (null != jedis) {
                jedis.close();
            }
        }
    }
}