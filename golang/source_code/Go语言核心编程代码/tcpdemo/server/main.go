package main

import (
	"fmt"
	"net"
)

func main() {
	fmt.Println("start server... 在8888端口上监听..")
	//监听8888,等待客户端连接
	listen, err := net.Listen("tcp", "0.0.0.0:8888")
	if err != nil {
		fmt.Println("listen failed, err:", err)
		return
	}
	for {
		//如果客户端发出链接请求,服务器端就会与客户端创建conn
		//通过conn ，客户端和服务器端就可以通讯(即收发数据)
		//如果没有客户端端来链接服务器端，则阻塞在这里...
		conn, err := listen.Accept()
		fmt.Println("和某客户端创建了一个链接")
		if err != nil {
			fmt.Println("accept failed, err:", err)
			continue
		}
		//当和某个客户端创建了一个conn,就创建一个goroutine去处理
		//该客户端和服务器端的通讯
		go process(conn)
	}
}
func process(conn net.Conn) {
	defer conn.Close()
	for {
		buf := make([]byte, 512)
		n, err := conn.Read(buf)
		if err != nil {
			fmt.Println("read err:", err)
			return
		}
		//将从客户端读到的数据输出到终端
		fmt.Printf(string(buf[0:n]))
	}
}