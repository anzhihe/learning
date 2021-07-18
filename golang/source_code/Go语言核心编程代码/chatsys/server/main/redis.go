package main

import "github.com/garyburd/redigo/redis"
import "time"

var pool *redis.Pool

func initRedis(addr string, idleConn, maxConn int, idleTimeout time.Duration) {

	pool = &redis.Pool{
		MaxIdle:     idleConn,
		MaxActive:   maxConn,
		IdleTimeout: idleTimeout,
		Dial: func() (redis.Conn, error) {
			return redis.Dial("tcp", addr)
		},
	}
	return
}

//从Redis的链接池中，得到一个链接
func GetConn() redis.Conn {
	return pool.Get()
}

//关闭一个从Redis的链接池中获取到的链接
func PutConn(conn redis.Conn) {
	conn.Close()
}
