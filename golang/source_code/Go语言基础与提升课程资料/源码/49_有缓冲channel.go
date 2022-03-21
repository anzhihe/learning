package main

import (
	"fmt"
	"time"
)

var ch chan int //定义了一个全局变量
var flag = false //标志位，作用是控制主程序退出

func main() {
	fmt.Println("=========有缓冲channel的基本使用==============")
	c := make(chan int, 3)
	fmt.Printf("创建的有缓冲channel长度为：%v；容量为：%v\n", len(c), cap(c))
	//在go程中向channel写入数据
	go func() {
		for i := 0; i < 10; i++ {
			c <- i
			fmt.Printf("通道c的长度为：%v；容量为：%v\n", len(c), cap(c))
		}
	}()

	//在主程序（主go程）中读取channel中的数据
	for i := 0; i < 10; i++ {
		time.Sleep(time.Second * 1)
		num := <-c
		fmt.Println("num=", num)
	}
	fmt.Println("===========有缓冲channel的关闭与遍历========================")
	ch = make(chan int, 3)
	go sendData()
	//go recvData1()
	go recvData2()
	for {
		if flag {
			break
		}
	}
}
func sendData() {
	for i := 0; i < 5; i++ {
		time.Sleep(time.Second * 1)
		ch <- i * i
	}
	close(ch)
}
func recvData1() {
	for {
		if data, ok := <-ch; ok {
			fmt.Println("接收到的数据为：", data)
		} else {
			fmt.Println("通道已经关闭！")
			break
		}
	}
	flag = true
}
func recvData2() {
	for data := range ch { // for-range 会一直阻塞读取channel中的数据，直到channel关闭才会退出
		fmt.Println("读取到的数据为：", data)
	}
	fmt.Println("子go程recvData2()执行结束！")
	flag = true
}
