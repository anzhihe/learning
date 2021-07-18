package main
import (
	"fmt"
)

/*
请使用递归的方式，求出斐波那契数1,1,2,3,5,8,13...
给你一个整数n，求出它的斐波那契数是多少？
*/
func fbn(n int) int {
	if (n == 1 || n == 2) {
		return 1
	} else {
		return fbn(n - 1) + fbn(n - 2)
	}
}

func main() {
	res := fbn(3)
	//测试
	fmt.Println("res=", res)
	fmt.Println("res=", fbn(4)) // 3
	fmt.Println("res=", fbn(5)) // 5 
	fmt.Println("res=", fbn(6)) // 8 
}