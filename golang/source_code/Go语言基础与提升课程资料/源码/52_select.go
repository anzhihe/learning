package main

import (
	"fmt"
	"time"
)

func main() {
	fmt.Println("==============select的基本使用=============")
	c1 := make(chan string)
	c2 := make(chan string)
	go func() {
		time.Sleep(time.Second * 3)
		c1 <- "one"
	}()
	go func() {
		time.Sleep(time.Second * 2)
		c2 <- "two"
	}()
	for i := 0; i < 2; i++ {
		select { //任意一个case满足条件，select就退出！
		case msg1 := <-c1:
			fmt.Println("接收到的数据为：", msg1)
		case msg2 := <-c2:
			fmt.Println("接收到的数据为：", msg2)
		}
		fmt.Println("******************")
	}
	fmt.Println("===============超时操作==================")
	TimeOutOperation()

}
func TimeOutOperation() {
	c := make(chan int)
	out := make(chan bool)
	go func() {
		for {
			select {
			case v := <-c:
				fmt.Println(v)
			case <-time.After(time.Second * 5):
				fmt.Println("超时！")
				out <- true
				return
			}
		}
	}()
	<-out
}
