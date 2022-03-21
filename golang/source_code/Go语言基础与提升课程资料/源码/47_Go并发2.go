package main

import (
	"fmt"
	"runtime"
)

func main() {
	fmt.Println("计算器当前的CPU个数：", runtime.NumCPU()) //可以通过NumCPU()函数获取当前计算器的CPU个数
	runtime.GOMAXPROCS(8)
	go func() {
		for i := 0; i < 2; i++ {
			fmt.Println("hello")
		}
	}()
	go running02()
	go running03()
	for i := 0; i < 2; i++ {
		runtime.Gosched() //让出当前的CPU，使该CPU执行其他go程
		fmt.Println("word")
	}
}
func running02() {
	for i := 0; i < 10; i++ {
		fmt.Println("执行的Go程1", i)
		if i > 6 {
			return
		}
	}
}
func running03() {
	for i := 0; i < 10; i++ {
		fmt.Println("执行Go程2", i)
		if i > 3 {
			runtime.Goexit()
		}

	}
}
