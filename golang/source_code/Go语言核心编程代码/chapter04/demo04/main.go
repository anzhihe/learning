package main
import (
	"fmt" 
)

//声明一个函数(测试)
func test() bool {
	fmt.Println("test....")
	return true
}

func main() {

	var i int = 10
	//短路与
	//说明 因为  i < 9 为 false ,因此后面的 test() 就不执行
	// if i < 9 && test() {
	// 	fmt.Println("ok...")
	// }

	if i > 9 || test() {
		fmt.Println("hello...")
	}

   /*

	//演示逻辑运算符的使用  &&
	var age int = 40
	if age > 30 && age < 50 {
		fmt.Println("ok1")
	}

	if age > 30 && age < 40 {
		fmt.Println("ok2")
	}

	//演示逻辑运算符的使用  ||

	if age > 30 || age < 50 {
		fmt.Println("ok3")
	}

	if age > 30 || age < 40 {
		fmt.Println("ok4")
	}

	//演示逻辑运算符的使用  !

	if age > 30 {
		fmt.Println("ok5")
	}

	if !(age > 30) {
		fmt.Println("ok6")
	} */

}