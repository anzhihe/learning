package main

import "fmt"

type A1 struct {
	Num int
}

//定义对象（结构体）A1的方法；注意：方法是针对某一对象的函数，只有改类型的对象才能调用
func (a A1) test() {
	fmt.Println("这里是结构体/对象A1的方法 test()")
	fmt.Println(a.Num)
}
func test() { //函数
	fmt.Println("这里是函数")

}

type Person1 struct {
	name string
	sex  byte
	age  int
}

func (s *Person1) PrintInfo() {
	fmt.Printf("name：%v;sex:%v;age:%v\n", s.name, s.sex, s.age)
}
func main() {
	test() //函数的调用
	a := A1{Num: 100}
	a.test() //方法的调用
	p := Person1{"小明", 1, 23}
	p.PrintInfo() //接受者为结构体指针类型方法的调用
}
