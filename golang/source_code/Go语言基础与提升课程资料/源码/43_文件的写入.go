package main

import (
	"fmt"
	"io"
	"os"
)

func main() {
	//path := "E:\\GoSrc\\src\\go.txt"
	path := "E:/GoSrc/src/go.txt"
	CreateFile1(path)
}
func CreateFile1(path string) error {
	file, err := os.Create(path)
	if err != nil {
		fmt.Println("文件创建失败！", err)
		return err
	}
	defer file.Close()
	for i := 0; i < 10; i++ {
		file.WriteString("Go 语言是一门很强大的语言\n")
	}
	file.WriteAt([]byte("文件操作"), 0)
	n, err := file.Seek(0, io.SeekEnd) //获取偏移量（0，文件的结尾）
	if err != nil {
		return err
	}
	file.WriteAt([]byte("123456"), n)
	return nil
}
