package main

import "fmt"

func main() {
	fmt.Println("请输入您的年龄：")
	var age int
	fmt.Scanf("%d", &age)
	if age >= 18 {
		fmt.Println("您已经是成年")
		if age >= 60 {
			fmt.Println("您已经是老年了！")
		} else {
			fmt.Println("您处于壮年！")
		}
	} else {
		//0（初生）-6岁为婴幼儿；7-12岁为少儿；13-17岁为青少年
		fmt.Println("未成年")
		if age <= 6 && age >= 0 {
			fmt.Println("您处于婴幼儿阶段！")
		} else if age >= 7 && age <= 12 {
			fmt.Println("您处于少儿阶段！")
		} else if age >= 13 && age <= 17 {
			fmt.Println("您处于青少年阶段！")
		} else {
			fmt.Println("您输入的年龄是错误的！")
		}

	}
	//todo 特别注意：在Go语言中，else（或者else if）一定要紧跟在}的后面
	//fmt.Println(age) //测试
}
