package main
import (
	"fmt"
)

func main() {

	//演示二维数组的遍历
	var arr3  = [2][3]int{{1,2,3}, {4,5,6}}

	//for循环来遍历
	for i := 0; i < len(arr3); i++ {
		for j := 0; j < len(arr3[i]); j++ {
			fmt.Printf("%v\t", arr3[i][j])
		}
		fmt.Println()
	}

	//for-range来遍历二维数组
	for i, v := range arr3 {
		for j, v2 := range v {
			fmt.Printf("arr3[%v][%v]=%v \t",i, j, v2)
		}
		fmt.Println()	
	}
}