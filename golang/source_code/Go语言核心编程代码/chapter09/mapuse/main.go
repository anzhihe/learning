package main
import (
	"fmt"
)

func main() {
	//第一种使用方式
	
	var a map[string]string
	//在使用map前，需要先make , make的作用就是给map分配数据空间
	a = make(map[string]string, 10)
	a["no1"] = "宋江" //ok?
	a["no2"] = "吴用" //ok?
	a["no1"] = "武松" //ok?
	a["no3"] = "吴用" //ok?
	fmt.Println(a)

	//第二种方式
	cities := make(map[string]string)
	cities["no1"] = "北京"
	cities["no2"] = "天津"
	cities["no3"] = "上海"
	fmt.Println(cities)

	//第三种方式
	heroes := map[string]string{
		"hero1" : "宋江",
		"hero2" : "卢俊义",
		"hero3" : "吴用",
	}
	heroes["hero4"] = "林冲"
	fmt.Println("heroes=", heroes)


	//案例
	/*
	课堂练习：演示一个key-value 的value是map的案例
	比如：我们要存放3个学生信息, 每个学生有 name和sex 信息
	思路:   map[string]map[string]string

	*/
	studentMap := make(map[string]map[string]string)
	
	studentMap["stu01"] =  make(map[string]string, 3)
	studentMap["stu01"]["name"] = "tom"
	studentMap["stu01"]["sex"] = "男"
	studentMap["stu01"]["address"] = "北京长安街~"

	studentMap["stu02"] =  make(map[string]string, 3) //这句话不能少!!
	studentMap["stu02"]["name"] = "mary"
	studentMap["stu02"]["sex"] = "女"
	studentMap["stu02"]["address"] = "上海黄浦江~"

	fmt.Println(studentMap)
	fmt.Println(studentMap["stu02"])
}