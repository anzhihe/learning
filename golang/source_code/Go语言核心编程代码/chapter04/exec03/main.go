package main
import (
	"fmt" 
)
func main() {

	//求两个数的最大值
	var n1 int = 10
	var n2 int = 40
	var max int
	if n1 > n2 {
		max = n1
	} else {
		max = n2
	}
	fmt.Println("max=", max)

	//求出三个数的最大值思路：先求出两个数的最大值，
	//然后让这个最大值和第三数比较，在取出最大值
	var n3 = 45
	if n3 > max {
		max = n3
	}
	fmt.Println("三个数中最大值是=", max)

}