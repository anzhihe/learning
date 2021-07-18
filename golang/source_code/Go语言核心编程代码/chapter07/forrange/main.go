package main
import (
	"fmt"
)

func main() {

	//演示for-range遍历数组
	 heroes  := [...]string{"宋江", "吴用", "卢俊义"}
	//使用常规的方式遍历，我不写了..

	for i, v := range heroes {
		fmt.Printf("i=%v v=%v\n", i , v)
		fmt.Printf("heroes[%d]=%v\n", i, heroes[i])
	}

	for _, v := range heroes {
		fmt.Printf("元素的值=%v\n", v)
	}
}