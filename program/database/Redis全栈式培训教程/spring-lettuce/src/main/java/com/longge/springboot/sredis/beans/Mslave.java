package com.longge.springboot.sredis.beans;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.stereotype.Component;

import io.lettuce.core.ReadFrom;
import io.lettuce.core.RedisClient;
import io.lettuce.core.RedisURI;
import io.lettuce.core.api.StatefulRedisConnection;
import io.lettuce.core.codec.StringCodec;
import io.lettuce.core.masterreplica.MasterReplica;
import io.lettuce.core.masterreplica.StatefulRedisMasterReplicaConnection;

/**
 * Spring集成lettuce的配置(标准主从)
 */
@Component
public class Mslave {
    @Value("${lettuce.mslave.host1}")
    private String url1;
    @Value("${lettuce.mslave.host2}")
    private String url2;
    @Value("${lettuce.mslave.host3}")
    private String url3;

    @Bean("mslaveConnection")
    public StatefulRedisConnection<String, String> getSentinelConnection() {
        RedisClient redisClient = RedisClient.create();
        List<RedisURI> list = new ArrayList<RedisURI>();
        list.add(RedisURI.create(this.url1));
        list.add(RedisURI.create(this.url2));
        list.add(RedisURI.create(this.url3));
        StatefulRedisMasterReplicaConnection<String, String> connection = MasterReplica.connect(redisClient,
                StringCodec.UTF8,
                list);
        connection.setReadFrom(ReadFrom.MASTER_PREFERRED);
        return connection;
    }
}
