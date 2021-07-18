package main
import (
	"fmt"
	"math/rand"
	"time"
)

func main() {

	//我们为了生成一个随机数，还需要个rand设置一个种子.
	//time.Now().Unix() : 返回一个从1970:01:01 的0时0分0秒到现在的秒数
	//rand.Seed(time.Now().Unix())
	//如何随机的生成1-100整数
	//n := rand.Intn(100) + 1 // [0 100)
	//fmt.Println(n)

	//随机生成1-100的一个数，直到生成了99这个数，看看你一共用了几次
	//分析思路：
	//编写一个无限循环的控制，然后不停的随机生成数，当生成了99时，就退出这个无限循环==》break
	var count int = 0
	for {
		rand.Seed(time.Now().UnixNano())
		n := rand.Intn(100) + 1
		fmt.Println("n=", n)
		count++
		if (n == 99) {
			break //表示跳出for循环
		}
	}

	fmt.Println("生成 99 一共使用了 ", count)


	//这里演示一下指定标签的形式来使用 break
	lable2: 
	for i := 0; i < 4; i++ {
		//lable1: // 设置一个标签
		for j := 0; j < 10; j++ {
			if j == 2 {
				//break // break 默认会跳出最近的for循环
				//break lable1 
				break lable2 // j=0 j=1
			}
			fmt.Println("j=", j) 
		}
	}

	
}