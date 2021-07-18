package main
import (
	"fmt"
)


//函数中的变量是局部的，函数外不生效
func test() {
	//n1 是 test函数的局部变量, 只能在test函数中使用
	//var n1 int = 10
}

func test02(n1 int) {
	
	n1 = n1 + 10
	fmt.Println("test02() n1= ", n1)
}

func test02(n1 int , n2 int) {
	
}

// n1 就是 *int 类型
func test03(n1 *int) {
	fmt.Printf("n1的地址 %v\n",&n1)
	*n1 = *n1 + 10
	fmt.Println("test03() n1= ", *n1) // 30
}




func main() {
	// num := 20
	// test02(num)
	// fmt.Println("main() num= ", num)

	num := 20
	fmt.Printf("num的地址=%v\n", &num)
	test03(&num)
	fmt.Println("main() num= ", num) // 30
}