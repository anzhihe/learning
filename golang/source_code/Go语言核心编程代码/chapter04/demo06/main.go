package main
import (
	"fmt" 
)
func main() {
	//演示一把 & 和 *的使用

	a := 100
	fmt.Println("a 的地址=", &a)

	var ptr *int = &a
	fmt.Println("ptr 指向的值是=", *ptr)

	var n int 
	var i int = 10
	var j int = 12
	//传统的三元运算
	//n = i > j ? i : j
	if i > j {
		n = i
	} else {
		n = j
	}
	fmt.Println("n=", n) // 12
}