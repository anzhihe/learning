package main

import "fmt"

func main() {
	name := "小明"
	score := 98
	fmt.Printf("姓名：%s,分数：%d", name, score)
	//问题：如果不确定变量的类型怎么办？
	fmt.Printf("\n我的姓名是：%v,我的分数是：%v", name, score) //多学一招： %v可以代表任意类型
	//问题：我想按照自己的需要，将变量格式化之后赋值给另外一个变量，如何操作？
	str := fmt.Sprintf("姓名是：%v,分数：%v", name, score)
	fmt.Println("\nstr变量的内容是：" + str)
	//输入
	var name1 string
	fmt.Println("请输入姓名：")
	fmt.Scan(&name1)
	fmt.Println("您输入的姓名是：" + name1)
	var age int
	fmt.Scanf("%d", &age)
	fmt.Println("您输入的年龄是：", age)
}
