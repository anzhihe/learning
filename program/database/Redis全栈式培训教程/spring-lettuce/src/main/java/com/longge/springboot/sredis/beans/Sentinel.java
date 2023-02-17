package com.longge.springboot.sredis.beans;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.stereotype.Component;

import io.lettuce.core.RedisClient;
import io.lettuce.core.RedisURI;
import io.lettuce.core.api.StatefulRedisConnection;

/**
 * Spring集成lettuce的配置(sentinel)
 */
@Component
public class Sentinel {
    @Value("${lettuce.sentinel.host1}")
    private String host1;
    @Value("${lettuce.sentinel.port1}")
    private int port1;
    @Value("${lettuce.sentinel.host2}")
    private String host2;
    @Value("${lettuce.sentinel.port2}")
    private int port2;
    @Value("${lettuce.sentinel.host3}")
    private String host3;
    @Value("${lettuce.sentinel.port3}")
    private int port3;

    @Bean("sentinelConnection")
    public StatefulRedisConnection<String, String> getSentinelConnection() {
        RedisURI redisUri = RedisURI.Builder.sentinel(host1, port1, "mymaster").withSentinel(host2, port2)
                .withSentinel(host3, port3).build();
        RedisClient redisClient = RedisClient.create(redisUri);
        StatefulRedisConnection<String, String> connection = redisClient.connect();
        return connection;
    }
}
