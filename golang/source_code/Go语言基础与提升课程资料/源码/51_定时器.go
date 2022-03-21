package main

import (
	"fmt"
	"runtime"
	"time"
)

var flag2 = false

func main() {
	fmt.Println("===========定时器的基本使用=================")
	timer1 := time.NewTimer(time.Second * 5)
	t1 := time.Now().Second()
	fmt.Println("当前时间是：", t1)
	timer1.Reset(time.Second * 1)
	t2 := <-timer1.C
	defer timer1.Stop()
	fmt.Println("时间到！", t2.Second())
	fmt.Println("============3种延时操作==============")
	delay01()
	delay02()
	delay03()
	fmt.Println("===============ticker的使用============")
	ticker1 := time.NewTicker(time.Second * 1) //完成周期性的延时操作
	i := 0
	go func() {
		for {
			<-ticker1.C
			i++
			fmt.Printf("执行第%v次\n", i)
			if i >= 5 {
				ticker1.Stop()
				flag2 = true
				//break
				//return
				runtime.Goexit()
			}
		}
	}()
	for {
		if flag2 {
			break
		}
	}
}
func delay01() {
	fmt.Println("开始执行延时函数1")
	t := time.NewTimer(time.Second * 3)
	<-t.C
	fmt.Println("延时函数1执行结束")
}
func delay02() {
	fmt.Println("开始执行延时函数2")
	<-time.After(time.Second * 3)
	fmt.Println("延时函数2执行结束")
}
func delay03() {
	fmt.Println("开始执行延时函数3")
	time.Sleep(time.Second * 3)
	fmt.Println("延时函数3执行结束")
}
