package main
import (
	"fmt"
	"github.com/garyburd/redigo/redis" //引入redis包
)

func main() {
	//通过go 向redis 写入数据和读取数据
	//1. 链接到redis
	conn, err := redis.Dial("tcp", "127.0.0.1:6379")
	if err != nil {
		fmt.Println("redis.Dial err=", err)
		return 
	}
	defer conn.Close() //关闭..

	//2. 通过go 向redis写入数据 string [key-val]
	_, err = conn.Do("HMSet", "user02", "name", "john", "age", 19)
	if err != nil {
		fmt.Println("HMSet  err=", err)
		return 
	}



	//3. 通过go 向redis读取数据 

	r, err := redis.Strings(conn.Do("HMGet","user02", "name", "age"))
	if err != nil {
		fmt.Println("hget  err=", err)
		return 
	}
	for i, v := range r {
		fmt.Printf("r[%d]=%s\n", i, v)
	}

}