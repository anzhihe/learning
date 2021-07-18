package main
import (
	"fmt"
)

func main() {

	/*
	一个养鸡场有6只鸡，它们的体重分别是3kg,5kg,1kg,
	3.4kg,2kg,50kg 。请问这六只鸡的总体重是多少?平
	均体重是多少? 请你编一个程序。=》数组

	*/

	//思路分析：定义六个变量，分别表示六只鸡的，然后求出和，然后求出平均值。
	hen1 := 3.0 
	hen2 := 5.0
	hen3 := 1.0 
	hen4 := 3.4 
	hen5 := 2.0 
	hen6 := 50.0
	
	totalWeight := hen1 + hen2 + hen3 + hen4 + hen5 + hen6
	//fmt.Sprintf("%.2f", totalWeight / 6) 将 totalWeight / 6 四舍五入保留到小数点2返回值
	avgWeight := fmt.Sprintf("%.2f", totalWeight / 6)
	fmt.Printf("totalWeight=%v avgWeight=%v\n", totalWeight, avgWeight)


	//使用数组的方式来解决问题

	//1.定义一个数组
	var hens [7]float64
	//2.给数组的每个元素赋值， 元素的下标是从0开始的  0-5
	hens[0] = 3.0  //hens数组的第一个元素 hens[0]
	hens[1] = 5.0  //hens数组的第2个元素 hens[1]
	hens[2] = 1.0 
	hens[3] = 3.4 
	hens[4] = 2.0 
	hens[5] = 50.0 
	hens[6] = 150.0  //增加一只鸡
	//3.遍历数组求出总体重
	totalWeight2 := 0.0 
	for i := 0; i < len(hens); i++ {
		totalWeight2 += hens[i]
	}

	//4.求出平均体重
	avgWeight2 := fmt.Sprintf("%.2f", totalWeight2 / float64(len(hens)))  
	fmt.Printf("totalWeight2=%v avgWeight2=%v", totalWeight2, avgWeight2)

  
}