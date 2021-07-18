package main
import "fmt"
func main() {

	//100以内的数求和，求出 当和 第一次大于20的当前数
	sum := 0
	for i := 1; i <= 100; i++ {
		sum += i //求和
		if sum > 20 {
			fmt.Println("当sum>20时，当前数是", i)
			break
		}
	}

	//实现登录验证，有三次机会，如果用户名为”张无忌” ,密码”888”提示登录成功，
	//否则提示还有几次机会.

	var name string 
	var pwd string
	var loginChance = 3 //
	for i := 1 ; i <= 3; i++ {
		fmt.Println("请输入用户名")
		fmt.Scanln(&name)
		fmt.Println("请输入密码")
		fmt.Scanln(&pwd)

		if name == "张无忌" && pwd == "888" {
			fmt.Println("恭喜你登录成功!")
			break
		} else {
			loginChance--
			fmt.Printf("你还有%v次登录机会，请珍惜\n", loginChance)
		}
	}

	if loginChance == 0 {
		fmt.Println("机会用完，没有登录成功!")
	}


	
}