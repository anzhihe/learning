package com.longge.springboot.sredis.beans;

import java.time.Duration;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.stereotype.Component;

import io.lettuce.core.RedisClient;
import io.lettuce.core.RedisURI;
import io.lettuce.core.api.StatefulRedisConnection;

/**
 * Spring集成lettuce的配置(单点)
 */
@Component
public class Simple {
    @Value("${lettuce.simple.host}")
    private String host;
    @Value("${lettuce.simple.port}")
    private int port;
    @Value("${lettuce.simple.timeout}")
    private int timeOut;

    @Bean("simpleConnection")
    StatefulRedisConnection<String, String> getSimpleConnection() {
        RedisURI redisURI = new RedisURI();
        redisURI.setHost(this.host);
        redisURI.setPort(this.port);
        redisURI.setTimeout(Duration.ofMillis(timeOut));
        RedisClient redisClient = RedisClient.create(redisURI);
        return redisClient.connect();
    }
}
