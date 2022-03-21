package main

import "fmt"

func main() {
	a1 := 123
	//1a:=456 错误的命名，不能以数字开头
	_a123 := 33.33
	_123 := 456 //变量命名可以是字母或者 _,但是不能是数字
	// var:=345 不能使用Go语言的关键字作为变量名
	fmt.Println(a1, _a123, _123)
	name := "张三"
	fmt.Println(name)
	age := 23
	fmt.Println(age)
	//用户名
	//username:="张三"
	userName := "张三" //小驼峰命名
	fmt.Println(userName)
	FirstName := "Jim"
	fmt.Println(FirstName) //大驼峰命名
}
