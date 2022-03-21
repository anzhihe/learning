package main

import "fmt"

func main() {
	const PI float32 = 3.14
	const pi = 3.14
	fmt.Println(PI, pi) //Go语言的语法规则比较灵活，在初始化的时候可以不用指定变量/常量的类型
	//同时为了提高代码的阅读性，可以使用 ()简化书写
	const (
		Left        = iota       //iota 初始的时候是0，每换行，自动加1
		Right       = iota       //1
		Above       = iota       //2
		Below                    //3,虽然木有显示指定iota，但是在底层还是通过iota赋值：Below=iota
		Front, Back = iota, iota //问题：Below Front,Back  4,4  ,iota换行，自动增加，否则不会增加
	)
	fmt.Println(Left, Right, Above, Below, Front, Back)
}
