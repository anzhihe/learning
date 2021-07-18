package main
import (
	"fmt"
)
func modify(map1 map[int]int) {
	map1[10] = 900
}

//定义一个学生结构体
type Stu struct {
	Name string
	Age int
	Address string
}

func main() {

	//map是引用类型，遵守引用类型传递的机制，在一个函数接收map，
	//修改后，会直接修改原来的map

	map1 := make(map[int]int, 2)
	map1[1] = 90
	map1[2] = 88
	map1[10] = 1
	map1[20] = 2
	modify(map1)
	// 看看结果， map1[10] = 900 ,说明map是引用类型
	fmt.Println(map1) 


	//map的value 也经常使用struct 类型，
	//更适合管理复杂的数据(比前面value是一个map更好)，
	//比如value为 Student结构体 【案例演示，因为还没有学结构体，体验一下即可】
	//1.map 的 key 为 学生的学号，是唯一的
	//2.map 的 value为结构体，包含学生的 名字，年龄, 地址

	students := make(map[string]Stu, 10)
	//创建2个学生
	stu1 := Stu{"tom", 18, "北京"}
	stu2 := Stu{"mary", 28, "上海"}
	students["no1"] = stu1
	students["no2"] = stu2

	fmt.Println(students)

	//遍历各个学生信息
	for k, v := range students {
		fmt.Printf("学生的编号是%v \n", k)
		fmt.Printf("学生的名字是%v \n", v.Name)
		fmt.Printf("学生的年龄是%v \n", v.Age)
		fmt.Printf("学生的地址是%v \n", v.Address)
		fmt.Println()
	}

}