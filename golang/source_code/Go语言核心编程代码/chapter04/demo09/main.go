package main
import (
	"fmt" 
)
func main() {

	//位运算的演示
	fmt.Println(2&3) // 2
	fmt.Println(2|3) // 3
	fmt.Println(2^3) // 3
	fmt.Println(-2^2) //-4

	a := 1 >> 2 //0
	c := 1 << 2 //4
	fmt.Println("a=", a, "c=", c)
	
}