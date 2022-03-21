package main

import (
	"fmt"
	"sync"
)

func init() { //init函数独立于主函数 main();并且先于主函数运行
	fmt.Println("这里是init函数，一般用于初始化操作！")
}
func main() {
	wg := sync.WaitGroup{} //定义
	wg.Add(100)            //添加子go程数量
	for i := 0; i < 100; i++ {
		go func(n int) {
			fmt.Printf("第%v个go程正在执行操作！\n", n)
			wg.Done() //子go程数量减1
		}(i)
	}
	wg.Wait() //阻塞，直到go程数量 <=0

}
