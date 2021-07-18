package main
import (
	"fmt"
	_ "math"
)

func main(){
	//岳小鹏参加Golang考试，他和父亲岳不群达成承诺：
	// 如果：
	// 成绩为100分时，奖励一辆BMW；
	// 成绩为(80，99]时，奖励一台iphone7plus；
	// 当成绩为[60,80]时，奖励一个 iPad；
	// 其它时，什么奖励也没有。
	// 请从键盘输入岳小鹏的期末成绩，并加以判断

	//分析思路
	//1. score 分数变量 int
	//2. 选择多分支流程控制
	//3. 成绩从键盘输入 fmt.Scanln

	/*
	var score int
	fmt.Println("请输入成绩:")
	fmt.Scanln(&score)

	//多分支判断
	if score == 100 {
		fmt.Println("奖励一辆BMW")
	} else if score > 80 && score <= 99 {
		fmt.Println("奖励一台iphone7plus")
	} else if score >= 60 && score <= 80 {
		fmt.Println("奖励一个 iPad")
	} else {
		fmt.Println("什么都不奖励")
	}

	//使用陷阱.....只会输出ok1...

	var n int = 10
	if n > 9 {
		fmt.Println("ok1") //输出 ok1
	} else if  n > 6 {
		fmt.Println("ok2")
	} else if n > 3 {
		fmt.Println("ok3")
	} else {
		fmt.Println("ok4")
	} */

	// var b bool = true
	// if b == false { 	//如果写成 b = false; 能编译通过吗？如果能，结果是？
	// 	fmt.Println("a")
	// } else if b {
	// 	fmt.Println("b") // b
	// } else if !b { 
	// 	fmt.Println("c")//c
	// } else {
	// 	fmt.Println("d")
	// }
	

	//求ax2+bx+c=0方程的根。a,b,c分别为函数的参数，如果：b2-4ac>0，则有两个解；
	// b2-4ac=0，则有一个解；b2-4ac<0，则无解； 
	// 提示1：x1=(-b+sqrt(b2-4ac))/2a                            
	//        X2=(-b-sqrt(b2-4ac))/2a
	// 提示2：math.Sqrt(num); 可以求平方根 需要引入 math包

	//分析思路
	//1. a,b,c 是三个float64
	//2. 使用到给出的数学公式 
	//3. 使用到多分支
	//4. 使用math.Squr方法 =》手册

	//走代码
	// var a float64 = 2.0
	// var b float64 = 4.0
	// var c float64 = 2.0

	// m := b * b - 4 * a * c
	// //多分支判断
	// if m > 0 {
	// 	x1 := (-b + math.Sqrt(m)) / 2 * a
	// 	x2 := (-b - math.Sqrt(m)) / 2 * a
	// 	fmt.Printf("x1=%v x2=%v", x1, x2)
	// } else if m == 0 {
	// 	x1 := (-b + math.Sqrt(m)) / 2 * a
	// 	fmt.Printf("x1=%v", x1)
	// } else {
	// 	fmt.Println("无解...")
	// }


	// 大家都知道，男大当婚，女大当嫁。那么女方家长要嫁女儿，当然要提出一定的条件：
	//高：180cm以上；富：财富1千万以上；帅：是。条件从控制台输入。
	// 如果这三个条件同时满足，则：“我一定要嫁给他!!!”
	// 如果三个条件有为真的情况，则：“嫁吧，比上不足，比下有余。”
	// 如果三个条件都不满足，则：“不嫁！”

	// var height int32  | var money float32 | var handsome bool

	//分析思路
	//1. 应该设计三个变量 var height int32  | var money float32 | var handsome bool
	//2. 而且需要从终端输入 fmt.Scanln
	//3. 使用多分支if--else if -- else
	var height int32
	var money float32
	var handsome bool

	fmt.Println("请输入身高(厘米)")
	fmt.Scanln(&height)
	fmt.Println("请输入财富(千万)")
	fmt.Scanln(&money)
	fmt.Println("请输入是否帅(true/false)")
	fmt.Scanln(&handsome)

	if height > 180 && money > 1.0 && handsome {
		fmt.Println("我一定要嫁给他!!!")
	} else if height > 180 || money > 1.0 || handsome {
		fmt.Println("嫁吧，比上不足，比下有余")
	} else {
		fmt.Println("不嫁....")
	}



}