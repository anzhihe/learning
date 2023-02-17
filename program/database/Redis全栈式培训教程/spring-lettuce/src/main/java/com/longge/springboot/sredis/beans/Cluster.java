package com.longge.springboot.sredis.beans;

import java.util.Arrays;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.stereotype.Component;

import io.lettuce.core.RedisURI;
import io.lettuce.core.cluster.RedisClusterClient;
import io.lettuce.core.cluster.api.StatefulRedisClusterConnection;

/**
 * Spring集成lettuce的配置(cluster模式)
 */
@Component
public class Cluster {
    @Value("${lettuce.cluster.host1}")
    private String host1;
    @Value("${lettuce.cluster.host3}")
    private String host2;
    @Value("${lettuce.cluster.host3}")
    private String host3;

    @Bean("clusterConnection")
    public StatefulRedisClusterConnection<String, String> getClusterConnection() {
        RedisURI node1 = RedisURI.create("redis://" + host1);
        RedisURI node2 = RedisURI.create("redis://" + host2);
        RedisURI node3 = RedisURI.create("redis://" + host3);
        RedisClusterClient clusterClient = RedisClusterClient.create(Arrays.asList(node1, node2, node3));
        StatefulRedisClusterConnection<String, String> connection = clusterClient.connect();
        return connection;
    }
}
