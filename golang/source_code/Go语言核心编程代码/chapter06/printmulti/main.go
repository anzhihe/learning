package main
import (
	"fmt"
)

//编写一个函数调用九九乘法表
func printMulti(num int) {

	//打印出九九乘法表
	//i 表示层数
	for i := 1; i <= num; i++ {
		for j := 1; j <= i; j++ {
			fmt.Printf("%v * %v = %v \t", j, i, j * i)
		}
		fmt.Println()
	} 

}

func main() {

	//从终端输入一个整数表示要打印的乘法表对应的数
	var num int
	fmt.Println("请输入九九乘法表的对应数")
	fmt.Scanln(&num)
	printMulti(num)
}