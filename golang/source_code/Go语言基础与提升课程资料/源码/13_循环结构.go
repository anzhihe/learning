package main

import "fmt"

func main() {
	//问题：我非常喜欢Go语言 （输出10次）
	for i := 0; i < 10; i++ {
		fmt.Println("我非常喜欢Go语言", i+1)
	}
	//问题；1——100的和？
	var sum int = 0
	for i := 1; i <= 100; i += 2 {
		//sum = sum + i
		sum += i
	}
	fmt.Println("1-100的和是：", sum)
}
