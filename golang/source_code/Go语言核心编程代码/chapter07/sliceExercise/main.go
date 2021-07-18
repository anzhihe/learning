package main
import (
	"fmt"
)

func test(slice []int) {
	slice[0] = 100  //这里修改slice[0],会改变实参
	}
	
func main() {

	var slice = []int {1, 2, 3, 4}
	fmt.Println("slice=", slice) // [1,2,3,4]
	test(slice)
	fmt.Println("slice=", slice) // [100, 2, 3, 4]


}