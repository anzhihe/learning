package main

import "fmt"

type operate struct {
	num1 int
	num2 int
}

func (o operate) Add() int {
	return o.num1 + o.num2
}
func (o *operate) Sub() int {
	return o.num1 - o.num2
}
func main() {
	fmt.Println("============一般方法的调用=============")
	o := operate{}
	o.num1 = 456
	o.num2 = 123
	fmt.Println(o.Add(), o.Sub())
	fmt.Println("================值方法形式的调用==============")
	f1 := o.Add
	f2 := o.Sub
	fmt.Println(f1, f2, f1(), f2())
	fmt.Println("===============表达式形式的调用================")
	f3 := operate.Add
	res1 := f3(o)
	f4 := (*operate).Sub
	res2 := f4(&o)
	fmt.Println(res1, res2)

}
