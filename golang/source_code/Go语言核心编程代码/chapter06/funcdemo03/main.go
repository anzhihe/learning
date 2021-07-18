package main
import (
	"fmt"
)

func test(n int) {
	if n > 2 {
		n--
		test(n)
	}
	fmt.Println("n=", n)
}

func test2(n int) {
	if n > 2 {
		n-- //递归必须向退出递归条件逼进，否则就是无限循环调用
		test2(n)
	} else {
		fmt.Println("n=", n)
	}
}

func main() {

	//看一段代码
	//test(4) // ?通过分析来看下递归调用的特点
	test2(4) // ?通过分析来看下递归调用的特点
}