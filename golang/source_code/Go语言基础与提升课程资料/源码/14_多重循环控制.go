package main

import "fmt"

func main() {
	for i := 1; i < 10; i++ { //i:代表的是行
		for j := 1; j <= i; j++ { //j:代表的是列
			fmt.Printf("%d*%d=%d\t", j, i, i*j)
		}
		fmt.Println()
	}
}

//TODO 多重循环控制的核心是：找到控制内容的规律（比如九九乘法表显示的规律）
