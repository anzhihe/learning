// customers
package model

type Customer struct {
	Id     int
	Name   string
	Gender string
	Age    int
	Phone  string
	Email  string
}

var idNums int

func NewCustomer(name string, gender string, age int, phone string, email string) Customer {
	idNums++
	return Customer{idNums, name, gender, age, phone, email}
}

func (c *Customer) GetInfo() (int, string, string, int, string, string) {
	return c.Id, c.Name, c.Gender, c.Age, c.Phone, c.Email
}

func (c *Customer) GetId() int {
	return c.Id
}

func (c *Customer) Reset(name string, gender string, age int, phone string, email string) {
	if name != "" {
		c.Name = name
	}
	if gender != "" {
		c.Gender = gender
	}
	if age != 0 {
		c.Age = age
	}
	if phone != "" {
		c.Phone = phone
	}
	if email != "" {
		c.Email = email
	}

}
