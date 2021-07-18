package main

//引入包
import (
	"fmt"
	"go_code/customer/service"
	"go_code/customer/model"
)

type CustomerView struct {

	//定义一个字段，控制菜单显示是否退出
	loop bool
	//定义一个字段，接收用户输入
	key string
	//定义一个CustomerService 字段，主要用于完成对客户信息的各种操作。
	customerService *service.CustomerService
}

//显示主菜单
//	-----------------客户信息管理软件-----------------
//
//    1 添 加 客 户
//    2 修 改 客 户
//    3 删 除 客 户
//    4 客 户 列 表
//    5 退           出
//
//    请选择(1-5)：_

func (this *CustomerView) mainMenu() {

	for {

		fmt.Println("-----------------客户信息管理软件-----------------")
		fmt.Println();
		fmt.Println("                 1 添 加 客 户")
		fmt.Println("                 2 修 改 客 户")
		fmt.Println("                 3 删 除 客 户")
		fmt.Println("                 4 客 户 列 表")
		fmt.Println("                 5 退          出")
		fmt.Print("请选择(1-5)：")
		fmt.Scanln(&this.key)

		switch (this.key) {
		case "1":
			this.add()
		case "2":
			//同学们自己加入
		case "3":
			this.delete()
		case "4":
			//调用方法显示客户信息
			this.list()
		case "5":
			this.loop = false
		default:
			fmt.Println("输入错误");
		}

		if !this.loop {
			break
		}

	}
}

//编写一个方法，可以显示客户信息
//	---------------------------客户列表---------------------------
//	编号  姓名       性别    年龄   电话            邮箱
//	 1    张三       男      30     010-56253825   abc@email.com
//	 2    李四       女      23     010-56253825    lisi@ibm.com
//	 3    王芳       女      26     010-56253825   wang@163.com
//	-------------------------客户列表完成-------------------------

func (this *CustomerView) list() {

	//调用 customerService 获取到 客户信息切片
	customerList := this.customerService.List()

	//显示
	fmt.Println("---------------------------客户列表---------------------------")
	fmt.Println("编号\t姓名\t性别\t年龄\t电话\t邮箱")

	//遍历
	for i := 0; i < len(customerList); i++ {
		fmt.Println(customerList[i].GetInfo())
	}
	fmt.Println("---------------------------客户列表完成---------------------------")
	
}

//添加客户
//	---------------------添加客户---------------------
//	姓名：张三
//	性别：男
//	年龄：30
//	电话：010-56253825
//	邮箱：zhang@abc.com
//	---------------------添加完成---------------------

func (this *CustomerView) add() {

	fmt.Println("---------------------添加客户---------------------")
	fmt.Println("姓名：")
	name := ""
	fmt.Scanln(&name)
	fmt.Println("性别：")
	gender := ""
	fmt.Scanln(&gender)
	age := 0
	fmt.Println("年龄：")
	fmt.Scanln(&age)
	fmt.Println("电话：");
	phone := ""
	fmt.Scanln(&phone)
	fmt.Println("邮箱：");
	email := ""
	fmt.Scanln(&email)

	//根据用户输入，创建一个Customer对象
	customer := model.NewCustomer2(name, gender, age, phone, email)
	
	if(this.customerService.Add(customer)){
		fmt.Println("---------------------添加客户成功---------------------");
	}else{
		fmt.Println("---------------------添加客户失败---------------------");
	}
}

//删除
//	---------------------删除客户---------------------
//	请选择待删除客户编号(-1退出)：1
//	确认是否删除(Y/N)：y
//	---------------------删除完成---------------------

func (this *CustomerView) delete() {

	fmt.Println("---------------------删除客户---------------------")
	fmt.Println("请选择待删除客户编号(-1退出)")
	id := 0
	fmt.Scanln(&id)
	//如果用户输入-1
	if id == -1 {
		return
	}
	fmt.Println("确认是否删除(Y/N)：")

	choice := ""
	fmt.Scanln(&choice) // 可以
	
	if choice == "Y" || choice == "y"  {
		
		if this.customerService.Delete(id) {
			fmt.Println("---------------------删除完成---------------------")
		} else {
			fmt.Println("---------------------删除失败,id不存在---------------------")
		}
	}
} 


func main() {

	customerView := CustomerView{
		loop : true,
	}
	customerView.customerService = service.NewCustomerService()
	customerView.mainMenu()
}