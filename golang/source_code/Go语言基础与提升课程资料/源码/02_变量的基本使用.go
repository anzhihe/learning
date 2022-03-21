package main

import "fmt"

func main() {
	var a int //声明一个变量
	a = 100   //变量的赋值
	//a = 123.35  错误，a申请内存的时候，已经限定了是int类型，不能是小数类型
	fmt.Println(a)
	var b int = 300 //变量的初始化操作
	b = 200
	fmt.Println(b) //? 200
}
