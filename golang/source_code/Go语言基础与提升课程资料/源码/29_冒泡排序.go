package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	//第一步：先产生随机数，对产生的随机数进行排序
	rand.Seed(time.Now().UnixNano()) //通过时间来产生随机数种子
	arr := make([]int, 0)
	for i := 0; i < 10; i++ {
		arr = append(arr, rand.Intn(100)) //产生0-100之间的数，[0,100)
	}
	fmt.Println("切片中的原始数据：", arr)
	BubbleSort(arr)
	fmt.Println("排序之后切片的数据为：", arr)
}
func BubbleSort(a []int) {
	n := len(a)
	for i := 0; i < n-1; i++ { //控制冒泡的次数
		for j := 0; j < n-1-i; j++ { //每次冒泡 比较相邻元素的次数
			if a[j] > a[j+1] {
				a[j], a[j+1] = a[j+1], a[j] //不满足条件，进行交换
			}
		}
	}
}
