// customersService
package service

import (
	"bufio"
	"encoding/json"
	"fmt"
	"go_code/homework13day/03_customer/model"
	"io"
	"os"
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
	var savePath = "./customer.txt"
	file, err := os.OpenFile(savePath, os.O_WRONLY|os.O_CREATE, 0666)
	defer file.Close()
	if err != nil {
		fmt.Println("打开文件时出错:", err)
		panic(err)
	}
	con, err := json.Marshal(cs)
	if err != nil {
		fmt.Println("序列化时出错:", err)
		panic(err)
	}
	writer := bufio.NewWriter(file)
	_, err = writer.Write(con)
	if err != nil {
		fmt.Println("写入json时出错:", err)
		panic(err)
	}
	writer.Flush()
}

func (cs *CustomersService) LoadCustomer() {
	var savePath = "./customer.txt"
	file, err := os.OpenFile(savePath, os.O_RDONLY, 0666)
	defer file.Close()
	if err != nil {
		fmt.Println("打开文件时出错:", err)
		panic(err)
	}
	reader := bufio.NewReader(file)
	con, err := reader.ReadBytes('\n')
	if err == io.EOF {
		err := json.Unmarshal(con, cs)
		if err != nil {
			fmt.Println("反序列化时出错:", err)
			panic(err)
		}

	}

}
