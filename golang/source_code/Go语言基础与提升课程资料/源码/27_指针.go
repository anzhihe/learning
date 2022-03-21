package main

import "fmt"

type student struct {
	id    int
	name  string
	score float64
}

func main() {
	var a int = 100
	fmt.Println("变量a的地址为：", &a)
	p := &a
	fmt.Printf("变量p的类型为：%T,值为：%v,*P的值为：%v\n", p, p, *p)
	fmt.Println("==============指针变量的定义===================")
	p1 := new(string)
	*p1 = "name"
	fmt.Println(p1, *p1)
	fmt.Println("===============指针的使用==================")
	str := "Go 语言是一门很强大的编程语言！"
	p2 := new(string)
	p2 = &str
	fmt.Printf("变量str的值是：%v,*p2的值是：%v\n", str, *p2)
	fmt.Println("===============通过指针修改数据==================")
	*p2 = "Go 语言从入门到精通" //p2保存的是str的地址，所以可以通过*p2直接修改变量str中的内容
	fmt.Printf("*p2的值是：%v,str的值是：%v\n", *p2, str)
	fmt.Println("========================结构体指针===================")
	p3 := &student{}
	p3.name = "小明"
	p3.score = 98.9
	p3.id = 1
	fmt.Printf("指针变量p3的值为：%v,*p3的值为：%v\n", p3, *p3)
}
