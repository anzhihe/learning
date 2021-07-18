package main
import (
	"fmt"
	"net"
)

func informetion(conn net.Conn) {
	//关闭conn
	defer conn.Close()
	for {
		//创建一个新的切片
		newSlice := make([]byte, 1024)
		//等待客户端通过 conn 发送消息
		//如果客户端没有 write [发送], 那么协程就阻塞在这里
		fmt.Printf("\n服务器在等待客户端%v发送消息\n", conn.RemoteAddr().String())
		//从conn 读取
		n, err := conn.Read(newSlice)
		if err != nil {
			fmt.Println("conn.Read err = ", err)
			return
		}
		
		switch string(newSlice[:n]) {
			case "who are you":
				
				//显示客户端发送的内容到服务器的终端
				fmt.Print("我是小冰")
			case "你的性别?" :
				//显示客户端发送的内容到服务器的终端
				fmt.Print("你猜猜看")				
			case "你会什么" :
				//显示客户端发送的内容到服务器的终端
				fmt.Print("我会讲故事")
			case "你讲个笑话吧" :
				//显示客户端发送的内容到服务器的终端
				fmt.Print("从前有座山,山上有座庙,庙里有个老和尚和小和尚,老和尚对小和尚说:从前有座山,山上有座庙,....")
			default :
				//显示客户端发送的内容到服务器的终端
				fmt.Print("你说啥")
		}
		
	}

}

func main() {
	fmt.Println("服务器开始监听")
	//tcp 表示使用网络协议是 tcp
	// 127.0.0.1 表示在本地监听 6666端口
	listen, err := net.Listen("tcp","0.0.0.0:8888")
	if err != nil {
		fmt.Println("net.Listen err = ", err)
		return
	}
	//延时关闭 listen
	defer listen.Close()

	//循环等待客户端来连接客户端
	for {
		//等待客户端连接
		fmt.Println("等待客户端来连接")
		conn, err := listen.Accept()
		if err != nil {
			fmt.Println("listen.Accept err = ", err)
			return
		} else {
			fmt.Printf("Accept() suc con = %v 客户端 ip = %v\n", conn, conn.RemoteAddr().String())
		}
		//为客户端服务
		go informtion(conn)

	}
}