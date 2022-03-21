package main

import (
	pb "TestPackage" //pb：为TestPackage包起的别名
	"fmt"
)

func main() {
	sum := pb.Add(12, 34, 56)
	fmt.Println("调用TestPackage下的求和函数：", sum)
	pb.ShowAll()
}
