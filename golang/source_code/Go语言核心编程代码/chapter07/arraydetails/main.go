package main
import (
	"fmt"
)

//函数
func test01(arr [3]int) {
	arr[0] = 88
} 

//函数
func test02(arr *[3]int) {
	fmt.Printf("arr指针的地址=%p", &arr)
	(*arr)[0] = 88 //!!
} 

func main() {
	
	/*
	//数组是多个相同类型数据的组合,一个数组一旦声明/定义了,其长度是固定的, 不能动态变化。
	var arr01 [3]int
	arr01[0] = 1
	arr01[1] = 30
	//这里会报错
	arr01[2] = 1.1  
	//其长度是固定的, 不能动态变化,否则报越界
	arr01[3] = 890

	fmt.Println(arr01)
	*/

	//数组创建后，如果没有赋值，有默认值(零值)
	//1. 数值(整数系列, 浮点数系列) =>0
	//2. 字符串 ==> ""
	//3. 布尔类型 ==> false

	var arr01 [3]float32
	var arr02 [3]string
	var arr03 [3]bool
	fmt.Printf("arr01=%v arr02=%v arr03=%v\n", arr01, arr02, arr03)

	//数组的下标是从0开始的

	// var arr04 [3]string // 0 - 2
	// var index int = 3
	// arr04[index] = "tom" // 因为下标是 0 - 2 ,因此arr04[3]就越界

	//Go的数组属值类型， 在默认情况下是值传递， 因此会进行值拷贝。数组间不会相互影响

	// arr := [3]int{11, 22, 33}
	// test01(arr)
	// fmt.Println("main arr=", arr) //


	arr := [3]int{11, 22, 33}
	fmt.Printf("arr 的地址=%p", &arr)
	test02(&arr)
	fmt.Println("main arr=", arr)
}