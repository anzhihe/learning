package main
import (
	"fmt"
	"math/rand"
	"time"
)
func main() {

	//使用 for 循环完成下面的案例请编写一个程序，可以接收一个整数,表示层数，打印出金字塔

	//编程思路
	//1. 打印一个矩形
	/*

		***
		***
		***
	*/

	//2. 打印半个金字塔
	/*
		*    1 个 *
		**   2 个 *
		***  3 个 *
	*/

	//3 打印整个金字塔
	/*
	    *     1层 1 个*  规律: 2 * 层数 - 1   空格 2 规律 总层数-当前层数
	   ***    2层 3 个*  规律：2 * 层数 - 1   空格 1 规律 总层数-当前层数
	  *****   3层 5 个*	 规律：2 * 层数 - 1   空格 0 规律 总层数-当前层数
	*/
	//4 将层数做成一个变量, 先死后活
	//var totalLevel int

	//5 打印空心金字塔
	/*
		*     
	   * *    
	  *****   
	   分析：在我们给每行打印*号时，需要考虑是打印 * 还是打印 空格
	   我们的分析的结果是，每层的第一个和最后一个是打印*, 其它就应该是空的，即输出空格
	   我们还分析到一个例外情况，最后层（底层）是全部打*

	*/

	var totalLevel int = 20

	//i 表示层数
	for i := 1; i <= totalLevel; i++ {
		//在打印*前先打印空格
		for k := 1; k <= totalLevel - i; k++ {
			fmt.Print(" ")
		}

		//j 表示每层打印多少*
		for j :=1; j <= 2 * i - 1; j++ {
			if j == 1 || j == 2 * i - 1 || i == totalLevel {
				fmt.Print("*")
			} else {
				fmt.Print(" ")
			}
			
		}
		fmt.Println()
	}


	//打印出九九乘法表
	//i 表示层数
	var num int = 9
	for i := 1; i <= num; i++ {
		for j := 1; j <= i; j++ {
			fmt.Printf("%v * %v = %v \t", j, i, j * i)
		}
		fmt.Println()
	} 
	
}