package main

import (
	"fmt"
	"math/rand"
	"runtime"
	"sync"
	"time"
)

var cond sync.Cond //定义条件变量
func main() {
	cond.L = new(sync.Mutex)         //初始化条件变量的锁
	buf := make(chan int, 3)         //生产者消费者模型中的缓冲区
	rand.Seed(time.Now().UnixNano()) //初始化随机数种子
	for i := 0; i < 3; i++ {
		go producer01(buf, i+1)
	}
	for i := 0; i < 3; i++ {
		go consumer01(buf, i+1)
	}
	//主程序
	for {
		time.Sleep(time.Second * 1)
		runtime.GC()
	}
}

//生产者
func producer01(ch chan<- int, n int) {
	for {
		cond.L.Lock()      //加锁
		for len(ch) == 3 { //判断缓冲区的数据是否满了
			cond.Wait()
		}
		num := rand.Intn(100)
		ch <- num
		fmt.Printf("=====第%v个生产者正在进行生产，生产的数据为：%v\n", n, num)
		cond.L.Unlock() //解锁
		cond.Signal()   //发送信息至消费者
		time.Sleep(time.Second * 2)
	}
}

//消费者
func consumer01(ch <-chan int, n int) {
	for {
		cond.L.Lock()
		for len(ch) == 0 { //判定缓冲区的数据是否为空
			cond.Wait()
		}
		num := <-ch
		fmt.Printf("第%v个消费者正在消费，消费的数据为：%v\n", n, num)
		cond.L.Unlock()
		cond.Signal()
		time.Sleep(time.Second * 1)
	}
}
