package service

import (
	_ "fmt"
	"go_code/customer/model"
)

type CustomerService struct {
	//定义一个客户切片,可以存放客户信息
	customers []*model.Customer
	//定义客户的实际个数
	customerNum int
}

//先创建一个Customer对象,放到 CustomerService的Customers切片中
//作为测试数据
func NewCustomerService() *CustomerService {

	customerService := &CustomerService{}

	//customerService.customers = make([]model.Customer, 1)
	customerService.customerNum = 1
	customer := model.NewCustomer(1, "张三", "男",
		10, "999", "zs@sohu.com")
	customerService.customers = append(customerService.customers, customer)

	return customerService
}

//返回客户的信息数组

func (this *CustomerService) List()  []*model.Customer {
	return this.customers
}

//完成添加客户的功能
func (this *CustomerService) Add(customer *model.Customer) bool {

	this.customerNum++
	//这时我们可以这个customer一个id
	customer.Id = this.customerNum
	this.customers = append(this.customers, customer)
	
	return true
	
}


//删除一个客户
func (this *CustomerService) Delete(id int) bool {

	//先根据id去得到该id的客户对应元素下标
	index := this.FindById(id)
	
	if index == -1 {
		return false
	}
	//找到，删除切片对应的index的元素
	this.customers = append(this.customers[:index], 
		this.customers[index+1:]...)
	//this.customerNum--
	return true
	
}

//先根据id去得到该id的客户对应元素下标
//如果找到就返回对应的下标，如果找不到，我们返回-1
func (this *CustomerService) FindById(id int) int {
	index := -1
	for i := 0; i < this.customerNum; i++ {
		if this.customers[i].Id == id {
			index = i
			break
		}
	}
	return index
}

