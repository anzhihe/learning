package main
import (
	"go_code/familyaccount/utils"
	"fmt"
)
func main() {

	fmt.Println("这个是面向对象的方式完成~~")
	utils.NewFamilyAccount().MainMenu() //思路非常清晰
}