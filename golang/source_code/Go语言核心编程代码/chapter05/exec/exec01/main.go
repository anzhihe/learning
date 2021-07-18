package main
import (
	"fmt" 
)

func main() {
	//编写程序，声明2个int32型变量并赋值。判断两数之和，如果大于等于50，打印“hello world!”

	//分析
	//1. 变量 
	//2. 单分支

	var n1 int32 = 10
	var n2 int32 = 50
	if n1 + n2 >= 50 {
		fmt.Println("hello,world")
	}

	//编写程序，声明2个float64型变量并赋值。判断第一个数大于10.0，
	//且第2个数小于20.0，打印两数之和

	var n3 float64 = 11.0
	var n4 float64 = 17.0
	if n3 > 10.0 && n4 < 20.0 {
		fmt.Println("和=", (n3 + n4) )
	}

	//7)【选作】定义两个变量int32，判断二者的和，是否能被3又能被5整除，打印提示信息

	var num1 int32 = 10
	var num2 int32 = 5
	if (num1 + num2) % 3 == 0 &&  (num1 + num2) % 5 == 0 {
		fmt.Println("能被3又能被5整除")
	}

	//8)判断一个年份是否是闰年，闰年的条件是符合下面二者之一：
	//(1)年份能被4整除，但不能被100整除；(2)能被400整除
	var year int = 2019
	if (year % 4 == 0 && year % 100 !=0) || year % 400 == 0 {
		fmt.Println(year, "是润年~")
	}

	
}

