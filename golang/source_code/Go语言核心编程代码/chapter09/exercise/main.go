package main
import (
	"fmt"
)

/*

1)使用 map[string]map[string]sting 的map类型
2)key: 表示用户名，是唯一的，不可以重复
3)如果某个用户名存在，就将其密码修改"888888"，如果不存在就增加这个用户信息,
（包括昵称nickname 和 密码pwd）。
4)编写一个函数 modifyUser(users map[string]map[string]sting, name string) 完成上述功能
*/

func modifyUser(users map[string]map[string]string, name string) {

	//判断users中是否有name
	//v , ok := users[name]
	if users[name] != nil {
		//有这个用户
		users[name]["pwd"] = "888888"
	} else {
		//没有这个用户
		users[name] = make(map[string]string, 2)
		users[name]["pwd"] = "888888"
		users[name]["nickname"] = "昵称~" + name //示意

	}

}

func main() {

	users := make(map[string]map[string]string, 10)
	users["smith"] = make(map[string]string, 2)
	users["smith"]["pwd"] = "999999"
	users["smith"]["nickname"] = "小花猫"

	modifyUser(users, "tom")
	modifyUser(users, "mary")
	modifyUser(users, "smith")

	fmt.Println(users)

}


