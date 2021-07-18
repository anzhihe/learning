package main
import (
	"fmt"
	"net"
	"time"
	"go_code/chatsys/server/model"
)



func initUserDao() {
	//说明pool 是一个全局变量，在redis.go中初始化的
	//因此这里可以直接使用
	model.MyUserDao = model.NewUserMgr(pool)
}


func proccess(conn net.Conn) {

	//defer conn.Close()
	//创建一个client,相当于一个控制器
	cp := &ClientProcessor{
		conn: conn,
	}
	//让client进行处理，其实主要是让client将不同的
	//请求，分配给不同的处理器文件去处理.
	err := cp.Process()
	if err != nil {
		fmt.Println("client process failed err= ", err)
		return
	}

}

func main() {
	
	//在服务器端链接到Redis
	initRedis("localhost:6379", 16, 1024, time.Second*300)
	//在服务器端初始化一个UserDao,用于操作Redis
	initUserDao()


	var addr = "0.0.0.0:8889"
	fmt.Println("服务器在8889端口上监听, 等待客户端来链接...")
	l, err := net.Listen("tcp", addr)
	if err != nil {
		fmt.Println("监听失败.. err= ", err)
		return
	}

	for {
		//等待链接..
		conn, err := l.Accept()
		if err != nil {
			fmt.Println("accept failed, err= ", err)
			continue
		}
		go proccess(conn)
	}
	
}