// customersService
package service

import (
	"encoding/json"
	"fmt"
	"go_code/Demo/0801/03_customer/model"

	"github.com/garyburd/redigo/redis"
)

type CustomersService struct {
	Customers []model.Customer
}

func NewCustomers() *CustomersService {
	var customersService CustomersService
	customersService.Customers = append(customersService.Customers, model.NewCustomer("zs", "男", 18, "151", "zs151@qq.com"))
	return &customersService
}

func (cs *CustomersService) List() []model.Customer {
	return cs.Customers
}

func (cs *CustomersService) AddCustomer(name string, gender string, age int, phone string, email string) {
	cs.Customers = append(cs.Customers, model.NewCustomer(name, gender, age, phone, email))
	return
}

func (cs *CustomersService) DeleteId(id int) {
	index := cs.GetById(id)
	if index == -1 {
		fmt.Println("改用户不存在,无法删除")
	} else {
		cs.Customers = append(cs.Customers[:index], cs.Customers[index+1:]...)

	}
}

func (cs *CustomersService) GetById(id int) int {
	index := -1
	for i, v := range cs.Customers {
		if id == v.GetId() {
			index = i
			break
		}
	}
	return index
}

func (cs *CustomersService) SaveCustomer() {
	conn, err := redis.Dial("tcp", "127.0.0.1:6379")
	defer conn.Close()
	if err != nil {
		fmt.Println("连接数据库出错:", err)
	}
	data, err := json.Marshal(cs.Customers)
	if err != nil {
		fmt.Println("序列化出错:", err)
	}
	_, err = conn.Do("set", "Cutomers", data)
	if err != nil {
		fmt.Println("储存数据时错误:", err)
	}
}

func (cs *CustomersService) LoadCustomer() {
	conn, err := redis.Dial("tcp", "127.0.0.1:6379")
	defer conn.Close()
	if err != nil {
		fmt.Println("连接数据库出错:", err)
	}

	result, err := redis.Bytes(conn.Do("get", "Cutomers"))
	if err != nil {
		fmt.Println("储存数据时错误:", err)

	}
	err = json.Unmarshal(result, &cs.Customers)
	if err != nil {
		fmt.Println("反序列化出错:", err)
	}
}
