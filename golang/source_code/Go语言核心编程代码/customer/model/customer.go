package model

import (
	"fmt"
)

type Customer struct {
	Id int
	Name string
	Gender string
	Age int
	Phone string
	Email string
}

//获取一个Customer
func NewCustomer(id int, name string, gender string, age int, 
	phone string, email string) *Customer {
	return &Customer{
		Id : id,
		Name : name,
		Gender : gender,
		Age : age,
		Phone : phone,
		Email : email,
	}
}

//获取一个Customer, 不提供id
func NewCustomer2(name string, gender string, age int, 
	phone string, email string) *Customer {
	return &Customer{
		Name : name,
		Gender : gender,
		Age : age,
		Phone : phone,
		Email : email,
	}
}

//返回Customer的信息
func (this *Customer) GetInfo() string {

	info := fmt.Sprintf("%v\t%v\t%v\t%v\t%v\t%v", this.Id, this.Name, this.Gender, 
		this.Age, this.Phone, this.Email)
	return info
}


