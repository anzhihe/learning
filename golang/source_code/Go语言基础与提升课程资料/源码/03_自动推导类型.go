package main

import "fmt"

func main() {
	//var a int = 100 //初始化一个变量
	a := 100
	//a = 123.3  错误，因为在执行 a:=100的时候，已经设定了a的类型是 int
	// b=200,c=300,d=400
	/*b := 200
	c := 300
	d := 400*/
	b, _, d := 200, 300, 400 //多个变量的赋值,300通过匿名变量 _接收，之后丢弃
	fmt.Println(a)
	fmt.Println(b, d) // b=200 d=400
	/*var temp int
	temp = b
	b = d
	d = temp*/
	b, d = d, b //Go 语言数据快速交换的方法
	fmt.Println(b, d)

}
