package main

import "fmt"

var res int //全局变量
func main() {
	a := 100          //变量a是局部变量
	b := 200          //变量b是局部变量
	res1 := Add(a, b) //res1：局部变量
	res = Sub(a, b)
	fmt.Print(res1, res)
	fmt.Println()
	fmt.Println(sum(100))
	//函数的嵌套调用
	fmt.Println("开始调用A函数")
	A()
	fmt.Println("A函数执行结束")
}

//求和函数
func Add(a1 int, a2 int) int { //a1,a2为Add函数的参数，只在Add函数范围内有效
	//res+=100 全局变量可以在本文件对应的所有函数中使用
	return a1 + a2
}
func Sub(a1, a2 int) int { //a1,a2为Sub函数的形参，只在Sub函数范围内有效
	return a1 - a2
}

//函数功能：实现1-n之间所有数字和的运算
func sum(n int) int {
	var res int //如果局部变量的名称与全局变量名称相同，在本局部变量范围内（作用域）,以局部变量为准
	for i := 1; i <= n; i++ {
		res += i
	}
	return res
}
func A() {
	fmt.Println("A函数正在执行。。。")
	fmt.Println("开始调用B函数")
	B()
	fmt.Println("B函数调用结束")
}
func B() {
	fmt.Println("B函数正在执行。。。")

}
