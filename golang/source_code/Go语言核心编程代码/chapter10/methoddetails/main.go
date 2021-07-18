package main

import (
	"fmt"	
)
/*
Golang中的方法作用在指定的数据类型上的(即：和指定的数据类型绑定)，因此自定义类型，
都可以有方法，而不仅仅是struct， 比如int , float32等都可以有方法
*/

type integer int

func (i integer) print() {
	fmt.Println("i=", i)
}
//编写一个方法，可以改变i的值
func (i *integer) change() {
	*i = *i + 1
}

type Student struct {
	Name string
	Age int
}

//给*Student实现方法String()
func (stu *Student) String() string {
	str := fmt.Sprintf("Name=[%v] Age=[%v]", stu.Name, stu.Age)
	return str
}

func main() {
	var i integer = 10
	i.print()
	i.change()
	fmt.Println("i=", i)

	//定义一个Student变量
	stu := Student{
		Name : "tom",
		Age : 20,
	}
	//如果你实现了 *Student 类型的 String方法，就会自动调用
	fmt.Println(&stu) 
} 