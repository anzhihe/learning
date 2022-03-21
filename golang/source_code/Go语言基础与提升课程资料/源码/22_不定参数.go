package main

import "fmt"

func main() {
	fmt.Println("==============没有任何参数的情况===============")
	Test01()
	fmt.Println("==============有2个参数的情况=================")
	Test01(1, 2)
	fmt.Println("===============参数为切片的情况===================")
	s := make([]int, 0)                         //定义一个切片，长度、容量都为0
	s = append(s, 111, 222, 333, 444, 555, 666) //给切片s追加数据
	Test01(s...)                                //函数的调用 获取切片的元素  s...
}
func Test01(args ...int) { //可以接收多个（0-n）个int类型的参数
	fmt.Println("执行带有不定参数列表的函数")
	for index, value := range args {
		fmt.Println(index, value)
	}
}

// arg1：string  ;args：int...
func Test02(arg1 string, args ...int) {

}

/*func Test03(arg0 float64,arg1 ...string,arg2 ...int)  {

}*/
//以上充分说明，不定参数在函数列表中只能有一个，而且只能是参数列表中的最后一个
