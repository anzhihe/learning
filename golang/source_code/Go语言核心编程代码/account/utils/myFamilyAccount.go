package utils
import (
	"fmt"
)

type MyFamilyAccount struct {

	// 定义一个字段
	loop bool
	// 用于接收用户的输入
	key string
	// 记录用户的收入和支出情况，该字符串会拼接
	details string 
	// 保存账号的金额
	balance float64
	// 定义一个标识符
	flag bool
	// 定义一个金额
	money float64
	// 声明一个说明
	note string
}

func NewMyFamilyAccount() *MyFamilyAccount {
	return &MyFamilyAccount{
		loop : true,
		key : "",
		details : "收支\t账户金额\t收支金额\t说    明",
		balance : 10000.0,
		flag : false,
		money : 0.0,
		note : "",
	}
}

func (this *MyFamilyAccount) MainMenu() {

	for {
		// 1. 先输出这个主菜单
		fmt.Println("-----------------家庭收支记账软件-----------------")
		fmt.Println("			1 收支明细")
		fmt.Println("			2 登记收入")
		fmt.Println("			3 登记支出")
		fmt.Println("			4 退出")
		fmt.Print("请选择(1-4):")
		fmt.Scanln(&this.key)

		// 使用switch
		switch (this.key) {
		case "1":
			this.showDetails()
		case "2":
			this.income()
		case "3":
			this.pay()
		case "4":
			this.loop = this.exit()
		default:
			fmt.Println("请输入正确的选项...")
		}
		if !this.loop {
			break
		}

	}
	fmt.Println("你退出了软件的使用。。。。")
}

//显示收支明细的方法
func (this *MyFamilyAccount) showDetails() {

	// 增加我代码。。
	fmt.Println("-----------------当前收支明细记录-----------------")
	if this.flag {
		fmt.Println(this.details)
	} else {
		fmt.Println("没有任何收支明细")
	}
}

//登记收入
func (this *MyFamilyAccount) income() {

	fmt.Print("本次收入金额:")
	fmt.Scanln(&this.money)
	fmt.Print("本次收入说明：")
	fmt.Scanln(&this.note)
	this.balance += this.money
	this.details += fmt.Sprintf("\n收入\t%v\t%v\t%v", 
		this.balance, this.money, this.note)
	this.flag = true
}

//登记支出

func (this *MyFamilyAccount) pay() {

	fmt.Print("本次支出金额:")
	fmt.Scanln(&this.money)
	fmt.Print("本次支出说明：")
	fmt.Scanln(&this.note)
	
	//判断
	if this.money > this.balance {
		fmt.Println("朋友，余额不足 ...")
		return // 终止一个方法使用return
	} 
	this.balance -= this.money
	this.details += fmt.Sprintf("\n支出\t%v\t%v\t%v", 
		this.balance, this.money, this.note)
	this.flag = true
}

//退出

func (this *MyFamilyAccount) exit() bool {
	// 修改loop
	fmt.Println("确定要退出吗？y/n");
		
	choice := ""
	//循环判断，直到输入y 或者 n

	for {
		fmt.Scanln(&choice)
		if choice == "y" || choice == "n" {
			break
		}
		fmt.Print("你的输入有误，请输入y/n:")
	}
	if choice == "y" {
		return false
	}  else {
		return true
	}
}