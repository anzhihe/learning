package main

import "fmt"

func main() {
	//切片的创建
	s1 := []int{1, 2, 3, 4}
	fmt.Println(s1)
	s2 := make([]int, 5, 10) //长度为5，容量为10；
	fmt.Println(s2, len(s2), cap(s2))
	s3 := make([]int, 5) //长度：5，容量5
	fmt.Println(s3, len(s3), cap(s3))
	s2[4] = 333
	//错误：s2[9] = 666 赋值只能是长度范围内，容量代表可以拓展的范围（预留的）
	fmt.Println("=========切片的遍历==========")
	for i := 0; i < len(s1); i++ {
		fmt.Printf("%v\t", s1[i])
	}
	fmt.Println("\n通过for-range遍历")
	for index, value := range s1 {
		fmt.Println(index, value)
	}
	fmt.Println("============数组--->切片 ==============")
	arr := [10]int{111, 222, 333, 444, 555, 666, 777, 888, 999, 1000}
	s4 := arr[:] //将数组arr转换为切片
	fmt.Printf("s4的内容是：%v，类型是：%T\n", s4, s4)
	s5 := arr[2:8]
	fmt.Println(s5)
}
