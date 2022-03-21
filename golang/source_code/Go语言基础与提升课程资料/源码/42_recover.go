package main

import "fmt"

func main() {
	defer func() {
		v := recover()
		fmt.Println("错误信息：", v)
	}() //recover调用：1）需要结合defer使用；2）只能在函数内部，一般是匿名函数
	arr := [3]int{}
	i := 100
	arr[i] = 66
	fmt.Println(arr)
	fmt.Println("===================================") //重新遇到panic错误，会结束执行。虽然有recover捕获异常
	recoverTest01(100, 0)
	//recover只能捕获一个panic错误信息，因为：遇到panic错误，程序会结束运行。
	//panic错误：如果不用recover捕获，是异常推出；捕获之后是正常退出
}
func recoverTest01(a, b float64) float64 {
	if b == 0 {
		panic("被除数不能为0")
		return 0
	}
	return a / b
}
