package main
import (
	"fmt"
	"go_code/chapter06/fundemo01/utils"
)


func main() {

	fmt.Println("utils.go Num~=", utils.Num1)
	//请大家完成这样一个需求:
	//输入两个数,再输入一个运算符(+,-,*,/)，得到结果.。
	//分析思路....
	var n1 float64 = 1.2
	var n2 float64 = 2.3
	var operator byte = '+'
	result := utils.Cal(n1, n2 , operator) 
	fmt.Println("result~=", result)


	//代码...
	//代码...
	//代码...

	//有需求，输入两个数num1, num2，计算 + / *  - 的值

	n1 = 4.5
	n2 = 6.7
	operator = '*'
	result = utils.Cal(n1, n2 , operator)
	fmt.Printf("result~=%.2f", result)
	// //..需求


}