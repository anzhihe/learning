package main
import (
	_ "fmt"
)

//一个被测试函数
func addUpper(n int)  int {
	res := 0
	for i := 1; i <= n - 1; i++ {
		res += i
	}
	return res
}

func addUpper2(n int)  int {
	res := 0
	for i := 1; i <= n - 1; i++ {
		res += i
	}
	return res
}

func main() {

	//传统的测试方法，就是在main函数中使用看看结果是否正确
	// res := addUpper(10) // 1.+ 10 = 55
	// if res != 55 {
	// 	fmt.Printf("addUpper错误 返回值=%v 期望值=%v\n", res, 55)
	// } else {
	// 	fmt.Printf("addUpper正确 返回值=%v 期望值=%v\n", res, 55)
	// }
}