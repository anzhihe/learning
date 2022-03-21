package TestPackage

import "fmt"

//如果是不同包下调用函数，函数名首字母需要大写
func Add(args ...int) int { //求和函数
	sum := 0
	for _, v := range args {
		sum += v
	}
	return sum
}
func ShowAll() {
	fmt.Println("调用相同包下的函数show()")
	show()
}
