package main

import "fmt"

type person struct {
	id   string
	name string
	age  int
}
type student2 struct {
	person
	score float64
	name  string
	person1
}
type person1 struct {
	addr string
}

func main() {
	stu := student2{person: person{id: "0x001x", name: "小明"}, score: 98.9}
	fmt.Printf("变量stu的类型为：%T,编号为：%v,姓名为：%v,age为：%v，分数为：%v\n", stu, stu.id, stu.name, stu.age, stu.score)
	fmt.Println("==============对象属性的操作===================")
	//在Go语言中，可以将结构体称作：类、对象、实体
	stu.score = 99
	stu.age = 23
	stu.age++
	fmt.Println(stu)
	fmt.Println("===============子对象与父对象重名的情况==================")
	stu.name = "张三"        //问题？ 修改的是子对象的name 还是父对象的name？
	fmt.Println(stu)       //修改的是子对象的属性name
	stu.person.name = "阿香" //如果属性存在重名情况，默认是子对象的属性值。如果要获取或者修改父对象的属性，需要指定到具体的父对象下面
	fmt.Println(stu)
	fmt.Println("===============对象的多个继承=============================")
	stu.addr = "北京"
	fmt.Println(stu) //Go语言可以有多个父类对象（继承）
}
