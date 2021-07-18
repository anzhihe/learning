package main
import (
	"fmt"
)

/*
题2：求函数值已知 f(1)=3; f(n) = 2*f(n-1)+1; 请使用递归的思想编程，求出 f(n)的值?

*/
func f(n int) int {
	if n == 1 {
		return 3
	} else {
		return 2 * f(n - 1) + 1
	}
}
func main(){

	//测试一下
	fmt.Println("f(1)=", f(1))
	fmt.Println("f(5)=", f(5))
}