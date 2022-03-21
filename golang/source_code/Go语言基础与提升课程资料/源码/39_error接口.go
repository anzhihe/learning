package main

import (
	"errors"
	"fmt"
	"strconv"
)

func main() {
	fmt.Println("=================基本使用========================")
	err := errors.New("这是一个错误信息！")
	fmt.Println(err.Error())
	str := "Go 语言error接口！"
	e := fmt.Errorf("这里是错误信息，对应的错误为：%v", str)
	fmt.Println(e.Error())
	fmt.Println("================函数调用使用==================")
	res, err := Dev(200, 3)
	if err == nil {
		fmt.Println("计算的结果为：", res)
		return
	}
	fmt.Println("计算错误，错误信息：", err)
}
func Dev(a, b float64) (float64, error) {
	if b == 0 {
		return 0, errors.New("被除数不能为0")
	}
	str := fmt.Sprintf("%.3f", a/b)
	return strconv.ParseFloat(str, 64)
	//return a / b, nil
}
