package main
import "fmt"

//演示golang中标识符的使用
func main() {

	//Golang中严格区分大小写
	//golang 中 认为 num 和 Num是不同的变量
	var num int = 10
	var Num int = 20
	fmt.Printf("num=%v Num=%v\n", num, Num)

	//标识符不能包含空格
	//var ab c int = 30

	//_ 是空标志符，用于占用
	// var _ int = 40 //error
	// fmt.Println(_)

	var int int = 90
	fmt.Println(int)
}