package com.longge.springboot.sredis;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.data.redis.RedisProperties;
import org.springframework.cache.annotation.EnableCaching;

@EnableCaching
@SpringBootApplication
public class Application {

	public static void main(String[] args) {
		// redis配置参考RedisProperties
		RedisProperties tt;
		SpringApplication.run(Application.class, args);
	}
}
