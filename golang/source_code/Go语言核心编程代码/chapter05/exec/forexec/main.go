package main
import "fmt"

func main() {
	//打印1~100之间所有是9的倍数的整数的个数及总和

	//分析思路
	//1. 使用for循环对 max 进行遍历
	//2. 当一个数%9 ==0 就是9的倍数
	//3. 我们需要声明两个变量 count 和 sum 来保存个数和总和
	var max uint64 = 100
	var count uint64 = 0
	var sum uint64 = 0
	var i uint64 = 1
	for ; i <= max; i++ {
		if i % 9 == 0 {
			count++
			sum += i
		}
	}
	fmt.Printf("count=%v sum=%v\n", count, sum)

	fmt.Println("--------------------------------")
	//完成下面的表达式输出 ，6是可变的
	var n int = 60
	for i := 0; i <= n; i++ {
		fmt.Printf("%v + %v = %v \n", i, n - i, n)
	}
}