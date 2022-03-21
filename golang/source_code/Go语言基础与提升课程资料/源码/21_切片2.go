package main

import "fmt"

func main() {
	fmt.Println("============append函数的基本使用==========")
	s1 := []int{111, 222, 333, 444, 555, 666}
	fmt.Printf("切片的长度：%v，切片的容量：%v, 切片对应的数据为：%v\n", len(s1), cap(s1), s1)
	s1 = append(s1, 777)
	fmt.Printf("扩容之后的切片s1的长度为：%v，容量为：%v，对应的数据为：%v\n", len(s1), cap(s1), s1)
	//错误： s1[10] = 888再次提示：切片的有效赋值范围：为切片对应的长度范围内
	s1 = append(s1, 888, 999) //len=？  cap=？
	fmt.Printf("扩容之后的切片s1的长度为：%v，容量为：%v，对应的数据为：%v\n", len(s1), cap(s1), s1)
	//只有在切片的长度==容量的时候，扩容的切片，容量才会增加（一般容量会翻番，前提条件是：容量<1024）
	fmt.Println("============切片的容量大于1024的情况===================")
	s2 := make([]int, 1024, 1024)
	s2 = append(s2, 333)
	fmt.Printf("容量为1024的切片s2扩容的长度为:%v;容量为：%v\n", len(s2), cap(s2))
	fmt.Println("================扩容的数据为切片的情况=================")
	s2 = append(s2, s1...)
	fmt.Println("追加切片所有元素的情况：", s2)
	fmt.Println("=======================copy函数的使用===========================")
	data1 := []int{111, 222, 333, 444, 555, 666, 777, 888, 999, 1000}
	data2 := []int{123, 456, 789}
	copy(data1, data2)
	fmt.Println(data1)
	data3 := []int{1, 2, 3}
	copy(data3, data1)
	fmt.Println(data3)
}
