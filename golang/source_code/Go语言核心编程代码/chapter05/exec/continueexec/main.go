package main
import "fmt"
func main() {
	//continue实现 打印1——100之内的奇数[要求使用for循环+continue]

	// for i := 1; i <= 100; i++ {
	// 	if i % 2 == 0 {
	// 		continue
	// 	}
	// 	fmt.Println("奇数是", i)
	// }

	//从键盘读入个数不确定的整数，并判断读入的正数和负数的个数，输入为0时结束程序

	var positiveCount int // 正数的个数
	var negativeCount int // 负数个数
	var num int
	for {
		fmt.Println("请输入一个整数")
		fmt.Scanln(&num)
		if num == 0 {
			break //终止for循环
		}

		if num > 0 {
			positiveCount++
			continue//结束本次循环，进入下次循环
		}
		negativeCount++
	}
	fmt.Printf("正数个数是%v 负数的个数是%v\n", positiveCount, negativeCount)
}