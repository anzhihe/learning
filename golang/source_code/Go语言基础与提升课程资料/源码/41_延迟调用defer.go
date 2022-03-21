package main

import "fmt"

func main() {
	fmt.Println("===============defer的基本使用====================")
	defer fmt.Println("Hello Go")
	fmt.Println("开始执行命令！")
	//问题？ 如果有多个defer，执行顺序是怎样的？
	defer fmt.Println("执行命令1")
	defer fmt.Println("执行命令2")
	fmt.Println("==============defer与匿名函数结合使用===============")
	deferTest1()
	deferTest2()
}
func deferTest1() {
	fmt.Println("开始执行deferTest1")
	a := 10
	b := 20
	defer func() {
		fmt.Printf("匿名函数中a的值为：%v,b的值为：%v\n", a, b) //没有携带任何参数，执行的是全局变量a,b的最终值
	}()
	a = 100
	b = 200
	fmt.Println("函数中a，b的值为；", a, b)
}
func deferTest2() {
	fmt.Println("开始执行deferTest2")
	a := 10
	b := 20
	defer func(a, b int) {
		fmt.Printf("匿名2函数中a的值为：%v,b的值为：%v\n", a, b) //注意：执行的是压入栈中的数据（a=10；b=20）
	}(a, b)
	a = 100
	b = 200
	fmt.Println("函数2中a,b的值分别为：", a, b)
}
