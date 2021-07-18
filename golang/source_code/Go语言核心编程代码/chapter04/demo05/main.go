package main
import (
	"fmt" 
)

func test() int {
	return 90
}

func main() {
	//赋值运算符的使用演示
	// var i int 
	// i = 10 //基本赋值

	//有两个变量，a和b，要求将其进行交换，最终打印结果
	// a = 9 , b = 2 ==> a = 2 b = 9
	a := 9
	b := 2
	fmt.Printf("交换前的情况是 a = %v , b=%v \n", a, b)
	//定义一个临时变量
	t := a
	a = b //
	b = t //
	fmt.Printf("交换后的情况是 a = %v , b=%v \n", a, b)

	//复合赋值的操作
	a += 17 // 等价 a = a + 17
	fmt.Println("a=", a)


	var c int 
	c = a + 3 // 赋值运算的执行顺序是从右向左
	fmt.Println(c)

	//2)赋值运算符的左边 只能是变量,右边 可以是变量、表达式、常量值
	// 表达式：任何有值都可以看做表达式
	var d int
	d = a //  
	d = 8 + 2 * 8 // =的右边是表达式
	d = test() + 90 //  =的右边是表达式
	//d = 890 // 890常量
	fmt.Println(d)
}