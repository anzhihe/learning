package main

import (
	"fmt"
	"io"
	"os"
)

func main() {
	var srcPath string
	var dstPath string
	fmt.Println("请输入源文件的名称（包括详细的路径）")
	fmt.Scan(&srcPath)
	fmt.Println("请输入目标文件的名称（包括详细的路径）")
	fmt.Scan(&dstPath)
	//fmt.Println(srcPath, dstPath)
	if srcPath == dstPath {
		fmt.Println("路径（包括文件名）雷同")
		return
	}
	CopyFile(srcPath, dstPath)
}
func CopyFile(srcPath, dstPath string) error {
	//打开源文件
	srcFile, err := os.Open(srcPath)
	if err != nil {
		fmt.Println("打开文件错误！", err)
		return err
	}
	defer srcFile.Close()
	//创建一下新文件
	dstFile, err := os.Create(dstPath)
	if err != nil {
		fmt.Println("打开文件失败！", err)
		return err

	}
	defer dstFile.Close()
	//创建一个缓冲区
	buf := make([]byte, 4*1024)
	for {
		//读取文件，将文件内容（源文件）读取到缓冲区中
		n, err := srcFile.Read(buf)
		if err != nil && err != io.EOF {
			fmt.Println("读取源文件错误！", err)
			return err
		}
		if n == 0 {
			fmt.Println("文件拷贝完成！")
			break
		}
		//将缓冲区中的数据写入目标文件
		dstFile.Write(buf[:n])
	}
	return nil
}
