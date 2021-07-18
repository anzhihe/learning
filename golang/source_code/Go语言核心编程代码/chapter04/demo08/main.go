package main
import (
	"fmt" 
)


func main() {

	var i int = 5
	//二进制输出 
	fmt.Printf("%b \n", i)

	//八进制：0-7 ，满8进1. 以数字0开头表示
	var j int = 011 // 011=> 9
	fmt.Println("j=", j)

	//0-9及A-F，满16进1. 以0x或0X开头表示
	var k int = 0x11 // 0x11=> 16 + 1 = 17
	fmt.Println("k=", k)
}