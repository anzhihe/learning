package TestPackage

import "fmt"

func show() { //函数首字母小写，只能被相同包下的函数调用
	fmt.Println("这里是TestPackage包下的show()函数")
}
