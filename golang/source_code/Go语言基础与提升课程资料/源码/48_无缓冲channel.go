package main

import (
	"fmt"
	"time"
)

func main() {
	c := make(chan int) //定义了一个无缓冲的channel;另外一种写法：make(chan int, 0)
	fmt.Printf("变量c的类型为：%T；长度为：%v；容量为：%v\n", c, len(c), cap(c))
	fmt.Println("===========channel的基本使用====================")
	go func() {
		defer fmt.Println("子go程退出！")
		for i := 0; i < 20; i++ {
			c <- i //向变量channel c中写入数据
			fmt.Printf("变量c的长度为：%v；容量为：%v\n", len(c), cap(c))
			time.Sleep(time.Millisecond * 300)
		}
	}()
	for i := 0; i < 10; i++ {
		num := <-c //从变量channel中读取数据
		fmt.Println("num=", num)
		time.Sleep(time.Millisecond * 300)
	}
}

//总结：channel是一种数据类型（其实channel就是通道），主要解决的是go程之间的数据同步与数据共享
//同时，要特别注意死锁问题！
