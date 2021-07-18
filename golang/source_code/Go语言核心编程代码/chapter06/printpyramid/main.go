package main
import (
	"fmt"
)


//将打印金字塔的代码封装到函数中
func printPyramid(totalLevel int) {

	//i 表示层数
	for i := 1; i <= totalLevel; i++ {
		//在打印*前先打印空格
		for k := 1; k <= totalLevel - i; k++ {
			fmt.Print(" ")
		}

		//j 表示每层打印多少*
		for j :=1; j <= 2 * i - 1; j++ {
				fmt.Print("*")
		}
		fmt.Println()
	}

}
func main() {
	//调用printPyramid函数，就可以打印金字塔
	//从终端输入一个整数打印出对应的金子塔
	var n int 
	fmt.Println("请输入打印金字塔的层数")
	fmt.Scanln(&n)
	printPyramid(n)
}