package main
import "fmt"

func main(){

	//使用while方式输出10句 "hello,world"
	//循环变量初始化
	var i int = 1
	for {
		if i > 10 { //循环条件
			break // 跳出for循环,结束for循环
		}
		fmt.Println("hello,world", i)
		i++ //循环变量的迭代
	}

	fmt.Println("i=", i)


	//使用的do...while实现完成输出10句”hello,ok“
	var j int = 1
	for {
		fmt.Println("hello,ok", j)
		j++ //循环变量的迭代
		if j > 10 {
			break //break 就是跳出for循环
		}
	}

	
}