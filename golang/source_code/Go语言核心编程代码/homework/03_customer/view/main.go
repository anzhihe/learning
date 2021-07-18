// main
package main

import (
	"fmt"
	"go_code/Demo/0801/03_customer/service"
	"strings"
)

type customerView struct {
	loop            bool
	key             int
	customerService *service.CustomersService
}

func NewCV() *customerView {
	return &customerView{
		loop:            true,
		key:             0,
		customerService: service.NewCustomers(),
	}

}

func (c *customerView) Add() {
	var name string
	fmt.Println("请输入用户姓名")
	fmt.Scanln(&name)
	var gender string
	fmt.Println("请输入性别")
	fmt.Scanln(&gender)
	var age int
	fmt.Println("请输入年龄")
	fmt.Scanln(&age)
	var phone string
	fmt.Println("请输入电话号码")
	fmt.Scanln(&phone)
	var email string
	fmt.Println("请输入邮箱")
	fmt.Scanln(&email)
	c.customerService.AddCustomer(name, gender, age, phone, email)
}

func (c *customerView) Reset() {
	var id int
	fmt.Println("请输入需要修改的用户ID(无需请输入-1)")
	fmt.Scanln(&id)
	if id == -1 {
		return
	}
	resetIndex := c.customerService.GetById(id)
	if resetIndex == -1 {
		fmt.Println("改用户不存在")
	} else {
		_, name, gender, age, phone, email := c.customerService.List()[resetIndex].GetInfo()
		fmt.Printf("姓名(%v):", name)
		fmt.Scanln(&name)
		fmt.Printf("性别(%v):", gender)
		fmt.Scanln(&gender)
		fmt.Printf("年龄(%v):", age)
		fmt.Scanln(&age)
		fmt.Printf("电话(%v):", phone)
		fmt.Scanln(&phone)
		fmt.Printf("邮箱(%v):", email)
		fmt.Scanln(&email)
		c.customerService.List()[resetIndex].Reset(name, gender, age, phone, email)
	}

}
func (c *customerView) DeleteCustomer() {
	var id int
	fmt.Println("请输入需要删除的用户ID(无需请输入-1)")
	fmt.Scanln(&id)
	var choice string
	if id == -1 {
		return
	} else {
		fmt.Printf("你确定删除ID为%v的客户吗?请输入y/n\n", id)
	}
	fmt.Scanln(&choice)
	for {
		if choice == "y" || choice == "Y" {
			c.customerService.DeleteId(id)
			fmt.Println("-------------------------客户删除成功-------------------------")
			break
		} else if choice == "n" || choice == "N" {
			break
		}
	}
}

func (c *customerView) List() {
	var customer = c.customerService.List()
	fmt.Println("---------------------------客户列表---------------------------")
	fmt.Println("编号\t姓名\t性别\t年龄\t电话\t\t邮箱")
	for _, v := range customer {
		a, b, c, d, e, f := v.GetInfo()
		fmt.Printf("%v\t%v\t%v\t%v\t%v\t\t%v\n", a, b, c, d, e, f)
	}
	fmt.Println("-------------------------客户列表完成-------------------------")
}

func (c *customerView) Query() {
	fmt.Println("请选择查询方式(-1退出查询):1,ID查询,2,姓名查询")
	var choice string
	fmt.Scanln(&choice)
	if choice == "-1" {
		return
	} else if choice == "1" {
		var id int
		fmt.Println("请输入需要查询的ID")
		fmt.Scan(&id)
		resetIndex := c.customerService.GetById(id)
		if resetIndex == -1 {
			fmt.Println("改用户不存在")
		} else {
			fmt.Println("---------------------------客户信息---------------------------")
			fmt.Println("编号\t姓名\t性别\t年龄\t电话\t\t邮箱")
			a, b, c, d, e, f := c.customerService.List()[resetIndex].GetInfo()
			fmt.Printf("%v\t%v\t%v\t%v\t%v\t\t%v\n", a, b, c, d, e, f)
			fmt.Println("-------------------------客户信息完成-------------------------")
			fmt.Println()
		}
	} else if choice == "2" {
		fmt.Println("请选择查询方式:1,精准查询,2,模糊查询")
		var choice2 string
		fmt.Scan(&choice2)
		var name string
		fmt.Println("请输入客户姓名")
		fmt.Scan(&name)
		var customer = c.customerService.List()
		if choice2 == "1" {
			var Isin = false
			for _, v := range customer {
				a, b, c, d, e, f := v.GetInfo()
				if b == name {
					Isin = true
					fmt.Printf("%v\t%v\t%v\t%v\t%v\t\t%v\n", a, b, c, d, e, f)
				}
			}
			if Isin == false {
				fmt.Println("改用户不存在")
			}
		} else if choice2 == "2" {
			var Isin = false
			for _, v := range customer {
				a, b, c, d, e, f := v.GetInfo()
				if strings.Contains(b, name) {
					Isin = true
					fmt.Printf("%v\t%v\t%v\t%v\t%v\t\t%v\n", a, b, c, d, e, f)
				}
			}
			if Isin == false {
				fmt.Println("改用户不存在")
			}
		}
	}
}

func (c *customerView) Menu() {
	for {
		fmt.Println("----------------客户信息管理软件----------------")
		fmt.Println("-----------------1 添 加 客 户-----------------")
		fmt.Println("-----------------2 修 改 客 户-----------------")
		fmt.Println("-----------------3 删 除 客 户-----------------")
		fmt.Println("-----------------4 客 户 列 表-----------------")
		fmt.Println("-----------------5 查 询 客 户-----------------")
		fmt.Println("-----------------6 退 出 系 统-----------------")
		fmt.Println("-----------------7 保 存 数 据-----------------")
		fmt.Println("-----------------8 读 取 数 据-----------------")
		fmt.Printf("请选择(1-8):")
		fmt.Scanln(&c.key)
		switch c.key {
		case 1:
			c.Add()
		case 2:
			c.Reset()
		case 3:
			c.DeleteCustomer()
		case 4:
			c.List()
		case 5:
			c.Query()
		case 6:
			for {
				var char string
				fmt.Println("你确定退出吗?请输入y/n")
				fmt.Scanln(&char)
				if char == "y" || char == "Y" {
					c.loop = false
					break
				} else if char == "n" || char == "N" {
					break
				}
			}
		case 7:
			c.customerService.SaveCustomer()
		case 8:
			c.customerService.LoadCustomer()
		default:
			fmt.Println("请输入正确的数字")
		}
		if !c.loop {
			break
		}
	}

}

func main() {
	var cv = NewCV()
	cv.Menu()
}
