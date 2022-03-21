package main

import (
	"fmt"
	"strconv"
)

func main() {
	fmt.Println("=================int--->string===================")
	i := 100
	str := strconv.Itoa(i)
	fmt.Printf("转换之前的数据类型为：%T,转换之后的数据类型为：%T;转换之后的数据为：%v\n", i, str, str)
	fmt.Println("=================string--->int===================")
	j, err := strconv.Atoi(str) //如果转换失败，err对应的数据不为空，提示错误信息
	if err != nil {             //nil:在go语言中代表空
		fmt.Println("转换失败！", err)
		return
	}
	fmt.Printf("转换之后的数据类型：%T，对应的数据为；%v\n", j, j)
	fmt.Println("=================其他类型的转换===================")
	flag := true
	str1 := strconv.FormatBool(flag)
	fmt.Printf("转换之前的数据类型为：%T;转换之后的数据类型为：%T；对应的数据为：%v\n", flag, str1, str1)
	b, err := strconv.ParseBool(str1)
	if err != nil {
		fmt.Println("转换错误！", err)
		return
	}
	fmt.Printf("转换之后的数据类型为：%T，数据为：%v\n", b, b)
	fmt.Println("=================float类型的转换========================")
	f1 := 20 / 3.0  //特别注意：如果是20/3 结果为6；原因：整数/整数=整数
	fmt.Println(f1) //6  6.66666
	str2 := strconv.FormatFloat(f1, 'f', 2, 64)
	fmt.Printf("转换之后的数据类型为；%T；对应的数据为：%v\n", str2, str2)

}
