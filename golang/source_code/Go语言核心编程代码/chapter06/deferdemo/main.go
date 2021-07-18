package main
import (
	"fmt"
)

func sum(n1 int, n2 int) int {
	
	//当执行到defer时，暂时不执行，会将defer后面的语句压入到独立的栈(defer栈)
	//当函数执行完毕后，再从defer栈，按照先入后出的方式出栈，执行
	defer fmt.Println("ok1 n1=", n1) //defer 3. ok1 n1 = 10
	defer fmt.Println("ok2 n2=", n2) //defer 2. ok2 n2= 20
	//增加一句话
	n1++ // n1 = 11
	n2++ // n2 = 21
	res := n1 + n2 // res = 32
	fmt.Println("ok3 res=", res) // 1. ok3 res= 32
	return res

}

func main() {
	res := sum(10, 20)
	fmt.Println("res=", res)  // 4. res= 32
}
	