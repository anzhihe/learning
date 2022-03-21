package main

import (
	"errors"
	"fmt"
)

func main() {
	testPanic1()
	//testPanic2() //特别注意：一旦调用panic函数，程序会终止，不会继续执行
	res := dev1(100, 8)
	fmt.Println(res)
	res1 := dev1(100, 0)
	fmt.Println(res1)
}
func testPanic1() error {
	fmt.Println("error接口的函数")
	return errors.New("错误类型为error接口的函数")
}
func testPanic2() {
	fmt.Println("执行panic函数")
	panic("程序发生了严重的错误！")

}
func dev1(a, b float64) float64 {
	if b == 0 {
		panic("被除数不能为0！")
	}
	return a / b
}
