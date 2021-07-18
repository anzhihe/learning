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
	_, err = conn.Do("Set", "name", "tomjerry猫猫")
	if err != nil {
		fmt.Println("set  err=", err)
		return 
	}

	//3. 通过go 向redis读取数据 string [key-val]

	r, err := redis.String(conn.Do("Get", "name"))
	if err != nil {
		fmt.Println("set  err=", err)
		return 
	}

	//因为返回 r是 interface{}
	//因为 name 对应的值是string ,因此我们需要转换
	//nameString := r.(string)

	fmt.Println("操作ok ", r)
}