package main

import "fmt"

//定义结构体
type Student struct {
	id      int
	name    string
	sex     byte //1:表示男生；0：表示女生
	address string
}

func main() {
	//初始化结构体
	var s1 Student = Student{1, "阿香", 0, "北京"}
	fmt.Printf("s1的类型：%T,数据为：%v\n", s1, s1)
	s2 := Student{name: "小明", sex: 1}
	fmt.Println(s2)
	fmt.Println("===========结构体成员的使用==========")
	fmt.Printf("s1结构体成员的具体内容为：编号：%v,姓名：%v,性别：%v,地址：%v\n", s1.id, s1.name, s1.sex, s1.address)
	fmt.Println("===========结构体的比较============")
	flag := s1 == s2
	fmt.Println(flag)
	flag1 := s1 != s2
	fmt.Println(flag1)
	fmt.Println("===========结构体数组/切片============")
	students := make([]Student, 0)
	students = append(students, s1, s2)
	fmt.Println(students)
	for _, value := range students {
		fmt.Printf("编号：%v,姓名：%v\n", value.id, value.name)
	}
}
