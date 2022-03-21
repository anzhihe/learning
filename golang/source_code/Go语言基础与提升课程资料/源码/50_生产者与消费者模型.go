package main

import (
	"fmt"
	"time"
)

var flag1 = false

func main() {
	ch := make(chan int) //默认为双向channel
	go producer(ch)      //双向channel可以赋值给单向channel
	go consumer(ch)
	for {
		if flag1 {
			break
		}
	}
}

//生产者
func producer(ch chan<- int) { //参数为单向channel；只能写
	for i := 0; i < 10; i++ {
		fmt.Printf("生产第%v条数据\n", i+1)
		ch <- i * i
		time.Sleep(time.Second * 1)
	}
	close(ch)
}

//消费者
func consumer(ch <-chan int) { //参数为单向channel，只能读
	for num := range ch {
		fmt.Println("消费者读取到的内容为：", num)
	}
	flag1 = true
}
