package main

import (
	"fmt"
	"sync"
	"time"
)

var count = 0 //读写锁操作的数据资源
var rwLock sync.RWMutex

func main() {
	for i := 0; i < 5; i++ { //开启5个go程执行读操作
		go read(i + 1)
	}
	for i := 0; i < 5; i++ { //开启5个go程执行写操作
		go write(i+1, i*i)
	}
	select {
	case <-time.After(time.Second * 30):
		fmt.Println("主程序（go程）退出")
	}
}

//读操作（读取数据资源）
func read(n int) {
	//加锁 ：读写锁下面的读模式锁
	rwLock.RLock()         //加锁
	defer rwLock.RUnlock() //解锁
	data := count
	fmt.Printf("-----读操作正在执行第%v个go程的操作，读取到的数据为：%v\n", n, data)
	time.Sleep(time.Second * 3)
}

//写操作（修改数据资源）
func write(n, data int) {
	//加锁、解锁为写模式下的
	rwLock.Lock()
	defer rwLock.Unlock()
	count = data
	fmt.Printf("写操作正在执行第%v个go程的操作，写入的数据为：%v\n", n, data)
	time.Sleep(time.Second * 3)
}

//读写锁可以并发的读，但是同时只能有一个go程写；并且读、写不能同时进行
