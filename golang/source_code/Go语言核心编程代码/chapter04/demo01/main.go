package main
import (
	"fmt" 
)

func main() {

	//重点讲解 /、%
	//说明，如果运算的数都是整数，那么除后，去掉小数部分，保留整数部分
	fmt.Println(10 / 4) 
	
	var n1 float32 = 10 / 4 //
	fmt.Println(n1)

	//如果我们希望保留小数部分，则需要有浮点数参与运算
	var n2 float32 = 10.0 / 4
	fmt.Println(n2)

	// 演示  % 的使用 
	// 看一个公式 a % b = a - a / b * b
	// fmt.Println("10%3=", 10 % 3) // =1
	// fmt.Println("-10%3=", -10 % 3) // = -10 - (-10) / 3 * 3 = -10 - (-9) = -1
	// fmt.Println("10%-3=", 10 % -3) // =1
	// fmt.Println("-10%-3=", -10 % -3) // =-1

	// ++ 和 --的使用
	var i int = 10
	i++ // 等价 i = i + 1
	fmt.Println("i=", i) // 11
	i-- // 等价 i = i - 1
	fmt.Println("i=", i) // 10

	if i > 0 {
		fmt.Println("ok")
	}
	
}