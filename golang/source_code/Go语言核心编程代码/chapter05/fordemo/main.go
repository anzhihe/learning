package main
import (
	"fmt" 
)

func main() {
	//输出10句 "你好，尚硅谷"

	// fmt.Println("你好，尚硅谷")
	// fmt.Println("你好，尚硅谷")
	// fmt.Println("你好，尚硅谷")
	// fmt.Println("你好，尚硅谷")
	// fmt.Println("你好，尚硅谷")
	// fmt.Println("你好，尚硅谷")
	// fmt.Println("你好，尚硅谷")
	// fmt.Println("你好，尚硅谷")

	// fmt.Println("你好，尚硅谷")
	// fmt.Println("你好，尚硅谷")
	// fmt.Println("你好，尚硅谷")
	// fmt.Println("你好，尚硅谷")
	// fmt.Println("你好，尚硅谷")
	// fmt.Println("你好，尚硅谷")
	// fmt.Println("你好，尚硅谷")
	// fmt.Println("你好，尚硅谷")


	// fmt.Println("你好，尚硅谷")
	// fmt.Println("你好，尚硅谷")
	// fmt.Println("你好，尚硅谷")
	// fmt.Println("你好，尚硅谷")
	// fmt.Println("你好，尚硅谷")
	// fmt.Println("你好，尚硅谷")
	// fmt.Println("你好，尚硅谷")
	// fmt.Println("你好，尚硅谷")

	//golang中，有循环控制语句来处理循环的执行某段代码的方法->for循环
	//for循环快速入门
	
	for i := 1; i <= 10; i++ {
		fmt.Println("你好，尚硅谷", i)
	}



	//for循环的第二种写法
	j := 1 //循环变量初始化
	for j <= 10 { //循环条件
		
		fmt.Println("你好，尚硅谷~", j)
		j++ //循环变量迭代
	}

	//for循环的第三种写法, 这种写法通常会配合break使用
	k := 1
	for {  // 这里也等价 for ; ; { 
		if k <= 10 {
			fmt.Println("ok~~", k)
		} else {
			break //break就是跳出这个for循环
		}
		k++
	}


	//字符串遍历方式1-传统方式
	// var str string = "hello,world!北京"
	// for i := 0; i < len(str); i++ {
	// 	fmt.Printf("%c \n", str[i]) //使用到下标...
	// }

	//字符串遍历方式1-传统方式
	var str string = "hello,world!北京"
	str2 := []rune(str) // 就是把 str 转成 []rune
	for i := 0; i < len(str2); i++ {
		fmt.Printf("%c \n", str2[i]) //使用到下标...
	}

	fmt.Println()
	//字符串遍历方式2-for-range
	str = "abc~ok上海"
	for index, val := range str {
		fmt.Printf("index=%d, val=%c \n", index, val)
	}
}