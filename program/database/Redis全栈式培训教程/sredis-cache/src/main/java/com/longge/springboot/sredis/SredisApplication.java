package com.longge.springboot.sredis;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cache.annotation.EnableCaching;

@EnableCaching
@SpringBootApplication
public class SredisApplication {

	public static void main(String[] args) {
		/*
		 * RedisProperties tt6;
		 * RedisStandaloneConfiguration tt1;
		 * RedisSentinelConfiguration tt;
		 * RedisClusterConfiguration tt2;
		 * LettuceConnectionFactory tt3;
		 * RedisStaticMasterReplicaConfiguration tt4;
		 * RedisCacheConfiguration ttttt;
		 * CacheManager ttt13;
		 */
		SpringApplication.run(SredisApplication.class, args);
	}
}
