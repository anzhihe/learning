package main
import (
	"fmt"
	_ "math"
)

func main(){

	//参加百米运动会，如果用时8秒以内进入决赛，
	//否则提示淘汰。并且根据性别提示进入男子组或女子组。【可以让学员先练习下】, 
	//输入成绩和性别.

	//分析思路
	//1. 定义一个变量，来接收跑步使用秒数. float64
	//2. 定义一个变量，来接收性别string
	//3. 因为判断是嵌套的判断，因此我们会使用嵌套分支

	// var second float64 
	
	// fmt.Println("请输入秒数")
	// fmt.Scanln(&second)

	// if second <= 8 {
	// 	//进入决赛
	// 	var gender string
	// 	fmt.Println("请输入性别")
	// 	fmt.Scanln(&gender)
	// 	if gender == "男" {
	// 		fmt.Println("进入决赛的男子组")
	// 	} else {
	// 		fmt.Println("进入决赛的女子组")
	// 	}
	// } else {
	// 	fmt.Println("out...")
	// }


	/*
	出票系统：根据淡旺季的月份和年龄，打印票价 [考虑学生先做]

	4_10 旺季：
		成人（18-60）：60
		儿童（<18）:半价
		老人（>60）:1/3

	淡季：
		成人：40
		其他：20

	*/

	//分析思路
	//1.month age 的两个变量 byte
	//2.使用嵌套分支

	var month byte
	var age byte
	var price float64 = 60.0
	fmt.Println("请输入游玩月份")
	fmt.Scanln(&month)
	fmt.Println("请输入游客的年龄")
	fmt.Scanln(&age)	

	if month >= 4 && month <= 10 {
		if age > 60 {
			fmt.Printf("%v月 票价 %v 年龄 %v ", month, price / 3 ,  age)
		} else if age >= 18 {
			fmt.Printf("%v月 票价 %v 年龄 %v ", month, price,  age)
		} else {
			fmt.Printf("%v月 票价 %v 年龄 %v ", month, price / 2,  age)
		}
	} else {
		//淡季
		if age >= 18 && age < 60 {
			fmt.Println("淡季成人 票价 40")
		} else {
			fmt.Println("淡季儿童和老人  票价 20")
		}
	}
}