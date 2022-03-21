package main

import "fmt"

func main() {
	var number int = 123
	number = 456
	fmt.Println(number)
	//const num int
	//num=123 错误：常量在赋值的时候就需要进行初始化操作
	const num int = 123
	//num = 456 错误：常量不能进行任何的更改
	//小结：变量：是可以变化的量，常量的值不能进行任何的更改；常量的应用场景：主要用在程序一开始就确定好值，
	//后续不能进行任何的修改（比如：圆周率、游戏的等级等）
	const NUM = 333 //充分说明：Go语言区分大小写；多学一招；常量一般用大写字母来表示
	fmt.Println(NUM)
	fmt.Println("常量是：", num)
	m := 3 + 2i
	fmt.Println(m)
	fmt.Printf("m变量的格式是：%T", m)
}
