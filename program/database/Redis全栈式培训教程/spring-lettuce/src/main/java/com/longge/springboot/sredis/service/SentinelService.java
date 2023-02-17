package com.longge.springboot.sredis.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Service;

import io.lettuce.core.api.StatefulRedisConnection;

@Service
public class SentinelService {
    @Autowired
    @Qualifier("sentinelConnection")
    private StatefulRedisConnection<String, String> connection;

    public void set(String key, String value) {
        connection.sync().set(key, value);
    }

    public String get(String key) {
        return connection.sync().get(key);
    }
}
