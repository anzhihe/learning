package main

import "fmt" //fmt包中提供格式化，输出，输入的函数.

//这是一个main函数，是程序入口
func main() {
	//演示转义字符的使用 \t
	fmt.Println("tom\tjack")

	// 如果希望一次性注释 ctrl + / 第一次表示注释，第二次表示取消注释
	fmt.Println("hello\nworld")
	fmt.Println("C:\\Users\\Administrator\\Desktop\\Go语言核心编程课程\\资料")
	fmt.Println("tom说\"i love you\"")

	// \r 回车,从当前行的最前面开始输出，覆盖掉以前内容
	fmt.Println("天龙八部雪山飞狐\r张飞厉害")

	fmt.Println("helloworldhelloworldhelloworldhelloworl\n", 
		"dhelloworldhelloworldhelloworldhelloworldhelloworldhellowor\n", 
		"ldhelloworldhelloworldhelloworldhelloworldhelloworldhelloworl\n", 
		"dhelloworldhelloworldhelloworldhelloworldhelloworldhelloworldhel\n", 
		"loworldhelloworldhelloworldhelloworldhelloworldhelloworldhellowor\n", 
		"ldhelloworldhelloworldhelloworldhelloworldhelloworldhelloworld")

	//var num = 2 + 4 * 5 
}
