package main

import (
	"fmt"
	"unsafe"
)

func main() {
	a := 123
	fmt.Println(&a) //0xc00006c090 程序在执行时，变量a的地址是随机分配的，每一次都不用
	b := 1
	c := b << 1
	c <<= 1        //c=c<<1
	fmt.Println(c) //问题：c的值是什么？
	d := 123.3
	fmt.Println(int(d))
	//问题：如果要输出变量a的大小（占用内存），怎么操作
	fmt.Println(unsafe.Sizeof(a), unsafe.Sizeof(d)) //Sizeof:输出变量占用内存的大小
	//===根据输入的年份，判断是否是闰年===
	/*
		符合下面两个条件之一
		1、年份能够被400整除.(2000)
		2、年份能够被4整除但不能被100整除.(2008)
	*/
	var year int
	fmt.Println("请输入年份：")
	fmt.Scanf("%d", &year)
	flag := year%400 == 0 || (year%4 == 0 && year%100 != 0)
	fmt.Println("您输入的年份是否是闰年：", flag)
}
