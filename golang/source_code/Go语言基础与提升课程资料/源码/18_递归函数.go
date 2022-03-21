package main

import "fmt"

func main() {
	//fmt.Println(Fac(10))
	//fmt.Println(fbn(6))
	fmt.Println(sum01(100))
}

//求：n! = 1 * 2 * 3 * ... * n
//n！=n*（n-1）!;0!=1
func Fac(n int) int { //求阶层的函数，n
	if n > 0 {
		return n * Fac(n-1) //调用自身（n-1）
	}
	return 1
}

/*
斐波那契数列：1,1,2,3,5,8,13...
*/
func fbn(n int) int {
	if n == 1 || n == 2 {
		return 1
	} else {
		return fbn(n-1) + fbn(n-2)
	}
}

/*
1+2+3+4+...+100
*/
func sum01(n int) int {
	if n == 1 {
		return 1

	} else {
		return n + sum01(n-1)
	}
}
