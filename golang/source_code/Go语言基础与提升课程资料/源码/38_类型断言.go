package main

import (
	"fmt"
)

func main() {
	fmt.Println("==================类型断言的基本使用=====================")
	var i interface{} = 123
	var a int
	a, ok := i.(int)
	if ok {
		fmt.Println("类型断言成功！")
	} else {
		fmt.Println("类型断言失败！")
	}
	fmt.Printf("变量a的值为：%v\n", a)
	fmt.Println("====================类型断言复杂（常用写法）=================")
	if v, ok := i.(string); ok {
		fmt.Println("断言成功！", v)
	} else {
		fmt.Println("断言失败！")
	}
	fmt.Println("=================类型断言复杂应用==========================")
	s1 := make([]interface{}, 0)
	s1 = append(s1, 123, 98.9, "Go语言", true)
	for index, data := range s1 {
		if v, ok := data.(int); ok {
			fmt.Printf("第%v个元素，数据类型为：%T；数据为：%v\n", index, v, v)
		} else if v, ok := data.(string); ok {
			fmt.Printf("第%v个元素，数据类型为：%T；数据为：%v\n", index, v, v)
		} else if v, ok := data.(bool); ok {
			fmt.Printf("第%v个元素，数据类型为：%T；数据为：%v\n", index, v, v)
		} else if v, ok := data.(float64); ok {
			fmt.Printf("第%v个元素，数据类型为：%T；数据为：%v\n", index, v, v)
		} else {
			fmt.Println("数据类型为其他！")
		}
	}
}
