package main
import (
	"fmt" 
)
func main() {

	//假如还有97天放假，问：xx个星期零xx天
	var days int = 97
	var week int = days / 7
	var day int = days % 7
	fmt.Printf("%d个星期零%d天\n", week, day)


	//定义一个变量保存华氏温度，华氏温度转换摄氏温度的公式为：
	//5/9*(华氏温度-100),请求出华氏温度对应的摄氏温度
	var huashi float32 = 134.2
	var sheshi float32 = 5.0 / 9 * (huashi - 100)
	fmt.Printf("%v 对应的摄氏温度=%v \n", huashi, sheshi)
}