package main

import "fmt"

func main() {
	f := func() {
		fmt.Println("这里是匿名函数")
	}
	fmt.Printf("变量f的类型是：%T；对应的值是：%v\n", f, f)
	f() //匿名函数的调用
	//匿名函数的直接调用
	fmt.Println("========匿名函数的直接调用===========")
	func(a, b int) {
		fmt.Println("匿名函数接收到的参数值是：", a, b)
	}(100, 200)
	fmt.Println("========具有返回值的匿名函数===========")
	f1 := func(a, b int) int {
		return a + b
	}
	i := f1(100, 200)
	fmt.Println(i)

}
