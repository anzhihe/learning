package main

import (
	"fmt"
	"sync"
	"time"
)

var f1 = false
var f2 = false
var mutex sync.Mutex //定义互斥锁

func main() {
	go person01("hello")
	go person02("word!")
	for {
		if f1 == true && f2 == true {
			break
		}
	}
}
func printer(str string) {
	mutex.Lock()         //加锁
	defer mutex.Unlock() //解锁操作
	for _, data := range str {
		fmt.Printf("%c", data)
		time.Sleep(time.Second * 1)
	}
	fmt.Println()

}
func person01(str string) {
	printer(str)
	f1 = true
}
func person02(str string) {
	printer(str)
	f2 = true
}
