package main

import (
	"fmt"
	"io"
	"os"
)

func main() {
	path := "E:/GoSrc/src/go.txt"
	//ReadFile1(path)
	ReadFile2(path)
}
func ReadFile1(path string) error {
	file, err := os.Open(path)
	if err != nil {
		fmt.Println("文件打开失败！")
		return err
	}
	defer file.Close()
	buf := make([]byte, 1024*4) //创建4K大小的切片缓冲区
	n, err := file.Read(buf)
	if err != nil && err != io.EOF {
		fmt.Println("文件读取错误！")
		return nil
	}
	fmt.Println("去取到的内容为：", string(buf[:n]))
	return nil
}
func ReadFile2(path string) error {
	file, err := os.OpenFile(path, os.O_RDWR, 666) //读写 方式打开；666：代表：文件所有者、群组用户、其他用户；
	// 参考；文件所有者、群组用户、其他用户都具有读写权限（参考：https://blog.csdn.net/pythonw/article/details/80263428）
	if err != nil {
		fmt.Println("文件打开失败！")
		return err
	}
	defer file.Close()
	buf := make([]byte, 1024)
	for {
		n, err := file.Read(buf)
		if err != nil && err != io.EOF {
			fmt.Println("文件读取错误！")
			return err
		}
		if n == 0 {
			break
		}
		fmt.Println(string(buf[:n]))
	}
	return nil
}
