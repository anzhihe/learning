package main

import "fmt"

func main() {
	var m1 = map[int]string{1: "张三", 2: "李四", 3: "小明"}
	fmt.Println(m1)
	m2 := map[string]string{"Go": "Go语言", "Java": "Java语言"}
	fmt.Println(m2)
	//为map添加数据
	m2["BlockChain"] = "区块链技术"
	fmt.Println(m2)
	//数据的修改
	m2["Java"] = "Java技术" //map数据类型的修改，也就是将key对应的数据进行覆盖
	fmt.Println(m2)
	m3 := make(map[int]string, 5) //5代表map类型的变量m3的容量，map类型的变量可以动态扩容
	m3[111] = "hello Go 语言"
	fmt.Println("===============Map的遍历方法1==========================")
	for k, v := range m2 {
		fmt.Println(k, v)
	}
	fmt.Println("===============Map的遍历方法2==========================")
	for k := range m2 { //如果只有1个参数，只取key值
		fmt.Println(k)
	}
	fmt.Println("===============Map的数据删除==========================")
	fmt.Println("m2原有的数据为：", m2)
	delete(m2, "Java")
	fmt.Println("m2删除之后的数据为：", m2)

}
