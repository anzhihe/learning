package main

import (
	"fmt"
	"time"
)

func main() {
	fmt.Println("===========goroutine与一般函数的使用==============")
	go running()
	for i := 0; i < 10; i++ {
		fmt.Println("执行主程序", i)
		time.Sleep(time.Second * 1)
	}
	fmt.Println("==================goroutine与匿名函数的结合=================")
	flag := false //定义一个标志位，来控制主程序的退出
	go func() {
		for i := 0; i < 10; i++ {
			fmt.Println("这里是匿名函数执行的并发", i)
			time.Sleep(time.Millisecond * 300)
		}
		flag = true
	}()

	for {
		if flag {
			break
		}
	}
}
func running() {
	for j := 0; j < 100; j++ { //如果主程序（主goroutine）退出，并发的goroutine也会退出。（并发程序是寄宿在主程序中的）
		fmt.Println("执行并发程序...", j)
		time.Sleep(time.Second * 1)
	}
}
