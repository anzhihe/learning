package main

import (
	"fmt"
)

type stu struct {
	id    int
	name  string
	score float64
}

func main() {
	fmt.Println("=================调用函数参数为基本数据类型===================")
	name := "小明"
	age := 23
	fmt.Println("调用函数之前的数据为：", name, age)
	test01(name, age)
	fmt.Println("调用函数之后的数据为：", name, age)
	fmt.Println("=================调用函数参数为数组类型===================")
	arr := [6]int{111, 222, 333, 444, 555, 666}
	fmt.Println("调用函数之前的数据为：", arr)
	test02(arr)
	fmt.Println("调用函数之后的数据为：", arr)
	fmt.Println("=================调用函数参数为切片类型===================")
	s := []int{111, 222, 333, 444, 555, 666}
	fmt.Println("调用函数之前的数据为：", s)
	test03(s)
	fmt.Println("调用函数之后的数据为：", s)
	fmt.Println("=================调用函数参数为结构体类型===================")
	student := stu{1, "小明", 98.9}
	fmt.Println("调用函数之前的数据为：", student)
	test04(student)
	fmt.Println("调用函数之后的数据为：", student)
	fmt.Println("=================调用函数参数为指针类型===================")
	p := &student
	fmt.Println("调用函数之前的数据为：", p, student)
	test05(p)
	fmt.Println("调用函数之后的数据为：", p, student)
}

//参数为基本数据类型
func test01(name string, age int) {
	name = "阿香"
	age = 20
}

//函数参数为数组类型
func test02(arr [6]int) {
	arr[0] = 888
}

//参数为切片类型
func test03(s []int) {
	s[0] = 888
}

//参数为结构体类型
func test04(s stu) {
	s.name = "阿香"
	s.id = 99

}

//参数为指针类型
func test05(s *stu) {
	s.id = 99
	s.name = "阿香"
}

//TODO 总结：
//函数参数为：基本数据类型、数组、结构体的为值传递（拷贝一份数据给封装的函数），不会改变原来的数据
//函数参数为：切片、指针的为引用传递（有的时候也说成是地址传递，将数据的地址给函数），由于传递的是地址，所以会修改原有的数据
