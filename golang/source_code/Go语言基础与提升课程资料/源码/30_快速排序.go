package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	rand.Seed(time.Now().UnixNano()) //产生随机数种子
	arr := make([]int, 0)
	for i := 0; i < 11; i++ {
		arr = append(arr, rand.Intn(100)) //[0,100)
	}
	fmt.Println("排序之前的切片内容为：", arr)
	quickSort(0, len(arr)-1, arr)
	fmt.Println("排序之后的切片为：", arr)
}
func quickSort(left, right int, arr []int) {
	l := left
	r := right
	value := arr[(l+r)/2] //取中间值，作为比较的参考值
	for l <= r {
		for arr[l] < value { //左指针对应的数据满足条件，左指针右移
			l++
		}
		for arr[r] > value { //右指针对应的数据满足条件，右指针左移
			r--
		}
		if l > r {
			break
		}
		arr[l], arr[r] = arr[r], arr[l] //交换数据
		r--
		l++
	}
	if l == r {
		l++
		r--
	}
	if l < right { //右半部分的递归
		quickSort(l, right, arr)
	}
	if r > left { //左半部分的递归
		quickSort(left, r, arr)
	}
}
