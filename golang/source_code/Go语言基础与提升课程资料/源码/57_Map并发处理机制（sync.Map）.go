package main

import (
	"fmt"
	"sync"
)

var m map[int]int       //定义一个map
var wg sync.WaitGroup   //作用：解决go程之间的同步问题
var RWLock sync.RWMutex //读写锁
var m1 sync.Map         //线程安全的map
func main() {
	m = make(map[int]int) //初始化map
	/*wg.Add(10)            //添加go程数量
	//开启go程
	for i := 0; i < 10; i++ {
		go w1(i, i*i)
	}*/
	wg.Add(20) //设置go程数量
	for i := 0; i < 10; i++ {
		go w2(i, i)
		//go r3(i)
	}
	for i := 0; i < 10; i++ {
		go r2(i)
	}
	wg.Wait() //阻塞等待
	wg.Wait() //等待，一直处于阻塞。直到所有go程执行结束
}
func w1(key, value int) {
	m[key] = value
	wg.Done() //go程数量减1
}

//map在并发条件下，多go程是不安全的
func w2(key, value int) {
	RWLock.Lock()         //加锁（读写锁中的 写模式锁）
	defer RWLock.Unlock() //解锁
	m[key] = value
	wg.Done()
}
func r2(k int) {
	RWLock.RLock()         //加锁（读写锁中的 读模式锁）
	defer RWLock.RUnlock() //解锁
	v, ok := m[k]
	fmt.Println("map读取到的数据为：", v, ok)
	wg.Done()
}
func w3(k, v int) {
	m1.Store(k, v*v) //sync.map的写操作
	wg.Done()
}
func r3(k int) {
	v, ok := m1.Load(k) //sync.map的读操作；如果key对应的value不存在，返回为：nil，false
	fmt.Println("sync.Map读取到的数据为：", v, ok)
	wg.Done()
}
