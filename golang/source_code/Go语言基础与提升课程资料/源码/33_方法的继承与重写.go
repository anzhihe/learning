package main

import "fmt"

type PersonA struct {
	name string
	sex  byte
	age  int
}

func (p *PersonA) PrintInfo() {
	fmt.Printf("name:%v;sex:%v;age:%v\n", p.name, p.sex, p.age)
}

type StudentA struct {
	PersonA
	id   int
	addr string
}

func (s *StudentA) PrintInfo() {
	fmt.Println("这里是对象StudentA重写的方法")
	fmt.Printf("name:%v,age:%v\n", s.name, s.age)
}

func main() {
	fmt.Println("==================方法的继承======================")
	s := StudentA{PersonA{"张三", 1, 23}, 20230001, "北京"}
	s.PrintInfo()
	fmt.Println("================方法的重写========================")
	s.PrintInfo() //直接调用，是重写之后的方法
	//问题？如何调用父类的方法？
	s.PersonA.PrintInfo() //需要指定到具体的父类，通过父类实现方法的调用
}
