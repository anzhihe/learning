package main

import "fmt"

//接口的定义
type Humaner interface {
	sayHello() //注意：在接口中的方法只有声明，没有实现。由对象对应的方法来实现
}
type Student3 struct {
	name string
	id   int
}

//复杂接口
type USB interface {
	Start(operate string) (res byte, err error)
	Stop() string
}
type Phone struct {
	id   int
	name string
}
type Camera struct {
	id   int
	mode string
}

func (p *Phone) Start(operate string) (res byte, err error) {
	fmt.Println(p.name, "phone 正在执行...", operate)
	res = 1
	err = nil
	return
}
func (p *Phone) Stop() string {
	return "phone已经停止工作。。。"
}
func (c *Camera) Start(operate string) (res byte, err error) {
	fmt.Println("编号为：", c.id, "的camera正在执行...")
	return 1, nil
}
func (c *Camera) Stop() string {
	return "camera已经停止工作..."
}

func (s *Student3) sayHello() {
	fmt.Println("接口的实现")
	fmt.Println(s.name, s.id)
}
func main() {
	//接口的调用
	s := Student3{id: 10001, name: "晓晓"}
	s.sayHello()
	fmt.Println("==============复杂接口方法的调用==============")
	p := Phone{id: 0x001, name: "华为"}
	res, err := p.Start("拍照") //自动添加变量的快捷键：Ctrl+Alt+v
	fmt.Println(res, err)

}
