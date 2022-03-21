package main

import "fmt"

func main() {
	//数组的定义
	var arr0 [10]int
	arr0[0] = 1
	arr0[1] = 2
	fmt.Println("arr0的值是：", arr0)
	for i := 0; i < 10; i++ {
		arr0[i] = i + 1
	}
	fmt.Println("通过for循环赋值之后的arr0的值是：", arr0)
	//数组的4种初始化方法
	var arr1 [3]int = [3]int{1, 2, 3}
	fmt.Println("初始化方法1：", arr1)
	var arr2 = [3]int{4, 5, 6}
	fmt.Println("初始化方法2：", arr2)
	var arr3 = [...]int{8, 9, 10} //数组元素个数不确定的情况下使用
	fmt.Println("初始化方法3：", arr3)
	var arr4 = [3]int{1: 100}
	fmt.Println("初始化方法4：", arr4)
	fmt.Println("=============数组的遍历==============")
	strArr := [3]string{"Go语言", "Java语言", "区块链"}
	for i := 0; i < len(strArr); i++ {
		fmt.Printf("第%d个元素的值是：%v\t", i, strArr[i])
	}
	fmt.Println("\n===========for-range遍历===========")
	for index, value := range strArr {
		fmt.Println(index, value)
	}
	fmt.Println("=========丢弃下标的情况===========")
	for _, value := range strArr {
		fmt.Println(value)
	}

}
