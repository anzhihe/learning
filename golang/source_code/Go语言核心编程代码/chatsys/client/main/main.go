package main
import (
	"fmt"
	"os"
	"go_code/chatsys/client/process"
)


var userId int
var passwd string
var userName string

func main() {

	//定义一个变量，控制菜单显示是否退出
	//var loop bool = true
	//接收用户的输入选择
	var key int
//	for loop {
		fmt.Println("-----------------欢迎登陆多人聊天系统:---------------")
		fmt.Println("\t\t\t 1 登录聊天系统")
		fmt.Println("\t\t\t 2 注册用户")
		fmt.Println("\t\t\t 3 退出系统")
		fmt.Println("请选择(1-3):")
		fmt.Println("-----------------------------")

		fmt.Scanf("%d\n", &key)
		switch key {
			case 1:
				//fmt.Println("登录...") //登录处理
				fmt.Println("请输入用户id:")
				fmt.Scanf("%d\n", &userId)
				process.UserId = userId
				fmt.Println("请输入用户密码:")
				fmt.Scanf("%s\n", &passwd)
				fmt.Println()
				//创建一个UserProcessor
				up := &process.UserProcessor{
				}
				up.Login(userId, passwd)
			case 2:
				fmt.Println("注册用户") //注册处理
				fmt.Println("请输入新用户id:")
				fmt.Scanf("%d\n", &userId)
				fmt.Println("请输入新用户密码:")
				fmt.Scanf("%s\n", &passwd)
				fmt.Println("请输入新用户名字:")
				fmt.Scanf("%s\n", &userName)
				fmt.Println()
				//创建一个UserProcessor
				up := &process.UserProcessor{
				}
				up.Register(userId, passwd, userName)
				//注册后，就退出系统
				os.Exit(0)
			case 3:
				fmt.Println("退出系统....") 
				os.Exit(0)
			default:
				fmt.Println("你是输入有误, 请重新输入...")
		}
//	}

		
}
