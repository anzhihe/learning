package main

import "fmt"

func main() {
	//===============基本使用===================
	fmt.Println("请您输入位置方向：")
	var position string
	fmt.Scanf("%s", &position)
	//fmt.Println(position)
	switch position {
	case "L":
		fmt.Println("左转")
		// 在Go语言中 break 可以省略
	case "R":
		fmt.Println("右转")
	case "F":
		fmt.Println("直走")
	case "B":
		fmt.Println("后传")
	default:
		fmt.Println("其他")

	}
	//=================条件判断==============
	var score int
	fmt.Println("请输入您的成绩：")
	fmt.Scanf("%d", &score)
	// 90以上： 优秀   80-90:良好   70-80：中等  70以下：其他
	switch {
	case score >= 90 && score <= 100:
		fmt.Println("您的成绩是优秀！")
	case score >= 80 && score < 90:
		fmt.Println("您的成绩是良好！")
		fallthrough
	case score >= 70 && score < 80:
		fmt.Println("您的成绩是中等！")
	default:
		fmt.Println("其他")

	}
}
