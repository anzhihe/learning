package main

import (
	"fmt"
	"math"
)

func main() {
	//============算术运算符==============
	num1 := 100
	num2 := 200
	fmt.Printf("num1+num2=%v", num1+num2)
	age := 23
	age++ //24  自加1，等价于：age=age+1
	fmt.Println("\nage:", age)
	area := math.Pi * 10 * 10
	fmt.Println("半径为10的圆面积是：", area)
	//=================赋值运算符=============
	var num = 10
	fmt.Println(num)
	num *= 3 // 问题：num的值是什么？ num=num*3
	fmt.Println("num的值是：", num)
	//============关系运算符===================
	flag1 := 100 > 200
	flag2 := num == 30
	fmt.Printf("flag1的数据类型是：%T；flag2的数据类型是：%T\n", flag1, flag2)
	fmt.Println(flag1)
	fmt.Println(flag2)
	//===========逻辑运算符====================
	temp1 := 5 > 3 || 2 > 3 // 在||左右有一个为true，结果为true
	fmt.Println(temp1)      //问题：temp1值是什么？
	var m, n = 10, 20
	temp2 := m >= 10 && n >= 20
	fmt.Println(temp2) //问题：temp2值是什么？ && 左右都为true，结果才为true，否则为false
}
