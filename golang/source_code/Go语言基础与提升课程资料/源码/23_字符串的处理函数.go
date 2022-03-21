package main

import (
	"fmt"
	"strings"
)

func main() {
	str := "hello Go 语言Go  Go"
	flag := strings.Contains(str, "Go") //判断字符串str是否包含指定的子字符串Go
	fmt.Println("str字符串是否包含 Go：", flag)

	arr := []string{"Go语言", "Java语言", "C语言"}
	str1 := strings.Join(arr, ";") //通过子字符串 ;将切片arr对应的元素连接起来，形成新的字符串
	fmt.Println("拼接之后的字符串为：", str1)

	arr1 := strings.Split(str1, ";") // 通过指定的子字符串 ; 将字符串str1分割成切片
	fmt.Println("字符串分割成切片的值为：", arr1)

	arr2 := strings.Fields(str) //依据空格，将字符串分割成对应的切片
	fmt.Println("通过空格将字符串分割成对应的切片", arr2)

	index := strings.Index(str, "Go") //在字符串str中找到Go所在的索引位置，如果不存在，则返回-1
	fmt.Println("str中Go所在的位置为：", index)

	str2 := strings.Replace(str, "Go", "区块链", -1) //在字符串str中用区块链替换所有的Go；-1：代表：全部替换
	fmt.Println("在字符串str中用区块链替换Go，替换次数：全部替换", str2)

	str3 := "   Go语言是一门很强大的编程语言   "
	str4 := strings.Trim(str3, " ")
	fmt.Println(len(str3), len(str4))

}
