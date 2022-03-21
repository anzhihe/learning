package main

import "fmt"

type Machine interface {
	run(operate string) (status bool)
}
type Car struct {
	name string
	mode string
}
type Computer struct {
	name     string
	cpuCount uint8
}

func (c *Car) run(operate string) (status bool) {
	fmt.Println(c.name, "car 正在执行", operate)
	return true
}
func (c *Computer) run(operate string) (status bool) {
	fmt.Println(c.name, "computer正在执行", operate)
	return true
}
func main() {
	car := Car{name: "长城", mode: "越野"}
	run(&car) //实现了多态；注意：传递的是变量car的地址
	computer := Computer{name: "华为", cpuCount: 16}
	run(&computer)

}
func run(m Machine) { //函数实现了多态，注意：形式参数为接口类型；
	m.run("启动！") //具体执行那个对象的方法，是由调用函数的对象决定
}
