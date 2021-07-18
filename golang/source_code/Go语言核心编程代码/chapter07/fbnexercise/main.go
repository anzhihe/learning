package main
import (
	"fmt"
)

func fbn(n int) ([]uint64) {
	//声明一个切片，切片大小 n
	fbnSlice := make([]uint64, n)
	//第一个数和第二个数的斐波那契 为1
	fbnSlice[0] = 1
	fbnSlice[1] = 1
	//进行for循环来存放斐波那契的数列
	for i := 2; i < n; i++ {
		fbnSlice[i] = fbnSlice[i - 1] + fbnSlice[i - 2]
	}

	return fbnSlice
}

func main() {

	/*
	1)可以接收一个 n int
	2)能够将斐波那契的数列放到切片中
	3)提示, 斐波那契的数列形式:
	arr[0] = 1; arr[1] = 1; arr[2]=2; arr[3] = 3; arr[4]=5; arr[5]=8

	思路
	1. 声明一个函数 fbn(n int) ([]uint64)
	2. 编程fbn(n int) 进行for循环来存放斐波那契的数列  0 =》 1 1 =》 1
	*/

	//测试一把看看是否好用
	fnbSlice := fbn(20)
	fmt.Println("fnbSlice=", fnbSlice)

}