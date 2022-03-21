package main

import "fmt"

func main() {
	var flag bool //定义一个bool类型的变量flag
	// flag = "33"  bool类型的变量只能是 false / true 两种状态的值
	fmt.Println(flag)
	var score1 float32 = 98.8
	var score2 float64 = 89.9
	sum := score1 + float32(score2)
	//f1 := 12    f1：类型是int
	//  f2 := 12.0  f2:类型float
	fmt.Println(score1, score2, sum)
	var number byte = 'a'
	fmt.Println(number) //输出的结果是 97，即a的ASCII码
	fmt.Println('b')
	var name string = "张三"
	fmt.Println(name)
	str := "a"  //string
	str1 := 'a' //byte
	fmt.Println(str)
	fmt.Println(str1)
}
