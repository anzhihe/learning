package main

import "fmt"

func main() {
	f1 := Test()
	f2 := Test()
	f3 := Test()
	fmt.Println(f1, f2, f3) //f1,f2,f3=?
	//虽然Test()函数调用了3次，但输出的都是1；
	//原因：每次调用Test()函数，都是重新分配内存，变量会重新声明，函数执行完毕，x会自动释放被占用的内存
	fmt.Println("===========匿名函数执行效果=============")
	f := func() int {
		var i int
		i++
		return i
	}
	fmt.Println(f(), f(), f())
	fmt.Println("===============闭包====================")
	var x int
	f4 := func() int {
		x += 2
		return x
	}
	fmt.Println(f4(), f4(), f4())
	fmt.Printf("%T", f4)
	fmt.Println("=================闭包的函数操作=====================")
	f5 := Test1()
	fmt.Println(f5(), f5(), f5()) //输出的值是什么？
}
func Test() int {
	var x int
	x++
	return x
}

func Test1() func() int {
	var x int
	/*f:= func() int{
		x++
		return x
	}
	return f*/
	return func() int {
		x++
		return x
	}
}
